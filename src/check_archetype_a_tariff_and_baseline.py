"""
check_archetype_a_tariff_and_baseline.py  (v2, 3 Oct 2026)

Two checks on Archetype A's headline (FINDINGS.md Findings 7-8, repo
AndyMoran/thermal-counterfactual-gb): 7,600 kWh/yr displaced, £1,984/yr,
5.4-year payback, £60,706 net over 36 years.

Uses the repo's OWN physics functions and config unchanged; only the inputs
named below are varied. Run from the repo root:
    python <this file> /path/to/thermal-counterfactual-gb
"""
import sys, yaml
repo = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, f"{repo}/src")
from thermal_counterfactual_gb.physics import (
    EnvelopeState, heat_loss_coefficient_w_per_k, annual_heating_electrical_kwh)

cfg = yaml.safe_load(open(f"{repo}/configs/tenure_insulation_assumptions.yml"))
g, env = cfg["geometry"], cfg["envelope_states"]
months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
T = [cfg["annual_impact"]["monthly_mean_outdoor_temp_c"]["values_c"][m] for m in months]
GAINS = cfg["internal_gains_w"]["point"]
CAPEX, LIFE = 10_728, 36
FLOOR = g["floor_area_m2"]

def H(state, **over):
    s = dict(env[state]); s.update(over)
    st = EnvelopeState(s["wall_u_w_per_m2k"], s["roof_u_w_per_m2k"], s["floor_u_w_per_m2k"],
                       s["window_u_w_per_m2k"], s["infiltration_ach"])
    return heat_loss_coefficient_w_per_k(st, g["opaque_wall_area_m2"], g["roof_area_m2"],
                                         g["ground_floor_area_m2"], g["window_area_m2"], g["heated_volume_m3"])

def elec(h, setpoint=21, cop=2.5):
    return annual_heating_electrical_kwh(h, T, setpoint, cop, internal_gains_w=GAINS)

# ---------------------------------------------------------------- 1. TARIFF
print("=" * 78); print("1. TARIFF -- same 7,600 kWh displaced, priced different ways"); print("=" * 78)
base_e, epc_e = elec(H("baseline")), elec(H("epc_c_package"))
disp = base_e - epc_e
print(f"Reproduced: baseline {base_e:,.0f}  EPC-C {epc_e:,.0f}  displaced {disp:,.0f} kWh/yr\n")
# Rates: 26.11p = model's own (Ofgem cap Jul-Sep 2026); 26.32p = cap Oct-Dec 2026;
# 16.9p = storage-heater project's own blended heat-pump-tariff result
#   (£302 Cosy/E7 vs £470 ordinary at 26.32p -> 26.32*302/470);
# 14.53p = Cosy off-peak rate (logged Apr 2026), i.e. ALL heating in cheap windows.
rates = [("Standard rate, model's own (Jul-Sep 2026 cap)", 26.11),
         ("Standard rate, Oct-Dec 2026 cap", 26.32),
         ("Heat-pump tariff, blended (storage-heater project)", round(26.32*302/470, 1)),
         ("Cosy off-peak only (floor; all heat in cheap windows)", 14.53)]
for label, p in rates:
    s = disp * p / 100
    print(f"  {label:55s} {p:5.2f}p  £{s:6,.0f}/yr  payback {CAPEX/s:4.1f} yrs  net36 £{LIFE*s-CAPEX:7,.0f}")

# ---------------------------------------------------------------- 2. BASELINE SIZE
print("\n" + "=" * 78); print("2. BASELINE SIZE -- heat demand vs benchmarks"); print("=" * 78)
heat = base_e * 2.5
print(f"Baseline H = {H('baseline'):.0f} W/K; heat delivered = {heat:,.0f} kWh/yr "
      f"= {heat/FLOOR:.0f} kWh/m2/yr on {FLOOR} m2")
print("Benchmarks (see CHANGES_FROM_V1.md): NEED 2024 median gas ~105 kWh/m2 for 51-150 m2 houses,")
print("  ALL end uses incl. hot water, before boiler losses; SHDF case study solid-wall")
print("  mid-terrace pre-retrofit 95 kWh/m2/yr space heating.\n")

rows = [
  ("Model as published (21C 24/7, roof U 2.3, floor U 1.5, COP 2.5)", {}, {}),
  ("+ seasonal COP 2.78 (DESNZ EoH median) instead of cold-snap 2.5", {}, {"cop": 2.78}),
  ("+ whole-home mean 18C instead of 21C continuous", {}, {"setpoint": 18}),
  ("+ roof U 0.4 (some loft insulation) instead of 2.3", {"roof_u_w_per_m2k": 0.4}, {}),
  ("+ floor U 0.8 instead of 1.5", {"floor_u_w_per_m2k": 0.8}, {}),
]
print(f"  {'One change at a time':63s} {'heat kWh/m2':>11} {'displaced':>9} {'£@26.11p':>9} {'payback':>8}")
for label, over, kw in rows:
    cop = kw.get("cop", 2.5); sp = kw.get("setpoint", 21)
    hb = H("baseline", **over); he = H("epc_c_package")
    eb, ee = elec(hb, sp, cop), elec(he, sp, cop)
    d = eb - ee; s = d * 0.2611
    print(f"  {label:63s} {eb*cop/FLOOR:11.0f} {d:9,.0f} {s:9,.0f} {CAPEX/s:8.1f}")

# combined plausible case
hb = H("baseline", roof_u_w_per_m2k=0.4, floor_u_w_per_m2k=0.8)
he = H("epc_c_package")
for sp in (18, 19):
    eb, ee = elec(hb, sp, 2.78), elec(he, sp, 2.78)
    d = eb - ee
    print(f"\n  COMBINED: roof 0.4, floor 0.8, COP 2.78, mean {sp}C -> heat {eb*2.78/FLOOR:.0f} kWh/m2, "
          f"displaced {d:,.0f} kWh/yr")
    for label, p in rates[:1] + rates[2:3]:
        s = d * p / 100
        print(f"     at {p:5.2f}p: £{s:,.0f}/yr, payback {CAPEX/s:.1f} yrs, net36 £{LIFE*s-CAPEX:,.0f}")
