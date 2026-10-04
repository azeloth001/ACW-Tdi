# ACW ∞ + TDI ∞ — G Generation Design Specification

**Date:** 2026-10-03  
**Generation:** G  
**Baseline:** `ACW 1f3` + `TDI 1f3`  
**Target:** first G production pair  
**Status:** Approved — implementation planned

---

## 1. Purpose

G is the production-calibration generation for the ACW ∞ + TDI ∞ pair.

F already established the intended architecture: ACW owns price structure and final market interpretation, TDI owns timing/momentum/flow evidence, and Near/Anchor context qualifies rather than erases local truth. F1.3 also established the risk hierarchy for exhaustion and divergence.

G does **not** reopen that architecture. It finishes the system by adding four things:

1. A selectable **Signal Personality** controlling how hard it is for a qualified opportunity to reach `READY`.
2. A chart-visible **Signal Lifecycle** so the user can see when an actionable state began, how old it is, when it weakened, and when the original thesis stopped being trusted.
3. Final calibration of the existing promotion/risk layer across BTC, GOLD and HYPE without curve-fitting to one chart.
4. Final human-language and mobile presentation polish, followed by a production freeze.

The core principle for G is:

> **F defined intelligence. G defines discipline, timing, lifecycle and presentation.**

---

## 2. User Outcome

The user should be able to open a chart after being away and answer, within a few seconds:

- Is the current market state bullish, bearish, mixed, compressed, exhausted or conflicted?
- Is there a valid actionable opportunity now, or only a developing one?
- If an actionable opportunity already happened, **which candle started it and how many bars ago was it?**
- Has the original opportunity merely weakened, reached an exit-quality deterioration state, or become structurally invalid?
- Is the current signal personality Selective, Balanced or Active?

G must improve this practical readability without turning ACW/TDI into a full automated trading strategy, fixed TP/SL engine, or ROM-style support/resistance system.

---

## 3. System Roles — Frozen from F

### 3.1 ACW remains the final interpreter

ACW owns:

- MAMA/FAMA context.
- MACD council context.
- confirmed swing structure and freshness.
- MA Core direction and phase.
- ACW Fusion and confluence interpretation.
- final `READY / WATCH / WAIT` promotion.
- final lifecycle state and price-chart lifecycle markers.

### 3.2 TDI remains timing and risk evidence

TDI owns:

- Trend Carrier / Price Core.
- Momentum Fusion and momentum phase.
- OBV Flow when volume is available.
- squeeze/chop/expansion/exhaustion regime.
- Near and Anchor context.
- divergence detection and freshness lifecycle.
- timing/continuation evidence transported through the existing bridge.

### 3.3 The bridge remains one-way TDI → ACW

The existing packed bridge interface is frozen for G unless implementation proves a hard technical impossibility.

Signal Personality and Signal Lifecycle must be implemented **without changing the meaning or packing format of the F1.3 bridge**.

This avoids profile mismatch and protects compatibility.

---

## 4. G Non-Goals

G will not:

- add support/resistance, Fibonacci, ROM geometry or proximity-to-level logic.
- add fixed take-profit targets.
- add an arbitrary fixed-price stop-loss engine.
- add automatic order execution.
- turn ACW/TDI into a TradingView `strategy()` script.
- redefine Trend Carrier, Momentum Fusion, Flow Score, Near/Anchor calculation, divergence detection or exhaustion detection.
- retune TDI's adaptive RSI mathematics merely to create more signals.
- add another master score.
- add a third HTF context layer.
- optimize specifically to one BTC, GOLD or HYPE move.
- start the future Signal Audit statistics engine inside G.

G may retain entry bar/price internally for lifecycle context and future Audit compatibility, but it will not calculate win rate, TP1/TP2, R-multiples or strategy performance yet.

---

## 5. Architecture Freeze Boundary

The following F1.3 semantics are frozen:

