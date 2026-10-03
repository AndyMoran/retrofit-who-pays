<!--
Corrected version of "The negawatt has no salesforce" (LinkedIn article, Aug 2026).
Same structure and argument as the original; numbers rerun with the baseline
loft already insulated (~200mm), a realistic heat-pump tariff and realistic use.
Ranges run from "plausible use, heat-pump tariff" to "as-published use,
standard rate". Sources: src/check_archetype_a_loft.py,
src/check_archetype_a_tariff_and_baseline.py, src/who_pays_who_gains.py,
src/check_peak_coastdown_loft.py, src/check_battery_headroom_loft.py.
Marginal carbon uses the original article's implied factor (0.35-0.40 kg/kWh).
See CHANGES_FROM_V1.md row 15.
-->

# The negawatt has no salesforce

*Updated October 2026. The first version of this article started from a home with a completely uninsulated loft. Most lofts already have insulation, so I've re-run every number. The negawatt is smaller than I first said, and the argument about who delivers it is stronger.*

We can now model it: roughly 2.6–4.6 GWh of displaced energy, £0.45–1.2m of bills, and 350–600 tonnes of CO2e per 1,000 homes a year. What we don't have is anyone whose job it is to sell it.

The negawatt, the unit of energy you never have to generate, transmit or pay for, is the oldest idea in energy policy and still the most under-delivered. I've spent recent months building a physics-based digital twin of a modelled, mixed-tenure English terrace estate, calibrated against national statistics, to find out whether the negawatt is real, what it's worth, and why so little of it exists. The short version: it's real, it pays for itself over its life, it's durable, and it has no salesforce.

## The negawatt, modelled

Take a pre-1919 solid-wall terrace whose loft is already insulated, as most are. Retrofitting the walls, floor and windows to EPC C displaces about 2,600–4,600 kWh of heat-pump electricity a year, depending on how warm the home is kept. That's worth about £450–1,200 a year to the household: the low end on a heat-pump tariff with realistic use, the high end at the standard rate. On the official average-grid basis it saves 0.35–0.60 tCO2e a year, or roughly 0.9–1.8 t on a marginal, CCGT-proxy basis. Which basis is "correct" for an abatement claim is genuinely contested, so this project reports both rather than picking a convenient one. At the coldest hour of a design winter, the same retrofit removes about 1.1 kW of peak demand per home: 1.1 MW per 1,000 homes, permanently, for as long as the fabric holds.

Per 1,000 homes that is 2.6–4.6 GWh a year, £0.45–1.2m a year, and 350–600 tCO2e a year on the average basis. No new generation, no new network, no land use, no new supply chain. And unlike a battery's roughly decade-scale replacement cycle, fabric's working life is measured in decades, not years.

## It pays for itself, slowly, and not to the person who pays

The retrofit costs £10,728 per home (English Housing Survey, pre-1919 average) and repays in about 9–24 years through bill savings alone. Compare the roughly 145 years it would take flexibility-market revenue to repay it, in a market that, as currently structured, can't buy what fabric delivers at all: passive retrofit has no meter, no dispatch signal and no verifiable baseline.

The bigger problem is who gets the money back. In a rented home the landlord pays and the tenant, who holds the energy account, keeps the saving. A 9–24-year payback to someone else is not an investment case any landlord can take to a board on bills alone. The landlord's real return is protection: against liability (from 30 November 2026, excess cold is an Awaab's Law hazard in social housing), against damp and mould repair, and against compliance deadlines.

Over the fabric's own working life (36 years, the Ofgem ECO/Green Deal standard measure life for solid wall insulation) the carbon arithmetic still lands well:

- **Gross cost, before counting bill savings:** about £490–860 a tonne on the average-grid basis, or £160–320 on the marginal-proxy basis.
- **Net cost, after bill savings** (the standard treatment in a marginal abatement cost curve): about –£430 to –£1,500 a tonne on the average basis, and –£140 to –£550 on the marginal basis. Negative means the measure saves money and cuts carbon at the same time.

