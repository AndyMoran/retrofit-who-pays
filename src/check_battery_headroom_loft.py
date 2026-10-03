"""
check_battery_headroom_loft.py  (3 Oct 2026)

Re-runs the battery-headroom / VPP-revenue figures from
thermal-counterfactual-gb (Finding 6 and
comms/insulation_business_case/src/check_headroom_revenue_scaling.py) with the
baseline loft ALREADY insulated (~200mm, roof U 0.2). Everything else is
unchanged, as published: design -3C, 21C setpoint, COP 2.5, 400W gains, a 4h
evening peak, a 10kWh battery, and £13,500 battery+solar capex.

Revenue split, also unchanged from the repo: £210/yr dispatch (unscaled) plus
£875/yr arbitrage scaled by spare battery capacity. That scaling is PROVISIONAL
in the source repo: reasoned, not simulated against real dispatch data.
Payback counts flexibility income only; solar bill savings are excluded, as in
the original post.

Run:  python src/check_battery_headroom_loft.py /path/to/thermal-counterfactual-gb
"""
import sys, yaml
repo = sys.argv[1] if len(sys.argv) > 1 else "."
sys.path.insert(0, f"{repo}/src")
from thermal_counterfactual_gb.physics import EnvelopeState, heat_loss_coefficient_w_per_k

cfg = yaml.safe_load(open(f"{repo}/configs/tenure_insulation_assumptions.yml"))
g, env = cfg["geometry"], cfg["envelope_states"]
DESIGN_C, SETPOINT_C, COP, GAINS_W = -3, 21, 2.5, 400
PEAK_H, BATT_KWH, CAPEX = 4, 10, 13_500
DISPATCH, ARBITRAGE = 210, 875

def H(state, **o):
    s = dict(env[state]); s.update(o)
    return heat_loss_coefficient_w_per_k(
        EnvelopeState(s["wall_u_w_per_m2k"], s["roof_u_w_per_m2k"], s["floor_u_w_per_m2k"],
                      s["window_u_w_per_m2k"], s["infiltration_ach"]),
        g["opaque_wall_area_m2"], g["roof_area_m2"], g["ground_floor_area_m2"],
        g["window_area_m2"], g["heated_volume_m3"])

results = {}
for label, loft in [("As published (bare loft, roof U 2.3)", None), ("Loft already at ~200mm (roof U 0.2)", 0.2)]:
    print(label)
    for st in ["baseline", "swi_only", "epc_c_package"]:
        o = {} if (loft is None or st == "epc_c_package") else {"roof_u_w_per_m2k": loft}
        kw = max(H(st, **o) * (SETPOINT_C - DESIGN_C) - GAINS_W, 0) / COP / 1000
        used = min(kw * PEAK_H / BATT_KWH, 1.0)
        rev = DISPATCH + ARBITRAGE * (1 - used)
        results[(label, st)] = CAPEX / rev
        print(f"  {st:14} peak {kw:.2f} kW  battery used {used:4.0%}  "
              f"flex income £{rev:4.0f}/yr  payback {CAPEX/rev:4.1f} yrs")
    a = results[(label, "baseline")] / results[(label, "epc_c_package")]
    print(f"  spread unretrofitted vs EPC-C: {a:.1f}x\n")
