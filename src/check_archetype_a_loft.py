"""
check_archetype_a_loft.py  (v2, 3 Oct 2026)

Archetype A's baseline assumes an UNINSULATED loft (roof U 2.3, PROVISIONAL in
the repo config). In reality most lofts have some insulation: EHS 2023-24 has
40% of homes with a loft at 200mm+, and topping up is cheap. The £10,728 capex
is the EHS 2024-25 modelled cost of taking the REAL pre-1919 stock to EPC C
(Annex Table 2.14), so it already reflects lofts as they actually are. Pairing
that cost with an uninsulated-loft baseline credits the package with loft
savings the real stock mostly already has.

This reruns the repo's own physics with the baseline loft already insulated.
Run:  python <this file> /path/to/thermal-counterfactual-gb
Roof U for a pitched roof, ~100mm mineral wool ~0.4, ~200mm ~0.2, 270mm ~0.16
(typical building-physics values, not taken from the repo).
"""
import sys, yaml
repo = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, f"{repo}/src")
from thermal_counterfactual_gb.physics import (
    EnvelopeState, heat_loss_coefficient_w_per_k, annual_heating_electrical_kwh)
cfg = yaml.safe_load(open(f"{repo}/configs/tenure_insulation_assumptions.yml"))
g, env = cfg["geometry"], cfg["envelope_states"]
m = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
T = [cfg["annual_impact"]["monthly_mean_outdoor_temp_c"]["values_c"][k] for k in m]
GAINS, CAPEX, LIFE, FLOOR = cfg["internal_gains_w"]["point"], 10_728, 36, g["floor_area_m2"]

def H(state, **o):
    s = dict(env[state]); s.update(o)
    return heat_loss_coefficient_w_per_k(
        EnvelopeState(s["wall_u_w_per_m2k"], s["roof_u_w_per_m2k"], s["floor_u_w_per_m2k"],
                      s["window_u_w_per_m2k"], s["infiltration_ach"]),
        g["opaque_wall_area_m2"], g["roof_area_m2"], g["ground_floor_area_m2"],
        g["window_area_m2"], g["heated_volume_m3"])

cases = {
  "As published (21C 24/7, COP 2.5, floor U 1.5)": dict(sp=21, cop=2.5, floor=None),
  "Plausible use (19C mean, COP 2.78, floor U 0.8)": dict(sp=19, cop=2.78, floor=0.8),
}
lofts = [("none (U 2.3, as published)", 2.3), ("~100mm (U 0.4)", 0.4), ("~200mm (U 0.2)", 0.2)]
for cname, c in cases.items():
    print("=" * 96); print(cname); print("=" * 96)
    print(f"  {'Baseline loft':28}{'heat kWh/m2':>12}{'displaced kWh':>14}"
          f"{'£ @26.11p':>11}{'payback':>9}{'£ @16.9p':>10}{'payback':>9}{'net36 @16.9p':>14}")
    for lname, u in lofts:
        over = {"roof_u_w_per_m2k": u}
        if c["floor"]: over["floor_u_w_per_m2k"] = c["floor"]
        hb, he = H("baseline", **over), H("epc_c_package")
        eb = annual_heating_electrical_kwh(hb, T, c["sp"], c["cop"], internal_gains_w=GAINS)
        ee = annual_heating_electrical_kwh(he, T, c["sp"], c["cop"], internal_gains_w=GAINS)
        d = eb - ee; s1, s2 = d*0.2611, d*0.169
        print(f"  {lname:28}{eb*c['cop']/FLOOR:12.0f}{d:14,.0f}{s1:11,.0f}{CAPEX/s1:9.1f}"
              f"{s2:10,.0f}{CAPEX/s2:9.1f}{LIFE*s2-CAPEX:14,.0f}")
    print()
