"""
check_peak_coastdown_loft.py  (3 Oct 2026)

Re-runs the grid-flexibility figures from thermal-counterfactual-gb
(Findings 1, 2 and 4: peak reduction per 1,000 homes, coastdown hours, and the
cold-snap reheat spike) with the baseline loft ALREADY insulated (~200mm,
roof U 0.2). Everything else is as published: design -3C, 21C setpoint,
preheat 22C, comfort floor 19C, COP 2.5, 400W gains, C = 10 kWh/K, and the
air-node sweep of 2-20%.

What this does NOT re-run: the repo's hourly Dec-2022 cold-snap simulation
(notebooks/02-03), whose synthetic hourly profile is not committed to the
repo. The "breach temperature" below is an INDICATIVE constant-temperature
1R1C check: the outdoor temperature at which coastdown from 22C to 19C falls
below the 4-hour peak window. Use it for the direction and rough size of the
shift, not as a replacement for the published -9.4C.

Run:  python src/check_peak_coastdown_loft.py /path/to/thermal-counterfactual-gb
"""
import sys, yaml
repo = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, f"{repo}/src")
from thermal_counterfactual_gb.physics import (
    EnvelopeState, heat_loss_coefficient_w_per_k, two_node_conductances_w_per_k,
    simulate_2r2c_coastdown_hours, coastdown_hours, thermal_time_constant_hours,
    net_heating_power_kw)

cfg = yaml.safe_load(open(f"{repo}/configs/tenure_insulation_assumptions.yml"))
g, env = cfg["geometry"], cfg["envelope_states"]
C = cfg["thermal_capacity"]["c_kwh_per_k"]
GAINS, COP, DESIGN, SETPOINT, PREHEAT, FLOOR_C = 400, 2.5, -3, 21, 22, 19
F_AIR = [0.02, 0.05, 0.10, 0.20]
STRESS_T = -9.4            # published breach point (hourly simulation)
STREET = {"diversified street": 22, "worst-tenure street": 27}   # homes reheating, of 30 (published)
AREAS = dict(wall_area_m2=g["opaque_wall_area_m2"], roof_area_m2=g["roof_area_m2"],
             floor_area_m2=g["ground_floor_area_m2"], window_area_m2=g["window_area_m2"],
             heated_volume_m3=g["heated_volume_m3"])

def state(name, **o):
    s = dict(env[name]); s.update(o)
    return EnvelopeState(s["wall_u_w_per_m2k"], s["roof_u_w_per_m2k"], s["floor_u_w_per_m2k"],
                         s["window_u_w_per_m2k"], s["infiltration_ach"])

def H(s):
    return heat_loss_coefficient_w_per_k(s, AREAS["wall_area_m2"], AREAS["roof_area_m2"],
                                         AREAS["floor_area_m2"], AREAS["window_area_m2"],
                                         AREAS["heated_volume_m3"])

def breach_temp(h):
    tau = thermal_time_constant_hours(C, h); lo, hi = -40.0, 15.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if coastdown_hours(tau, PREHEAT, FLOOR_C, mid, h, GAINS) > 4: hi = mid
        else: lo = mid
    return lo

epc = state("epc_c_package")
epc_peak = net_heating_power_kw(H(epc), SETPOINT, DESIGN, COP, GAINS)
for label, base in [("AS PUBLISHED (bare loft, roof U 2.3)", state("baseline")),
                    ("LOFT ALREADY AT ~200mm (roof U 0.2)", state("baseline", roof_u_w_per_m2k=0.2))]:
    h = H(base)
    peak = net_heating_power_kw(h, SETPOINT, DESIGN, COP, GAINS)
    cds = [simulate_2r2c_coastdown_hours(f, C, *two_node_conductances_w_per_k(base, **AREAS),
                                         t_start_c=PREHEAT, t_min_c=FLOOR_C, t_outdoor_c=DESIGN,
                                         internal_gains_w=GAINS) for f in F_AIR]
    reheat = net_heating_power_kw(h, FLOOR_C, STRESS_T, COP, GAINS)
    print(label)
    print(f"  Peak demand at -3C: {peak:.2f} kW/home (EPC-C {epc_peak:.2f})"
          f" -> reduction {peak-epc_peak:.2f} kW/home = {peak-epc_peak:.1f} MW per 1,000 homes")
    print("  Unretrofitted 2R2C coastdown at -3C: " +
          ", ".join(f"{v:.1f}h" if v else ">40h" for v in cds))
    print(f"  Indicative 1R1C breach temperature (coastdown < 4h): {breach_temp(h):.1f}C")
    print(f"  Reheat per home at {STRESS_T}C: {reheat:.2f} kW -> " +
          ", ".join(f"{k} {n} homes = {n*reheat:.1f} kW" for k, n in STREET.items()))
    print()

cds_epc = [simulate_2r2c_coastdown_hours(f, C, *two_node_conductances_w_per_k(epc, **AREAS),
                                         t_start_c=PREHEAT, t_min_c=FLOOR_C, t_outdoor_c=DESIGN,
                                         internal_gains_w=GAINS) for f in F_AIR]
print("EPC-C 2R2C coastdown at -3C (unchanged): " + ", ".join(f"{v:.1f}h" for v in cds_epc))
