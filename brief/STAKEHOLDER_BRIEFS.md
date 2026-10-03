# Practical Implications v2: What This Means for You

*v2, 3 October 2026. Supersedes STAKEHOLDER_BRIEFS.md (14 August). CHANGES_FROM_V1.md traces every change to its source.*

## The short version

The person who pays for insulation isn't the person who saves on the bills. In a rented home the landlord buys the fabric and the tenant, who holds the energy account, gets the lower bills. A single "payback" figure mixes those two up. So v2 answers two questions, for two typical homes:

1. **What does the tenant gain?** Lower bills from day one, a warmer home, and no upfront cost.
2. **What does the landlord protect?** Compliance, liability, and the condition and value of the asset. The landlord gets no bill savings at all.

And one sequencing rule before either: **top up the loft first.** It is cheap, already widespread (40% of homes with a loft have 200 mm or more, EHS 2023–24), and quick to pay back. v1's 5.4-year payback came mostly from a model that started with a bare loft. With the loft already done, the remaining fabric (walls, floor, windows) is a 9–24-year investment if judged on bills alone. That is why bills alone are the wrong yardstick for the landlord.

## The two homes

- **Archetype A, pre-1919 solid-wall mid-terrace.** v1's model (repo `AndyMoran/thermal-counterfactual-gb`, FINDINGS.md), rerun with the loft already at about 200 mm. Typical of private rented stock (31% pre-1919) and the wider stock (owner-occupied 20%), but not social housing (7%; EHS 2023–24).
- **Archetype B, storage-heated flat.** Built from the storage-heater project's 40 real London storage-heated households: 4,721 kWh/yr of heat, priced at the Oct–Dec 2026 Ofgem cap. Tenure isn't recorded in that data, so B stands in for housing association storage-heated stock; it is not a measured sample of it.

Both use simple undiscounted arithmetic at flat prices over a 36-year fabric life. Scripts are in `src/`: `who_pays_who_gains.py`, `check_archetype_a_loft.py` and `archetype_b_storage_heated_flat.py`.

| Fabric beyond the loft | A: pre-1919 terrace | B: storage-heated flat |
|---|---|---|
| Landlord's cost | £10,728 (EHS pre-1919 average to EPC C) | £5,000–7,000 (mid-floor flat external wall insulation) |
| Landlord's net cost after Wave 3 grant* | about £5,364 | about £2,500–3,500 |
| **Tenant's bill saving** | **£447–1,205/yr** | **£337–482/yr** |
| Simple payback on bills (whole cost) | 9–24 years | 10–21 years |
| Net over 36 years (bills only, undiscounted) | £5,350–32,650 | £5,150–12,350 |
| Carbon saved | 0.35–0.60 t/yr | 0.24–0.34 t/yr |
| Net cost per tonne over life | –£429 to –£1,500 | –£602 to –£1,012 |

*Wave 3 base cap is min(£7,500, 50% of cost). This assumes an allocation is held and the measures qualify.

A's range runs from realistic use on a heat-pump tariff (19°C average, field-trial heat pump efficiency of 2.78, typical floor loss, 16.9p per unit) to the model's original assumptions at the standard rate (21°C everywhere all day, 26.11p). The original assumptions are the generous end. Two caveats on A: its starting heat demand was still high compared with national consumption data after these adjustments, and it should ideally be calibrated against measured data.

Both homes come out ahead over their life, and both cut carbon at a net gain. Neither is a quick win on bills alone once the loft is done.

**Discounted, the low end turns negative.** At the Treasury's 3.5% discount rate the low end of each range is worth slightly less than it costs: about –£1,650 for A and –£150 for B. At 5% it is about –£3,300 and –£1,400. The high end stays positive, at +£3,000 to +£13,700. With the Wave 3 grant halving the landlord's outlay, every case is positive at both rates: +£2,000 to +£3,700 at the low end. So "pays for itself over its life" holds reliably only with the grant (`src/who_pays_who_gains.py`).

## Carbon at two levels

