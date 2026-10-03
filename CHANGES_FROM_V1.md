# Changes from v1

*3 October 2026. v1 stays where it was published, in [`thermal-counterfactual-gb/comms/insulation_business_case`](https://github.com/AndyMoran/thermal-counterfactual-gb/tree/main/comms/insulation_business_case), as the record of what went out. This file logs every change and its source.*

## Why there is a v2

v1 (14–17 August 2026) was built on one home: a pre-1919 solid-wall mid-terrace. It was written for housing association leaders, CEOs and facilities teams. In September, the storage-heater project ([AndyMoran/storage-heater](https://github.com/AndyMoran/storage-heater)) checked several of the same policy facts more carefully against primary sources, and modelled real storage-heated homes. v2 brings the business case into line with that later work.

## Is the Victorian terrace typical?

It depends on whose housing you mean (English Housing Survey 2023–24, Chapter 1):

| Tenure | Built before 1919 |
|---|---|
| Private rented | 31% |
| Owner occupied | 20% |
| Social rented | 7% |

The terrace is a fair stand-in for the private rented sector and much of the wider stock. It is not typical of the stock housing associations own. In social housing, 37% of homes are low-rise purpose-built flats and more are high-rise, and the average home is 66 m² against 110 m² for owner-occupied. Storage heaters also cluster in flats: many councils took gas out of tower blocks after Ronan Point in 1968 (storage-heater evidence_map, 7 Sep 2026).

So v2 reports **two archetypes** side by side instead of one:

- **Archetype A, pre-1919 solid-wall mid-terrace.** The v1 model is unchanged and is labelled as typical of private rented and wider stock.
- **Archetype B, storage-heated flat.** Built from the storage-heater project's 40 real London storage-heated households (LCL 2013 usage, 2026 prices). The dataset does not record tenure, so B stands in for housing association storage-heated stock; it is not a measured sample of it.

## What changed

| # | v1 said | v2 says | Why (source in [storage-heater/01_Evidence/evidence_map.md](https://github.com/AndyMoran/storage-heater/blob/main/01_Evidence/evidence_map.md)) |
|---|---|---|---|
| 1 | The Boiler Upgrade Scheme's flat £7,500 covers "close to the entire cost" of a right-sized heat pump | BUS is **not open to social housing providers**. That covers both the £7,500 air-to-water grant and the new £2,500 air-to-air grant. For housing associations the heat pump route runs through the Warm Homes: Social Housing Fund | Reconfirmed after the 28 April 2026 BUS refresh (entries of 7 Sep and 10 Sep) |
| 2 | Fabric is "what moves the EPC band"; a battery "isn't a scored EPC input" | The April 2026 final MEES policy lets landlords meet EPC C by 2030 on **any one of three metrics**: Fabric Performance, Smart Readiness or Heating System. The HEM consultation names batteries, storage heaters and smart heating controls as Smart Readiness technologies, but the thresholds are still unpublished | 7 Sep: "Insulation stress-test assumption corrected" and "Missing citation caught" |
| 3 | The £10,000 cap is a "known ceiling on required capital" | Still true, and a £10,000 exemption applies per metric (deferring to 2040). A further point: A's own £10,728 fabric cost is above the cap, and fabric is no longer required at all if another metric is met | 7 Sep entry |
| 4 | No Awaab's Law | Phase 2 on **30 November 2026** makes excess cold *and* excess heat legal hazards on the same day | 10 Sep fact-check |
| 5 | Bundle the heat pump with the fabric in one Wave 3 application | Kept. Added: Wave 3 grant must be **spent by 31 March 2028** (delivery window to September 2028) | 10 Sep fact-check |
| 6 | Heat pump capex £7,500–10,500 (installer surveys) | Kept for A, which has a wet system. For B it is **not costed**: storage-heated flats usually have no radiators or pipework, so air-to-water means a whole new system | 2 Sep and 7 Sep entries |
| 7 | External wall insulation "plausibly" better for summer comfort, unquantified | Promoted to a design requirement, because insulation holds summer heat in and excess heat becomes a legal hazard on 30 Nov 2026 | linkedin_post_insulation_overheating.md; Awaab Phase 2 |
| 8 | Battery 98% → 26%, and 1.8 MW per 1,000 homes | Kept, but marked as **Archetype A only**. In B the storage heater is already a thermal store that charges overnight, so the battery finding does not transfer | Scope |
| 9 | One archetype | Two archetypes, A and B | EHS 2023–24 |
| 10 | A pays back in 5.4 years and nets £60,706 | With the loft already topped up (cheap and widespread), the remaining fabric pays back in 9–24 years on bills and nets £5,350–32,650 over 36 years. Carbon falls to 0.35–0.60 t/yr | `src/check_archetype_a_loft.py`, `src/check_archetype_a_tariff_and_baseline.py` |
| 11 | One payback figure | Split by party. The tenant gets the bill saving (£340–1,200/yr) with no outlay. The landlord pays about £2,500–5,400 net after the Wave 3 grant and gets its return as protection against liability, damp repair and compliance risk, not as bills | `src/who_pays_who_gains.py`; landlord-side figures from storage-heater evidence_map 7 Sep 2026 (EHS 2024–25 damp, Inside Housing £7.8bn, trade repair-cost guides) |
| 12 | Undiscounted lifetime value only; no delivery risks | Discounted at 3.5% and 5%: the low end of each range turns negative, every case is positive after the Wave 3 grant. New "What could still change this" section: comfort-taking, prices, moisture risk and PAS 2035, limits on external wall insulation (conservation areas, fire rules, leaseholders), heater oversizing, England-only scope, health, embodied carbon | `src/who_pays_who_gains.py` (discounting block) |
| 13 | Battery headroom (published post): unretrofitted home uses 98% of a 10 kWh battery; flexibility payback ~59 / ~37 / ~16 years, a ~3.8x spread | With the loft already insulated, the unretrofitted home uses ~70%, earns ~£472/yr and pays back in ~29 years (wall insulation only ~22, EPC C ~16, unchanged). The spread is ~1.8x. Direction holds; size about halves | `src/check_battery_headroom_loft.py` |

Unchanged: MEES dates (2030 and 2039), the Decent Homes Criterion D date (2035), £1.29bn for Wave 3, Wave 3 core scope of EPC D–G, the per-property caps, the 36-year fabric life, and the flexibility-revenue warning (£127/yr, about 84 years).

## Still open

- **Archetype A checked, 3 Oct.** `FINDINGS.md` lives in the public repo `AndyMoran/thermal-counterfactual-gb`. Its £1,984/yr is heat-pump electricity at COP 2.5: annual heating electricity falls from 9,671 to 2,071 kWh, so 7,600 kWh is displaced. The figure reproduces exactly with the repo's own code. `src/check_archetype_a_tariff_and_baseline.py` varies one input at a time, using the repo's own physics:
  - **Tariff.** On a heat-pump tariff the saving falls to £1,104–1,284/yr. That is a payback of 8.4–9.7 years and £29,000–35,500 net over 36 years, against 5.4 years and £60,706 at the 26.11p standard rate. The 16.9p blended rate is the storage-heater project's own Cosy/E7 result. The 14.53p floor assumes every unit falls in Cosy's cheap windows.
  - **Baseline size.** The model's unretrofitted home needs 24,178 kWh/yr of heat, which is **345 kWh/m²/yr** on 70 m². For comparison, NEED 2024's median *gas* use for 51–150 m² houses is about 105 kWh/m², covering all uses including hot water and before boiler losses. A SHDF case study gives 95 kWh/m²/yr for a solid-wall mid-terrace before retrofit. Old homes sit above the median, but 345 is roughly 2–4 times what measured data suggests. Four inputs drive it:
    - 21°C held in every room, 24 hours a day
    - roof U 2.3, meaning no loft insulation at all
    - floor U 1.5
    - the cold-snap COP of 2.5 applied all year instead of the field-trial seasonal 2.78
  - **Combined plausible case.** With loft U 0.4, floor U 0.8, COP 2.78 and an 18–19°C whole-home mean, displacement falls to 2,490–2,854 kWh/yr. That is about £650–745/yr at the standard rate (14–17-year payback), or £421–482/yr on a heat-pump tariff (22–26 years). This overstates the payback somewhat, because a home that already has loft insulation would also cost less than £10,728 to bring to EPC-C, and that capex hasn't been re-estimated.
  - **Loft (`src/check_archetype_a_loft.py`).** The baseline assumes no loft insulation at all, but most lofts have some: EHS 2023–24 found 40% of homes with a loft at 200 mm or more. The £10,728 cost is the EHS modelled cost for the *real* pre-1919 stock, lofts as they are. So the model pairs real-stock costs with an uninsulated-loft baseline. Insulating the loft alone accounts for about 2,700 of the 7,600 kWh/yr displaced. With the loft already at 100–200 mm and other inputs as published, displacement is 4,600–4,900 kWh/yr, giving an 8.4–8.9-year payback at the standard rate or 13–14 years on a heat-pump tariff. With plausible use as well (19°C mean, COP 2.78, floor U 0.8), it is 2,640–2,850 kWh/yr, giving 14–16 years at the standard rate or 22–24 years on a heat-pump tariff. The cheap loft top-up is where the quick payback really comes from; walls, floor and windows are the slow part.
  - **Bottom line:** the terrace retrofit is probably still cash-positive over 36 years in most cases, but 5.4 years is a best case. A credible range is roughly 8–25 years depending on tariff and on how leaky and how warm the real home is. Treat £1,984 and £60,706 as upper bounds until the baseline is calibrated against measured data, for example NEED by age band or the estate's own meter data.
- Price: v1 used 26.11p/kWh, and the Oct–Dec 2026 cap is 26.32p. At the new price A's saving becomes about £2,000/yr and the payback still rounds to 5.4 years. No change has been made.
- Archetype B uses a sourced 35–50% demand cut for a multi-band (roughly F→C) upgrade. A flat-specific figure would be better.

## Files

- `brief/STAKEHOLDER_BRIEFS.md` — the internal three-audience brief, both archetypes
- `comms/article_who_pays.md` — the public article, rewritten
- `comms/article_vpp_funding_ladder.md` — scope and EPC wording fixed; otherwise as v1
- `comms/posts/post_1_ceo.md`, `comms/posts/post_2_facilities.md`, `comms/posts/post_3_ha_leader.md`
- `comms/posts/post_0_correction_bus_grant.md` — short public correction for the published grant claim
- `src/archetype_b_storage_heated_flat.py` — Archetype B numbers, inputs traced line by line
- `src/check_combined_capex_hypothesis.py` — the v1 check with the BUS eligibility fix
- `src/check_archetype_a_tariff_and_baseline.py` — the tariff and baseline-size checks on Archetype A (run against the repo)
- `src/check_archetype_a_loft.py` — Archetype A rerun with the loft already insulated
- `src/check_battery_headroom_loft.py` — battery headroom and flexibility payback, rerun with the loft already insulated
- `src/who_pays_who_gains.py` — tenant vs landlord split for both archetypes (the numbers the brief and article use)