- price direction and structure classification.
- MA Core states such as `EXPAND / HOLD / CONTRACT / COMPRESS / FLIP`.
- TDI Trend Carrier direction.
- TDI Momentum phase.
- Flow `CONFIRM / OPPOSE / N/A` meaning.
- confirmed Near/Anchor hierarchy.
- LOCAL versus MTF scope semantics.
- IMPULSE / CONTINUATION / RECOVERY / PULLBACK / COUNTERTREND interpretation.
- divergence detection and `FRESH / ACTIVE / expired` lifecycle.
- exhaustion detection.
- hard distinction between local truth and higher-timeframe context.
- F1.3 risk authority principle that exhaustion is not automatically a reversal.

G may calibrate only the **promotion layer** and the new lifecycle built on top of that layer.

---

## 6. Signal Personality

### 6.1 Control location

G adds one ACW input:

`Signal Personality = Selective / Balanced / Active`

Default: **Balanced**.

The control lives in ACW only. TDI's existing `Adaptive Profile` remains a separate oscillator-responsiveness feature and is not renamed or repurposed.

This prevents the user from having to keep two personality settings synchronized and preserves the F1.3 bridge.

### 6.2 Personality rule

Signal Personality may change **promotion requirements only**.

It may not redefine:

- trend direction.
- structure.
- MA Core state.
- TDI momentum state.
- Flow state.
- Near/Anchor state.
- divergence state.
- exhaustion state.
- `X` or `INV` meaning after a lifecycle signal already exists.

Therefore the same bar may be described as `BEAR TREND • COOLING • FLOW SUPPORTS` in all three personalities while only the final `WATCH/READY` promotion differs.

### 6.3 Balanced — reference behavior

Balanced is the production reference and preserves F1.3 behavior wherever possible.

Balanced means:

- qualified evidence can reach READY without requiring perfect MTF agreement.
- imperfect but coherent opportunities remain WATCH.
- squeeze, mature exhaustion, severe directional conflict and no-edge conditions remain WAIT.
- local continuation is allowed when local evidence is strong, while opposing Anchor remains visible as risk.

Balanced must be the default preset.

### 6.4 Selective — stricter promotion

Selective starts from the Balanced result and may only downgrade readiness.

A Balanced `READY` is retained as Selective `READY` only when all of the following are true:

- `fQuality >= 60`.
- `abs(confluenceScore) >= 60`.
- no strong/mature exhaustion.
- no fresh opposing divergence.
- no Flow opposition.
- Anchor is not opposite the candidate direction.
- no direction conflict.
- momentum is not `COUNTER`.

If these stricter conditions are not met, the signal is downgraded to `WATCH`; it is not rewritten as the opposite direction.

A Balanced `WATCH` never becomes READY under Selective.

### 6.5 Active — earlier but bounded promotion

Active starts from the Balanced result and may promote a coherent Balanced `WATCH` to `READY` only when all of the following are true:

- `fQuality >= 50`.
- `abs(confluenceScore) >= 50`.
- MA Core supports the candidate direction.
- structure is compatible with the candidate direction.
- momentum is not `COUNTER`.
- Near and Anchor are not both opposite the candidate direction.
- no direction conflict.
- no squeeze.
- no strong/mature exhaustion.
- no corroborated fresh opposing divergence.

Flow opposition alone is not a hard veto in Active, but strong Flow opposition must raise the promotion requirement: when opposing Flow magnitude is `>= 35`, Active requires `fQuality >= 55` and `abs(confluenceScore) >= 55`.

Active never promotes a `WAIT` state that is WAIT because of a hard risk/veto condition.

### 6.6 No personality-based rewriting of history semantics

TradingView recalculates history when an input changes, so each personality naturally has its own historical A/X/INV sequence. That is acceptable.

Within one selected personality, however, lifecycle events must be deterministic and confirmed-bar based.

---

## 7. Final Readiness Pipeline

G formalizes the order of operations:

1. F1.3 computes market state and baseline `READY / WATCH / WAIT`.
2. Existing F1.3 risk authority is applied:
   - Exhaustion.
   - Divergence.
   - Flow opposition.
   - Anchor opposition.
   - structural reversal pressure.
