# Retrofit: who pays, who gains?

A business case for insulating rented homes, written for housing association leaders, asset managers and boards. It splits the usual single "payback" figure into what the **tenant** gains and what the **landlord** protects.

This replaces an August 2026 version that headlined a 5.4-year payback. That figure didn't survive checking. [`CHANGES_FROM_V1.md`](CHANGES_FROM_V1.md) logs every correction and its source.

## The short version

In a rented home the landlord pays for the insulation, and the tenant, who pays the energy bills, keeps the savings. One payback figure divides one person's cost by another person's saving, so nobody actually experiences it.

1. **Top up the loft first.** It's cheap, widespread (40% of homes with a loft already have 200 mm+, English Housing Survey 2023–24) and quick to pay back.
2. **Then walls, floor and windows.** Judged on bills alone, these pay back over 9–24 years. That's the wrong yardstick for the landlord, who gets no bill saving at all.
3. **The tenant gains** lower bills from day one, with no outlay, and a warmer home.
4. **The landlord gains protection:** from liability (excess cold and heat become Awaab's Law hazards on 30 November 2026), from damp and mould repair, against compliance deadlines (EPC C by 2030, Decent Homes 2035), and in reported fleet carbon.

## Two homes

| Insulation beyond a topped-up loft | Victorian terrace | Storage-heated flat |
|---|---|---|
| Tenant saves | £450–1,200 a year | £340–480 a year |
| Landlord pays, after Warm Homes grant* | about £5,400 | about £2,500–3,500 |
| Carbon saved per home | 0.35–0.60 t a year | 0.24–0.34 t a year |
| Carbon saved per 1,000 homes | 350–600 t a year | 240–340 t a year |

\*Warm Homes: Social Housing Fund Wave 3 base cap, 50:50 match; this assumes an allocation is held and the measures qualify.

- **The terrace** is typical of private rented and older owner-occupied stock: 31% of private rented homes were built before 1919, against 7% of social rented ones. Its numbers come from the physics model in [AndyMoran/thermal-counterfactual-gb](https://github.com/AndyMoran/thermal-counterfactual-gb), rerun with the loft already insulated and realistic use.
- **The flat** is closer to housing association stock. Its numbers come from 40 real London storage-heated households in [AndyMoran/storage-heater](https://github.com/AndyMoran/storage-heater).

Both come out ahead over a 36-year insulation life before discounting. At a 3.5–5% discount rate the least favourable cases are worth slightly less than they cost, and every case comes out ahead once the grant halves the landlord's outlay.

## What's here

| Path | What it is |
|---|---|
| [`brief/STAKEHOLDER_BRIEFS.md`](brief/STAKEHOLDER_BRIEFS.md) | The full brief for CEOs, asset managers and housing association leaders, with caveats |
| [`comms/article_who_pays.md`](comms/article_who_pays.md) | Public article |
| [`comms/article_vpp_funding_ladder.md`](comms/article_vpp_funding_ladder.md) | Follow-up on who funds batteries (terrace only) |
| [`comms/posts/`](comms/posts/) | Correction post and three short posts |
| [`src/`](src/) | Every number above, reproducible |
| [`CHANGES_FROM_V1.md`](CHANGES_FROM_V1.md) | What changed from August, and why |

## Reproducing the numbers

```bash
git clone https://github.com/AndyMoran/thermal-counterfactual-gb
pip install pyyaml

# Terrace: run against the physics model, unchanged
python src/check_archetype_a_tariff_and_baseline.py thermal-counterfactual-gb
python src/check_archetype_a_loft.py thermal-counterfactual-gb
python src/check_battery_headroom_loft.py thermal-counterfactual-gb
python src/check_peak_coastdown_loft.py thermal-counterfactual-gb

# Flat, the tenant/landlord split, discounting, and the capex re-check
python src/archetype_b_storage_heated_flat.py
python src/who_pays_who_gains.py
python src/check_combined_capex_hypothesis.py
```

The flat's inputs are a handful of figures written into its script, each traced to a dated entry in the storage-heater project's [evidence map](https://github.com/AndyMoran/storage-heater/blob/main/01_Evidence/evidence_map.md).

## Limits, stated up front

- Two homes, not a portfolio.
- The terrace's starting heat demand still sits high against national consumption data and should be calibrated against real meters.
- Bill savings are an upper bound, because tenants who under-heat take some of the saving as warmth.
- Electrically heated homes' carbon savings shrink as the grid decarbonises.
- Badly fitted wall insulation can cause damp, so the damp argument holds only for whole-house work to PAS 2035.
- External wall insulation may be barred by conservation areas, fire rules or leaseholders.
- England only.

The full list is in the brief, under "What could still change this".

## Licence

MIT. See [LICENSE](LICENSE).
