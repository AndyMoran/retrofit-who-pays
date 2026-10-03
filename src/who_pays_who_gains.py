"""
who_pays_who_gains.py  (v2, 3 Oct 2026)

Splits "payback" by party for both archetypes. In rented homes the landlord
pays for the fabric, and the tenant, who holds the energy account, gets the
bill savings. A single payback figure mixes those two up.

Archetype A inputs: check_archetype_a_loft.py, run against
AndyMoran/thermal-counterfactual-gb, with the baseline loft already at
~200mm (U 0.2) because loft top-ups are cheap and widespread (EHS 2023-24:
40% of homes with a loft at 200mm+). Range = "as published use" (21C 24/7,
COP 2.5) down to "plausible use" (19C mean, COP 2.78, floor U 0.8).
Archetype B inputs: archetype_b_storage_heated_flat.py.

Grant: Warm Homes: Social Housing Fund Wave 3 base cap, 50:50 match:
grant = min(£7,500, 50% of cost). This ASSUMES an allocation is held and the
measure qualifies, and it is the base cap only. Carbon for A uses the repo's
DESNZ 2026 average factor of 0.131 kg/kWh.
"""
LIFE = 36
A_CAPEX = 10_728
A_DISPLACED = {"plausible use": 2_643, "as published use": 4_616}   # kWh/yr, loft at 200mm
RATES = {"heat-pump tariff 16.9p": 0.169, "standard 26.11p": 0.2611}
B_CAPEX = (5_000, 7_000); B_SAVE = (337, 482)
B_CARBON_T = (0.237, 0.339)

def grant(c): return min(7_500, 0.5 * c)

print("ARCHETYPE A (pre-1919 terrace, loft already topped up)")
for use, d in A_DISPLACED.items():
    for rname, r in RATES.items():
        s = d * r; net = LIFE * s - A_CAPEX; t = d * 0.131 / 1000
        print(f"  {use:17} {rname:22} tenant saves £{s:5,.0f}/yr  "
              f"whole-package payback {A_CAPEX/s:4.1f}y  net36 £{net:7,.0f}  "
              f"carbon {t:.2f} t/yr  net £/t {-net/(t*LIFE):6,.0f}")
g = grant(A_CAPEX)
print(f"  Landlord outlay £{A_CAPEX:,} - Wave 3 grant £{g:,.0f} = net £{A_CAPEX-g:,.0f}")

print("\nARCHETYPE B (storage-heated flat)")
print(f"  tenant saves £{B_SAVE[0]}-{B_SAVE[1]}/yr")
for c in B_CAPEX:
    print(f"  Landlord outlay £{c:,} - grant £{grant(c):,.0f} = net £{c-grant(c):,.0f}")

# ---- Discounting (added 3 Oct): HM Treasury Green Book 3.5% and a 5% lender-style rate.
print("\nDISCOUNTED VALUE over 36 years (NPV = saving x annuity factor - cost)")
for rate in (0.035, 0.05):
    af = (1 - (1 + rate) ** -LIFE) / rate
    for name, cost, save in [("A low end", A_CAPEX, 447), ("A high end", A_CAPEX, 1_205),
                             ("B low end", B_CAPEX[1], B_SAVE[0]), ("B high end", B_CAPEX[0], B_SAVE[1]),
                             ("A low end, net of grant", A_CAPEX - grant(A_CAPEX), 447),
                             ("B low end, net of grant", B_CAPEX[1] - grant(B_CAPEX[1]), B_SAVE[0])]:
        print(f"  {rate:.1%}  {name:26} £{save*af-cost:8,.0f}")
