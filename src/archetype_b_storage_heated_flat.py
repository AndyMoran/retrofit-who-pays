"""
archetype_b_storage_heated_flat.py

v2 addition. The original business case modelled ONE archetype: a pre-1919
solid-wall mid-terrace (Archetype A). That is a fair proxy for the private
rented sector (31% pre-1919) and the wider stock (owner-occupied 20%), but
not for social housing, where only 7% of homes are pre-1919 and flats
dominate (EHS 2023-24, Chapter 1). The business case's own audience is
housing associations, so v2 adds a second archetype built from the
storage-heater project's modelled data (Archetype B):

    a storage-heated social-housing flat, using the real per-household
    heat demand and running costs of the 40 confirmed storage-heater
    households in the LCL 2013 smart-meter dataset.

Every input below is copied from the storage-heater project's own logged,
already-checked outputs -- nothing is re-derived or newly assumed, except
where flagged ASSUMPTION. Sources (all in github.com/AndyMoran/storage-heater):

  - Heat demand 4,721 kWh/yr (real 40-household mean):
        01_Evidence/evidence_map.md, 2026-09-08 "Route B executed"
  - Running costs at Ofgem cap Oct-Dec 2026 (26.32p elec, 7.97p gas):
        Outputs/nightdial_heatpump_article-1.md, "Carbon and cost don't agree"
        gas 418, storage unmanaged 964, storage optimised 719,
        heat pump (SPF 2.78) ordinary tariff 470, Cosy/E7 302
  - Carbon, demand-weighted 131.5 gCO2/kWh grid (corrected Route B):
        evidence_map.md 2026-09-08 "Route B correction #2"
        gas 958 kg, storage actual 678, storage managed 621, heat pump 223
  - Fabric demand reduction 35-50% for a multi-band (approx. EPC F->C) upgrade:
        evidence_map.md 2026-09-02 policy stress test (sourced range)
  - Mid-floor flat external wall insulation £5,000-7,000 (Checkatrade):
        evidence_map.md 2026-09-07 "Correction: predominantly solid wall"
  - 36-year fabric life: carried over unchanged from the original business
        case (FINDINGS.md Finding 8, sourced there) for like-for-like comparison.

Same simplifications as the original Finding 8, stated so nobody mistakes
this for more than it is: undiscounted, flat prices for the whole life,
single average household, fabric reduction applied proportionally to
running cost and carbon (insulation is fuel-agnostic).
"""

# ---- Inputs (all logged in the storage-heater project) ---------------------
HEAT_DEMAND_KWH = 4_721

COST = {  # GBP/yr, Ofgem cap Oct-Dec 2026
    "gas": 418,
    "storage_unmanaged": 964,
    "storage_optimised": 719,
    "hp_ordinary": 470,
    "hp_cosy_e7": 302,
}
CARBON_KG = {  # kgCO2/household/yr
    "gas": 958,
    "storage_unmanaged": 678,
    "storage_optimised": 621,
    "hp": 223,
}
FABRIC_CUT = (0.35, 0.50)          # share of heating demand removed
FABRIC_CAPEX = (5_000, 7_000)      # mid-floor flat EWI, GBP
FABRIC_LIFE_YEARS = 36

# Archetype A, for side-by-side only (original FINDINGS.md, not re-derived)
A = {"capex": 10_728, "saving": 1_984, "payback": 5.4, "net_life": 60_706,
     "carbon_t_avg": 1.0}


def fmt(x):
    return f"£{x:,.0f}"