3. Signal Personality modifies **promotion only**.
4. The resulting readiness is the G final readiness.
5. Signal Lifecycle consumes only the G final readiness plus frozen F state/risk evidence.

The lifecycle must never feed back into market-state calculations. It is a state/output layer, not a new trend engine.

---

## 8. Signal Lifecycle State Machine

The lifecycle belongs in ACW because ACW is the final arbiter.

The conceptual flow is:

`IDLE → ENTRY EVENT → ACTIVE → CAUTION → EXIT or INVALIDATED → RE-ARM → IDLE`

The four user-visible lifecycle event symbols are:

- `A↑` / `A↓` — Agreement / actionable opportunity begins.
- `!` — caution begins.
- `X` — active edge deteriorated enough to exit the lifecycle.
- `INV` — the original directional thesis is invalidated.

These are indicator lifecycle events, not guaranteed trade outcomes.

---

## 9. Entry Event — A↑ / A↓

### 9.1 Entry event condition

An `A↑` or `A↓` event is created only when:

- the bar is confirmed when `confirmedOnly` is enabled.
- final G readiness is `READY`.
- final action direction is non-zero.
- no lifecycle is currently ACTIVE/CAUTION in either direction.
- that direction is armed.
- the current bar is the first confirmed bar of the new eligible READY episode.

A continuing READY state does not print another A marker.

### 9.2 Stored entry context

On A event, ACW stores at minimum:

- direction.
- `bar_index`.
- close price of the event bar as lifecycle entry reference.
- archetype (`IMPULSE / CONT / RECOVERY / ...`).
- scope (`LOCAL / MTF`).
- selected Signal Personality.

The stored close price is reference context only. G does not infer a fixed TP or SL from it.

### 9.3 Signal age

While ACTIVE or CAUTION:

`signal age = current bar_index - entry bar_index`

The HUD must show this age when enabled.

---

## 10. ACTIVE State

After A, the lifecycle becomes ACTIVE.

ACTIVE may persist through normal market noise and does not require every subsequent bar to remain READY.

A temporary downgrade from READY to WATCH does not automatically terminate the lifecycle.

The lifecycle ends only through `X` or `INV`.

This avoids treating every ordinary momentum cooling phase as a new signal or immediate exit.

---

## 11. CAUTION State

CAUTION means the original direction still exists, but one or more meaningful deterioration signs appeared.

CAUTION is entered on the first confirmed bar while ACTIVE when at least one of the following is true in the active direction:

- trend becomes `TREND TIRED` / same-direction exhaustion begins but is not yet strong/mature.
- a fresh opposing divergence becomes active.
- Flow changes to oppose with magnitude `>= 15`.
- Anchor becomes opposite the active direction.
- readiness drops from READY to WATCH while one of the above risk conditions is present.
- momentum is `COOLING` or `PULLBACK` **and** MA Core is `CONTRACT` or `COMPRESS`.

CAUTION does not flip direction and does not by itself produce `X`.

If caution evidence disappears and the original direction remains valid, the lifecycle may return from CAUTION to ACTIVE without printing a new A marker.

### 11.1 Caution marker

The chart `!` marker is optional and defaults **OFF**.

The HUD always reflects CAUTION when lifecycle information is enabled.

---

## 12. EXIT Event — X

`X` means the original opportunity no longer has enough active edge to remain ACTIVE, while the broader directional thesis has not yet been proven opposite.

An X event fires on a confirmed bar when an active lifecycle is not invalidated and at least one of the following exit authorities is true:

1. **Strong exhaustion:** existing F1.3 `fExhaustionStrong` is true in the active direction.
2. **Corroborated fresh opposing divergence:** fresh opposing divergence plus at least one corroborator already defined by F1.3 (`CONTRACT`, `COOLING/PULLBACK`, context disagreement, or aging structure).
3. **Two-or-more deterioration votes**, where the available votes are:
   - opposing Flow magnitude `>= 15`.
   - opposite Anchor.
   - momentum `COUNTER` while Trend Carrier/price direction has not yet flipped.
   - MA Core `CONTRACT` or `COMPRESS` plus non-fresh structure.
   - structural `REVERSAL PRESSURE`.