That still puts it in the "no-regrets" category, but only just at the low end. Discount future savings the way a lender would, at 3.5–5%, and the least favourable cases are worth slightly less than they cost. With a Warm Homes grant covering half the outlay, every case comes out ahead. The economics are positive but thin, and the delivery model decides which side of the line a project lands.

## It multiplies everything else we have to build

Every negawatt shrinks the heat pump, the battery and the network upgrade that electrification otherwise requires. In the same model, a battery in a home with a topped-up loft but nothing else spends about 70% of its capacity just holding comfort through one evening peak. In a fully retrofitted one, it spends 26%. Insulation is not a competitor to electrification or storage. It is the multiplier that makes them affordable at system scale.

## But the negawatt has no salesforce

Megawatts have vendors, lenders and procurement routes. Negawatts have to be delivered by capital that only flows where someone controls the asset. On the modelled mixed-tenure estate, 27% of homes have the retrofit today and the other 73% don't. The missing share concentrates exactly where decades of Right to Buy sales have put it furthest out of reach of any landlord programme:

- A social landlord can't retrofit a street it no longer owns.
- A private landlord can't capture a tenant's bill savings.
- An owner-occupier in fuel poverty can't front £10,728.

The delivery-model evidence is already in the data. Fabric retrofit, delivered as landlord-funded programmes, has reached this stock at roughly 4.6x the rate of battery-plus-solar, which has been an individual purchase. Area-based, funded programmes out-deliver market-led uptake, and current programme routes stop at the social-landlord boundary.

## What would a negawatt delivery policy actually do?

1. **Make delivery tenure-blind.** Area-based schemes must be able to treat every home on a street regardless of ownership, the fragmented ex-Right-to-Buy share included. Streets drawn from the same tenure mix range from 17% to 37% insulated in the model, and real spatial clustering, where whole streets were sold under Right to Buy together, likely makes the true range wider still. Without tenure-blind delivery, patchwork outcomes are guaranteed.

2. **Close the split incentive where capital exists but can't capture the benefit.** Within this stock, the ex-Right-to-Buy privately rented segment is the lowest-insulation tier: 10% insulated, against 34–37% for retained council and housing association stock. The landlord pays, the tenant saves. With paybacks of 9–24 years to someone else, minimum standards, grant or shared-cost mechanisms have to bridge that, or the capital stays on the sidelines.

3. **Give the negawatt a buyer on the network side.** The 1.1 MW per 1,000 homes is real avoided reinforcement cost, but no route exists to pay for it. A reinforcement-avoidance funding mechanism, or a metering-and-verification layer that makes fabric-driven reduction contractible, would turn the negawatt from a free good into a procurable resource.

If you're designing Warm Homes delivery routes, PRS minimum standards or reinforcement-avoidance mechanisms, I'd like to compare notes.

## Honest scope and limitations

- **Single archetype:** a mid-terrace, the physically favourable solid-wall form. Other forms coast faster and cost more to treat.
- **Modelled, not measured:** the estate is calibrated against national statistics, not surveyed. Even with the loft corrected, the model's starting heat demand sits high against measured national consumption and should be calibrated against real meter data.
- **Carbon:** basis-dependent and reported as such. It also shrinks over time for electrically heated homes as the grid decarbonises.
- **Bill savings are an upper bound:** households who under-heat today will take some of the saving as warmth.
- **Delivery quality matters:** badly fitted solid-wall insulation can cause damp, so this assumes whole-house work to PAS 2035.
- **Economics:** simple undiscounted arithmetic at flat prices over a sourced 36-year fabric life, not a discounted-cash-flow appraisal.
- **Correction:** the first version of this article used a bare-loft baseline and the standard electricity rate. That overstated the saving, the payback and the peak reduction by roughly 1.6–3x.

None of that changes the central finding. Decarbonisation that pays for itself over its life is sitting undelivered, not because it isn't real, but because nobody's revenue depends on selling it.

Full model and corrections: github.com/AndyMoran/retrofit-who-pays