**Per home (the household's heating).** Beyond a topped-up loft:
- **Terrace (A):** insulation cuts heating carbon by about two-thirds, from 526–876 to 180–271 kg/yr, a saving of 0.35–0.60 t/yr. On a marginal-emissions basis the saving is 0.9–1.8 t/yr.
- **Storage-heated flat (B):** heating carbon falls by 35–50% from 678 kg/yr, a saving of 0.24–0.34 t/yr.

These count only the walls, floor and windows; the loft is assumed already done, so its saving is not included. They use the official average carbon content of grid electricity, about 0.13 kg CO2 per kWh (DESNZ 0.131 for A; the storage-heater project's demand-weighted 131.5 g/kWh for B). The marginal figure instead assumes each unit saved switches off a gas power station, roughly 3x higher. Both are defensible, and that is why both are reported. Over a 36-year fabric life that is about 12–22 t per terrace and 9–12 t per flat.

**Per fleet (the landlord's books).** No law makes a housing association reach net zero; the 2050 target binds government. But:
- Tenants' heating counts in the landlord's own indirect carbon total (Scope 3, downstream leased assets).
- The voluntary Sustainability Reporting Standard for Social Housing (130+ adopters and funders, comply-or-explain) asks about emissions and net-zero targets, so lenders see the fleet figure.

At fleet scale, insulation beyond the loft saves:
- **Per 1,000 homes:** 240–340 t/yr for storage-heated flats and 350–600 t/yr for terraces.
- **All housing association storage-heated homes in England** (182,000–187,000): roughly 43,000–63,000 t/yr.

Every tonne comes with a net gain over the fabric's life rather than a cost.

**One honest caveat for both levels.** These are electrically heated homes, so their carbon saving shrinks as the grid gets cleaner, while the bill and warmth savings don't. The 36-year totals assume today's grid all the way through, so they are upper bounds. For gas-heated homes being insulated, the carbon case wouldn't fade this way.

---

## For CEOs and portfolio leaders

**Stop asking one payback question.** Ask two:

- **Tenant side.** The tenant saves £340–1,200 a year from day one, with no outlay, plus warmth. For storage-heated flats, that sits alongside two cheaper or bigger levers:
  - running the existing heaters properly: £964 → £719 a year, the storage-heater project's own finding, so declare the interest
  - a heat pump on a heat-pump tariff: £964 → £302 a year, though its capital cost for flats with no radiators isn't costed
- **Landlord side.** The landlord's net outlay after grant is about £2,500–5,400 per home. Its return isn't bill savings but avoided cost and risk, set out under housing association leaders below. For a sense of scale, the average cost to bring a housing association home to EPC C is £6,082 (EHS 2024–25, Annex Table 2.14). One average dry-rot repair runs to about £4,600 (UK trade cost guides). Those are the same order of money as the net retrofit.

**Portfolio carbon.** See "Carbon at two levels" above: 240–600 t/yr per 1,000 homes, reportable progress on the fleet's Scope 3 total, at a net gain per tonne.

**Compliance changed in April 2026.** EPC C by 1 April 2030 on any *one* of three metrics: Fabric Performance, Smart Readiness or Heating System. A second metric follows by 1 April 2039, with a £10,000 spend exemption per metric (deferring to 2040). A's £10,728 sits above that cap; B's £5,000–7,000 sits below it. Decent Homes Criterion D (thermal comfort) applies from 2035.

*Caveat to carry into any board paper, unchanged from v1:* the link from EPC status to EUV-SH valuation is this project's own reasoned inference, not a sourced valuation method.

## For facilities and asset managers

**Sequence: loft first, then the rest.** The loft top-up is the quick, cheap part. Walls, floor and windows are the slow part, and the stock-condition and compliance case carries them.

**Batteries (Archetype A only).** A fully retrofitted A home needs 26% of a 10 kWh battery to cover the evening peak, against 98% unretrofitted, cutting peak demand by about 1.8 kW per home (Findings 1 and 6). Those figures start from v1's bare-loft baseline, so with the loft already done the gap is smaller. In B the storage heater is already an overnight heat store, so this finding doesn't transfer.

**Overheating is now a legal hazard.** From 30 November 2026, under Awaab's Law Phase 2, excess heat is a hazard alongside excess cold, on the same day. Insulation keeps summer heat in too (DESNZ July 2026; Welsh Government factsheet). Specify:

- external rather than internal wall insulation where possible (CIBSE TM59)
- shading for south-facing glazing
- night-time purge ventilation

These matter most in top-floor and south-facing flats.

**Solar at street scale** needs a DNO conversation about voltage limits (216–253 V) before it is phased in (Finding 7).

**Battery uptake gap (27% fabric vs 5.8% battery or solar).** This is the same split incentive as fabric, in reverse: battery revenue (about £1,075/yr) goes to whoever holds the electricity account (Finding 6). Confirm whether Wave 3 funds batteries against the application guidance; published statistics don't break measures out that far.

## For housing association leaders

**What the landlord actually gets back.** None of the bill saving. The landlord's return is:

- **Avoided liability.** From 30 Nov 2026, excess cold is an Awaab's Law hazard with statutory response clocks. Fabric is the measure that directly reduces it.
- **Avoided damp and mould repair.** Unaffordable heating leads to under-heating, which leads to damp. That chain is documented for UK social housing (Frontiers review; storage-heater evidence log). Prevalence is already high: surveyors record significant damp in 6% of HA homes, and 38% of HA tenants report condensation, damp or mould (EHS 2024–25). The sector spent over £7.8bn on damp, mould and stock-condition contracts in 2022–25 (Inside Housing procurement analysis). Typical repairs: replastering £450–800 a room, rising damp £500–2,500, dry rot averaging about £4,600 (trade cost guides). Fabric doesn't guarantee these are avoided. But a warmer, cheaper-to-heat home removes the main financial reason tenants under-heat.
- **Compliance.** One of the three 2030 metrics, and the most direct route to Criterion D (2035).
- **Asset value.** EUV-SH protection, which is an inference, not sourced (see above).
- **Fleet carbon.** A measurable cut in the fleet's reported Scope 3 emissions, which lenders increasingly ask about under the Sustainability Reporting Standard. That is not a legal net-zero duty. Any sustainability-linked loan benefit is possible upside, not costed here.
- **Not yet quantified:** tenancy sustainment. Lower bills plausibly reduce arrears and voids, but no figure is sourced here.

**So the landlord's real comparison** is about £2,500–5,400 net per home after grant against those avoided costs. It is not a payback in years. That is a risk and obligation case, and it is stronger than the bill-payback case suggests.

**Three ways to comply.** The government's Home Energy Model consultation (closed 18 Mar 2026) names these as Smart Readiness technologies:

- smart meters
- solar PV
- batteries
- thermal storage, including storage heaters
- smart heating controls and demand management

The thresholds are still due "later in 2026". v1 said a battery "doesn't touch" the EPC, which is now too strong. Fabric remains the only route that cuts heat demand.

**Deadlines:**

1. **30 Nov 2026:** Awaab's Law Phase 2 (excess cold and heat).
2. **31 Mar 2028:** Wave 3 grant must be spent.
3. **1 Apr 2030:** MEES first metric.
4. **2035:** Decent Homes Criterion D.
5. **1 Apr 2039:** MEES second metric.

**Funding.**

- **Boiler Upgrade Scheme:** not open to social housing providers, for any heat pump type (reconfirmed after April 2026). v1 was wrong on this.
- **Wave 3 (£1.29bn):** £7,500 base per home at 50:50 match, plus £7,500 for off-gas-grid low-carbon heating, or up to £20,000 for 10% of an application's on-gas homes.
- **A £4.4bn low-income scheme** follows after 2028, with no detail yet.

Wave 3's core scope is EPC D–G, so put fabric and heat pump in **one** application while the home still qualifies.

**Rule out flexibility income** as a fabric funding source: £127/home/yr would take about 84 years to repay (Finding 5).

---

## Combined battery + heat pump capex, re-checked (Archetype A only)

v1's result is unchanged: about 41% lower battery cost and about 29% lower heat pump cost, giving roughly 33% lower combined capex (range about 25–40%). It is now partly overstated, because it starts from the bare-loft baseline. The grant half is corrected: BUS gives housing association stock £0, and Wave 3 is the main route. For B there is no wet system to right-size. Air-to-air heat pumps suit room-by-room layouts and can also cool, but they are equally excluded from BUS, and their capex isn't costed. See `src/check_combined_capex_hypothesis.py`.

---

## What could still change this

**Could move the numbers**

- **Discounting.** See above. The undiscounted lifetime figures flatter the low end, and the grant is what makes the case robust.
- **Comfort-taking ("prebound").** Tenants who under-heat today will take part of the saving as warmth, not lower bills. A's "plausible use" case allows for some of this. Treat bill savings as an upper bound, and the warmth as the social return.
- **Future electricity prices.** Flat prices are assumed for 36 years. Moving levies off electricity (Warm Homes Plan) lowers the value of each kWh saved; price spikes raise it.

**Could change the advice**

- **Moisture risk in solid walls.** Badly specified or badly fitted wall insulation, internal wall insulation especially, can trap moisture and *cause* the damp this case says fabric prevents. The damp argument holds only for whole-house work to PAS 2035, with ventilation designed in. Ventilation and the retrofit coordination and assessment process aren't in the £10,728 or the £5,000–7,000.
- **External wall insulation may not be allowed.** Every figure assumes external rather than internal wall insulation.
  - *Conservation areas* often bar it on street-facing Victorian elevations.
  - *Taller blocks* face post-Grenfell combustibility rules for external wall systems.
  - *Mixed-tenure blocks* need leaseholder consent and cost recovery.

  Falling back to internal insulation means more disruption, lost floor space and the moisture risk above.
- **Storage heaters become oversized after insulation.** A heater sized for a leaky flat is even more oversized in an insulated one (storage-heater project, 2 Sep). Heater control becomes more valuable after fabric work, not less.

**Scope**

- **England only.** Scotland and Wales have their own social housing standards and deadlines.
- **Health benefits** of warmer homes (reduced NHS costs) are real but not costed here. A BRE estimate exists, but it hasn't been checked for this brief.
- **Embodied carbon** of insulation materials slightly reduces the net carbon saving. It is small against 36 years of savings, and not quantified here.