4. **Sustained loss of edge:** final readiness remains WAIT for two consecutive confirmed bars while the active direction is still nominally intact and at least one deterioration vote above is present.

A lone squeeze/compression state is not enough to generate X unless accompanied by deterioration evidence.

X closes the lifecycle and begins re-arm logic.

---

## 13. INVALIDATED Event — INV

`INV` is stronger than X.

It means the original directional thesis itself is no longer accepted by the combined system.

INV fires on a confirmed bar when an active lifecycle exists and either:

1. The opposite direction becomes final G `READY`, **and** at least one independent ACW/TDI directional authority agrees with the opposite direction:
   - MA Core direction.
   - swing structure direction.
   - TDI Trend Carrier state.

or:

2. At least two of the three directional authorities below have flipped opposite the active signal:
   - MA Core direction.
   - swing structure direction.
   - TDI Trend Carrier state.

A temporary direction conflict, mixed state, opposing Anchor, divergence, Flow opposition or exhaustion alone is **not** sufficient for INV.

INV closes the lifecycle and begins re-arm logic.

If an opposite READY appears on the same bar as INV, G records INV first. The opposite A event may occur no earlier than the next confirmed bar after normal re-arm conditions are satisfied. G does not print `INV` and an opposite `A` on the same candle.

---

## 14. Re-Arm Semantics

The purpose of re-arming is to prevent marker spam and repeated A events during one continuous opportunity.

After an A event, that same direction is disarmed.

After X or INV, the direction remains disarmed until both conditions are met:

1. final readiness for that direction has been **not READY for at least two consecutive confirmed bars**, and
2. a later confirmed bar transitions back into READY.

A persistent READY episode can therefore produce only one A marker.

A WATCH/WAIT reset followed by a fresh READY promotion creates a new eligible opportunity.

The two-bar reset is global across Selective/Balanced/Active so X/INV semantics and lifecycle cadence remain comparable between personalities.

---

## 15. Lifecycle Conflict Resolution Priority

When multiple lifecycle events could occur on the same confirmed bar, G uses this priority:

1. `INV`
2. `X`
3. `!` CAUTION
4. return CAUTION → ACTIVE
5. new `A↑ / A↓`

Only one terminal lifecycle event may print for the currently active signal on a bar.

No same-bar opposite A is allowed after INV/X.

---

## 16. Visual Design

### 16.1 Price-chart markers

ACW owns all lifecycle markers.

Default visibility:

- `A↑ / A↓`: ON.
- `!`: OFF.
- `X`: ON.
- `INV`: ON.
- signal age in HUD: ON.

Bullish entry events plot below price; bearish entry events plot above price.

Exit/invalidation placement follows the active signal direction so the lifecycle history remains easy to read.

Markers must be small enough for mobile charts and must not obscure candles.

### 16.2 Marker identity

- `A↑ / A↓` receives the strongest visual emphasis.
- `X` is clear but visually weaker than A.
- `INV` must be visually distinct from X because it means thesis failure rather than ordinary edge deterioration.
- `!` remains subtle.

The exact palette follows the selected ACW theme; no new global theme system is added.

### 16.3 Plot budget

Lifecycle visuals may add dedicated `plotshape()` calls because ACW F1.3 remains comfortably below the TradingView 64-plot ceiling.

Implementation must re-count all plot-producing calls after lifecycle alerts and markers are added.

---

## 17. HUD Design

### 17.1 Descriptive HUD

The Descriptive HUD adds one lifecycle row and, when active, a concise entry-age reference.

Examples:

- `TRADE STATE  LONG ACTIVE • 6 bars`
- `TRADE STATE  SHORT ACTIVE • 3 bars`
- `TRADE STATE  CAUTION • TREND TIRED`
- `TRADE STATE  CAUTION • BEAR DIVERGENCE FRESH`
- `TRADE STATE  EXIT • EDGE DETERIORATED`
- `TRADE STATE  INVALIDATED • TREND FLIPPED`
- `ENTRY EVENT  A↑ • 6 bars ago`

