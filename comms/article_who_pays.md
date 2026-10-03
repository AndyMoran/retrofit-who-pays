<!--
Posting notes (v2, 3 Oct 2026):
- Replaces linkedin_article_business_case.md (v1, Aug 2026), which has already
  been published. Post as a NEW article; add one line to the top of v1 pointing here.
- Every figure traces to v2/src: who_pays_who_gains.py, check_archetype_a_loft.py,
  check_archetype_a_tariff_and_baseline.py (all run against the repo
  AndyMoran/thermal-counterfactual-gb) and archetype_b_storage_heated_flat.py.
  CHANGES_FROM_V1.md logs every change from v1.
- Suggested figure (not yet built): one chart, two homes, two bars each --
  "tenant saves per year" and "landlord's net outlay after grant".
-->

# Who does a retrofit actually pay back?

*In August I published a business case for insulating old homes: a 5.4-year payback and £60,000 saved over the insulation's life. I've since checked it properly. The case survives, but that headline doesn't, and I think the bigger mistake was asking "how long is the payback?" at all.*

## Three things I got wrong

**I started from a bare loft.** My model's unretrofitted Victorian terrace had no loft insulation whatsoever. Real homes almost all have some. 40% of homes with a loft already have 200 mm or more (English Housing Survey 2023–24), and topping up the rest is cheap. Over a third of my headline saving was the loft, a quick win most homes have already had. Yet my cost figure was the price of upgrading real homes, lofts as they actually are.

**I priced the heat pump's electricity at the standard rate.** A heat pump on a heat-pump tariff pays a lot less per unit. Good for the household, but it shrinks the saving per unit of energy avoided.

**I showed a terrace to people who mostly own flats.** Only 7% of social rented homes were built before 1919, against 31% of private rented ones. So I've added a second home: a storage-heated flat, built from 40 real London households I've spent two months analysing.

(And a straight correction: the Boiler Upgrade Scheme's heat pump grant is not open to social housing providers. I implied it was.)

## The question underneath: payback for whom?

In a rented home, the person who pays for insulation isn't the person who saves on the bills. The landlord buys the fabric. The tenant holds the energy account and gets every penny of the saving. Dividing one person's cost by another person's saving gives you a number, but nobody experiences that number.

So here are the two sides separately, for insulation beyond a topped-up loft:

| | Victorian terrace | Storage-heated flat |
|---|---|---|
| **Tenant** saves | £450–1,200 a year | £340–480 a year |
| **Landlord** pays, after Warm Homes grant | about £5,400 | about £2,500–3,500 |
| Carbon saved | 0.35–0.60 t a year | 0.24–0.34 t a year |

For anyone who still wants it, the combined figure is a payback of 9 to 24 years for the terrace and 10 to 21 for the flat. It is still positive over a 36-year life, and every tonne of carbon saved comes with a net gain, not a cost.

## What the tenant gets

Lower bills from the first winter, with no upfront cost, and a warmer home. That matters more than it sounds. In my storage-heater data, more than half a year's heating cost lands in four winter months. Research on prepayment households shows people cut back hardest exactly when it's coldest. Some of the "saving" will be taken as warmth rather than money, which is the point.

## What the landlord gets

None of the bill saving. What the landlord gets is protection:

- **Liability.** From 30 November 2026, Awaab's Law makes excess cold a hazard with a statutory response clock, and excess heat too, on the same day.
- **Damp and mould.** Unaffordable heat leads to under-heating, which leads to damp. In housing association homes surveyors record significant damp in 6% of cases, and 38% of tenants report condensation, damp or mould. The sector spent over £7.8bn on damp, mould and stock-condition work in three years. A single average dry-rot repair is about £4,600, which is comparable to the landlord's whole net cost of retrofitting a terrace after grant.
- **Compliance.** EPC C by 2030 on one of three routes. Insulation is the only one that actually reduces heat demand, which makes it the most direct answer to the Decent Homes thermal-comfort standard in 2035.
- **The asset itself.** Protecting what the building is worth. This is my own inference, not a sourced valuation method.

The landlord's case is a risk-and-obligation case, not a payback case. Measured that way it is stronger than the bill arithmetic suggests. But it doesn't fit neatly into a payback table, which may be one reason retrofit keeps getting filed under cost.

## So what should happen first?

1. **Top up the loft.** It is cheap, quick, and most of the easy money.
2. **Then the walls, floor and windows**, justified on liability, damp and compliance, with the tenant's bill saving as the social return. Do it properly: badly fitted wall insulation on solid Victorian walls can trap moisture and cause the very damp it's meant to prevent. That means whole-house work to PAS 2035, with ventilation designed in. And check early whether external insulation is allowed at all: conservation areas, fire rules on taller blocks and leaseholder consent can all rule it out. Spec it for summer as well as winter: external rather than internal wall insulation, shading, and night-time ventilation, because overheating becomes a legal hazard on the same day as cold.
3. **Fund it while you can.** Warm Homes: Social Housing Fund Wave 3 money must be spent by 31 March 2028. Its core scope is homes rated D to G, so put insulation and any heat pump in one application before the rating moves.

For storage-heated flats specifically, insulation isn't even the biggest lever for the tenant. Running the existing heaters properly takes a £964 annual bill to £719. A heat pump on the right tariff takes it to £302, but the capital cost in flats with no radiators is a real and unsolved problem. That's the subject of my other project, so weigh that comment accordingly.

## Scope, honestly

These are two homes, not a portfolio. Even after the corrections, the terrace's starting heat demand sits high against national consumption data, and it should be calibrated against real meter data. The flat's insulation effect is a sourced range, not a measurement. Both use simple arithmetic at flat prices. Discount future savings the way a lender would, at 3.5–5%, and the least favourable cases are worth slightly less than they cost. With the Warm Homes grant halving the landlord's outlay, every case comes out ahead. The grant figures assume an allocation and qualifying measures. Some of the bill saving will be taken as warmth rather than money, which is the point. This is England only.

The August version had a cleaner headline. This one answers the question the people paying for it actually ask.

Full model, both homes, every source: link in the comments.