if __name__ == "__main__":
    lo, hi = FABRIC_CUT
    base = COST["storage_unmanaged"]

    print("=" * 76)
    print("ARCHETYPE B -- storage-heated social flat (40 real LCL households)")
    print("=" * 76)
    print(f"Heat demand: {HEAT_DEMAND_KWH:,} kWh/yr   Prices: Ofgem cap Oct-Dec 2026")

    # 1. Fabric only, heater left as it is (unmanaged)
    s_lo, s_hi = base * lo, base * hi
    print("\n1. Fabric only (heater run as today, unmanaged)")
    print(f"   Bill saving: {fmt(s_lo)}-{fmt(s_hi)}/yr  (from {fmt(base)})")
    pb_best = FABRIC_CAPEX[0] / s_hi
    pb_worst = FABRIC_CAPEX[1] / s_lo
    print(f"   Payback on {fmt(FABRIC_CAPEX[0])}-{fmt(FABRIC_CAPEX[1])} EWI: "
          f"{pb_best:.1f}-{pb_worst:.1f} years")
    net_worst = FABRIC_LIFE_YEARS * s_lo - FABRIC_CAPEX[1]
    net_best = FABRIC_LIFE_YEARS * s_hi - FABRIC_CAPEX[0]
    print(f"   Net over {FABRIC_LIFE_YEARS} yrs (undiscounted): {fmt(net_worst)}-{fmt(net_best)}")
    c_lo = CARBON_KG["storage_unmanaged"] * lo
    c_hi = CARBON_KG["storage_unmanaged"] * hi
    print(f"   Carbon saved: {c_lo:.0f}-{c_hi:.0f} kg/yr  ({c_lo/1000:.2f}-{c_hi/1000:.2f} t)")
    # cost per tonne, same MACC treatment as original Finding 8
    life_t_lo = c_lo / 1000 * FABRIC_LIFE_YEARS
    life_t_hi = c_hi / 1000 * FABRIC_LIFE_YEARS
    macc_best = -net_best / life_t_hi
    macc_worst = -net_worst / life_t_lo
    print(f"   Net cost per tonne (lifetime, MACC treatment): "
          f"{macc_best:,.0f} to {macc_worst:,.0f} £/tCO2  (negative = cash-positive)")

    # 2. Fabric on an already-optimised (NightDial-style) home
    b2 = COST["storage_optimised"]
    print("\n2. Fabric only, heater already optimised")
    print(f"   Bill saving: {fmt(b2*lo)}-{fmt(b2*hi)}/yr  (from {fmt(b2)})")
    print(f"   Payback: {FABRIC_CAPEX[0]/(b2*hi):.1f}-{FABRIC_CAPEX[1]/(b2*lo):.1f} years")

    # 3. Heating-system swap, no fabric
    hp = COST["hp_cosy_e7"]
    print("\n3. Heat pump swap only, on a heat-pump tariff (no fabric)")
    print(f"   Bill saving: {fmt(base-hp)}/yr  ({fmt(base)} -> {fmt(hp)})")
    print(f"   On an ordinary tariff instead: {fmt(base-COST['hp_ordinary'])}/yr")
    print(f"   Carbon saved: {CARBON_KG['storage_unmanaged']-CARBON_KG['hp']} kg/yr")
    print("   Capex: NOT COSTED. Most storage-heated flats have no wet system, so")
    print("   air-to-water means a whole new system; BUS excludes social housing")
    print("   (both air-to-water £7,500 and air-to-air £2,500). No payback stated.")

    # 4. Fabric + heat pump
    print("\n4. Fabric + heat pump (Cosy/E7)")
    after = (hp * (1 - hi), hp * (1 - lo))
    print(f"   Running cost: {fmt(after[0])}-{fmt(after[1])}/yr  "
          f"-> saving {fmt(base-after[1])}-{fmt(base-after[0])}/yr vs today")

    # 5. Side by side with Archetype A
    print("\n" + "=" * 76)
    print("SIDE BY SIDE (fabric only)")
    print("=" * 76)
    print(f"{'':28}{'A: pre-1919 terrace':>22}{'B: storage-heated flat':>26}")
    print(f"{'Capex':28}{fmt(A['capex']):>22}{fmt(FABRIC_CAPEX[0])+'-'+fmt(FABRIC_CAPEX[1]):>26}")
    print(f"{'Bill saving /yr':28}{fmt(A['saving']):>22}{fmt(s_lo)+'-'+fmt(s_hi):>26}")
    print(f"{'Payback (yrs)':28}{A['payback']:>22}{f'{pb_best:.1f}-{pb_worst:.1f}':>26}")
    print(f"{'Net over 36 yrs':28}{fmt(A['net_life']):>22}{fmt(net_worst)+'-'+fmt(net_best):>26}")
    print(f"{'Carbon t/yr':28}{'~1.0 (avg grid)':>22}{f'{c_lo/1000:.2f}-{c_hi/1000:.2f}':>26}")