The final wording should favor plain human language over internal variable names.

### 17.2 Compact HUD

Compact mode must remain compact.

Examples:

- `L ACTIVE +6b`
- `S ACTIVE +3b`
- `L ! EXHAUST`
- `S ! DIV`
- `EXIT`
- `INV`

No large diagnostic expansion is allowed in Compact mode.

### 17.3 Flow wording polish

G should remove ambiguous signed prose such as `FLOW SUPPORTS -30.0`.

Preferred descriptive forms are directional:

- `BEAR FLOW SUPPORTS 30`
- `BULL FLOW SUPPORTS 24`
- `FLOW OPPOSES 18`
- `FLOW N/A`

The numerical sign may remain available in diagnostic/research display, but the normal descriptive sentence should not force the user to mentally decode a negative number that semantically supports a bearish trend.

---

## 18. Alerts

Because the lifecycle is intended to help when the user is not continuously watching the chart, G exposes TradingView alert conditions for:

- `A↑` Agreement Long.
- `A↓` Agreement Short.
- `X` lifecycle exit.
- `INV` lifecycle invalidation.
- optional CAUTION event.

Alerts use the exact same confirmed lifecycle booleans as chart markers. There must not be separate alert logic that can disagree with the historical marker.

Existing TDI and ACW alert conditions remain intact unless a direct duplicate would become confusing.

---

## 19. Exhaustion and Divergence Authority — Preserved

G must preserve the F1.3 distinction:

- **Trend direction ≠ trend health.**
- ordinary exhaustion can downgrade a good continuation without declaring reversal.
- mature/corroborated exhaustion can end lifecycle edge through X.
- fresh opposing divergence can create caution and, when corroborated, contribute to X.
- divergence alone does not flip direction or create INV.
- historical/expired divergence remains visible if the oscillator draws it, but it no longer affects current lifecycle decisions.

No G personality may bypass strong exhaustion or reinterpret divergence as a direct reversal signal.

---

## 20. Flow N/A Behavior

Markets or feeds without useful volume must continue to function normally.

When Flow is N/A:

- no Flow vote is counted for CAUTION or X.
- no penalty is invented as a substitute.
- ACW/TDI continue from price, structure, momentum, context, divergence and exhaustion evidence.

G must retain the GOLD behavior validated in F1.3 where Flow N/A does not break continuation logic.

---

## 21. Calibration Museum

G is validated against three intentionally different market archetypes.

### 21.1 BTC — compression and mixed-context museum

Primary behaviors to preserve:

- lower-TF rebound versus medium-TF weakness.
- squeeze/compression produces WAIT rather than signal spam.
- local direction can exist without being promoted to entry edge.
- mixed Near/Anchor context remains readable.
- Active must not turn genuine compression into READY.

### 21.2 GOLD / XAUUSD — divergence and missing-flow museum

Primary behaviors to preserve:

- fresh opposing divergence affects risk but does not automatically reverse the signal.
- old divergence decays from current decision authority.
- Flow N/A remains safe.
- LOCAL and MTF continuation remain distinct.
- a genuinely clean higher-timeframe continuation can still reach READY.

### 21.3 HYPE — conflict/exhaustion stress museum

Primary behaviors to preserve:

- strong Flow opposition remains visible.
- local trend may coexist with counter-Anchor risk.
- countertrend/local-continuation labels stay honest.
- exhaustion must visibly downgrade lifecycle health.
- Selective/Active must not erase severe HTF conflict or hard risk.

G does not require every market to generate the same number of A events.

---

## 22. Cross-Market Calibration Rule

No threshold change is accepted merely because one screenshot looks better.

A calibration survives only if:

- it fixes or improves the intended archetype, and
- it does not create an obvious regression in the other museum cases.

The goal is not equal signal frequency across assets. The goal is consistent semantics across assets.

---

## 23. Test Requirements

Implementation must use test-first development around extracted/pure decision logic where Pine itself cannot be executed locally.

At minimum the G regression suite must prove:

1. Balanced preserves F1.3 readiness for baseline fixtures.
2. Selective can downgrade Balanced READY but never promote Balanced WATCH/WAIT.
3. Active can promote only eligible Balanced WATCH states and cannot bypass hard blockers.
4. squeeze blocks Active promotion.
5. mature exhaustion blocks Active promotion.
6. corroborated fresh opposing divergence blocks Active promotion.
7. A prints once on the first eligible confirmed READY bar.
8. persistent READY does not repeat A.
9. signal age increments correctly.
10. first deterioration enters CAUTION without immediately forcing X when evidence is insufficient.
11. strong exhaustion creates X, not INV, when direction itself remains valid.
12. corroborated divergence can create X without flipping direction.
13. one isolated Flow-opposition vote does not automatically create X.
14. two deterioration votes can create X.
15. opposite directional authority can create INV according to the two-authority rule.
16. opposing Anchor alone cannot create INV.
17. X/INV require re-arm before another same-direction A.
18. no same-bar `INV + opposite A` occurs.
19. Flow N/A contributes no false risk vote.
20. lifecycle alerts and plotted event booleans are identical.
21. Compact HUD remains compact and Descriptive HUD includes lifecycle wording.
22. bridge packing/decoding remains exact and unchanged.
23. total TradingView plot-producing statements remain below 64 for each script.

Local tests are static/behavioral evidence only. Final Pine compilation and runtime behavior must still be verified in TradingView.

---

## 24. Implementation Constraints

G implementation must preserve Pine v6/mobile safety:

- parser-safe expressions.
- confirmed-bar gating for lifecycle events.
- no repainting from lifecycle state.
- no new `request.security()` calls unless absolutely required; the design itself requires none.
- no dynamic series-length patterns that Pine rejects.
- no global scalar mutation from invalid local scope patterns.
- bridge payload must remain within exact-integer-safe packing bounds.
- plot count must remain below TradingView's 64-plot limit.
- no unnecessary labels/lines when plotshape can express the lifecycle event.

---

## 25. Versioning

The first implementation is the `1g` matched pair:

- `ACW_1g.pine`
- `TDI_1g.pine`

Indicator titles/short titles must use the same `1g` generation tag so the user can immediately see that the two scripts belong together.

Later G calibrations, if testing proves they are necessary before production freeze, increment only the numeric suffix (`1g1`, `1g2`, ...). Same-generation ACW/TDI files are treated as a matched pair.

---

## 26. Production Freeze Rule

Once G passes:

- local static/behavioral verification,
- TradingView compilation,
- BTC/GOLD/HYPE runtime review,
- lifecycle marker review,
- and user acceptance,

G becomes the production baseline.

After freeze, new features are not added merely because another idea is interesting. Changes require either:

- a reproducible defect,
- a demonstrated semantic inconsistency,
- or evidence from the future Signal Audit that a specific calibration systematically underperforms its intended role.

This is the mechanism that prevents endless tuning.

---

## 27. Future Work — Explicitly After G

After production freeze, the next research project may be the previously discussed **Signal Audit Lab**.

That future system may use G's stored lifecycle entry/event information to study:

- signal archetype.
- entry reference.
- MFE/MAE.
- bars-to-target.
- exit/invalidation timing.
- regime and timeframe segmentation.
- R/ATR-normalized outcomes.

It must remain analytically separate from G's live decision engine until evidence justifies any later calibration change.

---

## 28. Acceptance Summary

G is acceptable when the pair can truthfully express the complete story:

> **What is the market doing?**  
> **Is the move healthy or tired?**  
> **Is there enough evidence for READY under the selected personality?**  
> **When did the actionable state begin?**  
> **Is it still active, only weakening, ready to exit, or invalidated?**

The final visual language is intentionally simple:

`A↑ / A↓ → ACTIVE → ! → X or INV → RE-ARM`

while all deeper ACW/TDI intelligence remains available underneath.
