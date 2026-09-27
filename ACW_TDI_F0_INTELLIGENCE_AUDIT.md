# ACW ∞ + TDI ∞ — F0 Intelligence Audit

**Audit date:** 2026-09-27  
**Source pair:** ACW 1e3 + TDI 1e3  
**ACW:** 938 lines — SHA256 `dabcd63572ebbca20ac7305cd7f823e0ff7ae1d7b73531ec87893f78b7fd85bc`  
**TDI:** 601 lines — SHA256 `b7aa4e594a8e7e087f461272f8bb456e7f6fa76527ffe5bd26ae56cedf70a64a`

## Executive verdict

The project does **not** need another major indicator engine before F. The code already contains enough directional, structural, momentum, flow, volatility and event intelligence. The biggest gains now come from **assigning each subsystem one clear responsibility**, exposing information that is currently compressed into aggregate scores, and preventing correlated price-derived engines from being treated as independent confirmation.

The S2S lesson is strongly supported by the source code: the next evolution should be **chart → structure → context → quality → readiness/trigger**, not another layer of filters.

---

## 1. ACW MA/ribbon audit — not decorative, but partly under-expressed

### MAMA/FAMA is deeply integrated

ACW's MAMA/FAMA engine is not decoration. `mamaScore` is built from:

- 76% ATR-normalized MAMA–FAMA spread
- 24% ATR-normalized MAMA slope

That score receives the largest default weight in native ACW fusion:

- MAMA/FAMA: 0.45
- MACD/EMA council: 0.35
- confirmed swing structure: 0.20

The MAMA score also participates in ACW's alignment/regime logic and drives the visual MAMA/FAMA coloring/fill.

**Conclusion:** the MAMA cloud is already a real intelligence source and is arguably the cleanest quantified MA geometry inside ACW.

### The fast/slow EMA ribbon contains visual information the score does not fully quantify

The MACD/EMA council uses ten binary ±1 votes. It does measure direction, slope and MACD/histogram behavior, but it does **not** explicitly quantify ATR-normalized EMA separation or whether the ribbon itself is widening/narrowing in magnitude.

This matters because the human eye reads:

- stacked + widening ribbon = propulsion
- stacked + narrowing ribbon = cooling
- compressed ribbon = transition
- cross/flip = state change

The current MACD council can give nearly the same score to a barely separated bullish stack and a dramatically expanded bullish stack if the same binary conditions are true.

### Two MACD votes are exact duplicates

The ten-vote council contains two exact logical duplicates:

- `fastMA > slowMA` and `macdLine > 0` are the same condition because `macdLine = fastMA - slowMA`.
- `macdLine > macdSignal` and `macdHist > 0` are the same condition because `macdHist = macdLine - macdSignal`.

So the nominal 10-vote council contains only 8 unique logical ideas, with two concepts intentionally or accidentally receiving double weight.

**Recommendation for F:** do not immediately rewrite the legacy MACD score because that would move the E baseline. Build an explicit semantic **MA CORE** beside it first, using the existing MAMA/FAMA geometry plus an explicit EMA-ribbon geometry measure. Later G can decide whether the old council weighting should be rationalized.

---

## 2. ZigZag / HH-HL structure — strong authority, but stale by design

The swing engine is confirmed-pivot based and therefore sanitized/non-repainting after confirmation. This is good. It correctly classifies only:

- HH + HL → +100
- LH + LL → -100
- otherwise → 0

However, the result is all-or-nothing and can remain at ±100 until enough future bars confirm a new opposing structure.

With automatic pivot lengths, the confirmation lag becomes meaningful on higher timeframes. An 8-bar right pivot on a 6h chart can represent roughly two days of structural delay.

The code already stores `lastHighTime` and `lastLowTime`, but those timestamps are never used to reduce structural authority or expose freshness. `swingEvent` is also calculated and then not used downstream.

**Buried treasure:** F can distinguish **CONFIRMED STRUCTURE** from **LIVE MA STATE** and add structure freshness/age without weakening the non-repainting design. This is likely a better solution than making pivots faster.

---

## 3. ACW native fusion and confidence — useful, but not independent evidence

Native ACW fusion is:

`MAMA 45% + MACD 35% + Structure 20%`, then mildly damped by price efficiency.

Its `confidence` is primarily a coherence/strength index built from fusion magnitude, sign agreement of those same components, and efficiency. It is **not an empirically calibrated probability of trade success**.

This distinction becomes important later when the Signal Audit / TP-SL lab is added. A HUD reading of `65% confidence` currently means roughly "strong coherent internal evidence," not "65% historical win probability."

**Recommendation:** keep the number for now, but in F conceptually treat it as **quality/coherence**. The later audit lab can calibrate it into evidence-based probabilities if useful.

---

## 4. TDI Local Trend Carrier — one of the strongest architectural pieces

The E-generation TDI trend carrier is well separated from the oscillator core:

- price persistence = signed efficiency + ATR-normalized displacement
- trend geometry = EMA 21/50 separation + fast-EMA slope
- price core = 55% persistence + 45% geometry
- persistent `trendState` comes from `priceCore`

OBV/volume flow does **not** create direction. It can only add/subtract up to about 10 points to the displayed carrier and later adjust trust/confidence.

That is exactly the architecture we wanted: **price determines direction; flow comments on the quality of that direction.**

This part should be preserved.

---

## 5. TDI CHOP/SQUEEZE are oscillator conditions, not market-direction truth

TDI's `CHOP` comes from RSI-domain conditions:

- center chop: Fast TDI near 45–55 with weak normalized energy
- statistical chop: RSI efficiency < 0.28 and |Fusion| < 38

TDI `SQUEEZE` is based on the percentile rank of the TDI volatility-band width.

These are valid oscillator states, but they are **not equivalent to price structure being directionless**. This explains many screenshots where price/ribbons are clearly directional while the TDI HUD says CHOP or COIL.

E already improved this by allowing medium Trend Carrier states and making CHOP a soft veto for ACW-assisted continuation. F should finish the semantic separation:

- price/MA structure = STATE
- oscillator chop/squeeze = QUALITY/READINESS CONDITION

A bullish market can therefore be `BULL • OSC CHOP`, `BULL • SQUEEZE`, `BULL • COOLING`, etc., without losing its directional identity.

---

## 6. The current "HTF Context" is almost entirely decorative — biggest F opportunity

This is the most important hidden finding in the audit.

TDI calculates an `htfState` using a requested timeframe and displays it in the TDI dashboard. But that state is **not used by**:

- TDI trend direction
- TDI Fusion
- TDI confidence
- TDI READY logic
- TDI continuation logic
- the semantic bridge to ACW
- ACW confluence/action logic

It is a display-only context row.

Additionally, the default context timeframe is fixed at `60`. On a 1D or 3D chart, `60` is not a higher timeframe at all; it is a lower timeframe. Therefore the label `HTF 60` is semantically misleading on higher charts, and the behavior of a lower-timeframe `request.security()` sample is not the same thing as true higher-timeframe context.

**This should be F's primary architectural upgrade.** F should use an actual adaptive higher-timeframe ladder or explicit context map and make that context participate in classification, while keeping local direction readable independently.

---

## 7. ACW already contains a true price-compression state distinct from TDI squeeze

ACW has its own `COMPRESSION` regime based on low ATR/price volatility rank plus a subdued MACD council.

That is conceptually different from TDI's RSI-band squeeze.

This is valuable. We already have the ingredients to distinguish:

- **price/structure compression**
- **oscillator squeeze**

They should not be merged into one generic "no trend" condition. F can use both without adding a new engine.

---

## 8. Current confluence can overstate independence because multiple engines read the same price trend

ACW MAMA, ACW MACD/EMA, ZigZag structure, and TDI's 21/50 EMA price carrier are all derived from the same underlying price path in different ways.

When ACW and TDI Trend agree, current confluence boosts ACW score/confidence as if TDI direction were another confirming source. It is useful corroboration, but it is **not fully independent evidence**.

This can cause "confidence inflation" when several highly correlated trend transforms all agree.

**F family model:** group evidence by responsibility rather than counting every transform as an independent vote:

- Structure family: ZigZag + MA Core + price carrier
- Momentum family: TDI oscillator Fusion/momentum
- Flow family: OBV
- Volatility/regime family: price compression + oscillator squeeze
- Context family: true higher-timeframe state

This preserves information while reducing duplicate voting.

---

## 9. Some existing intelligence is display/event-only

These currently do not participate materially in the decision engine:

- TDI higher-timeframe row — display only
- qualified divergence — visual + alert only
- shark-fin events — visual only
- squeeze-release events — visual + alert only

That is not automatically a flaw. Divergence in particular should probably remain a **warning/risk modifier**, not a direction engine, until the audit lab proves it improves outcomes.

---

## 10. Dead / legacy code found — cleanup later, not an F priority

Examples include:

### ACW
- `tdiImpulseReady` decoded but unused
- `biasName` unused
- `dashDetail` input unused
- `swingEvent` produced but unused
- stored swing timestamps not used downstream

### TDI
- `biasBull` / `biasBear` unused
- `fastBasisUp` / `fastBasisDn` unused
- `longTimingReady` / `shortTimingReady` unused
- `inExtOS` calculated but final zone fallback makes the variable unnecessary

These are safe candidates for G cleanup after F behavior is frozen. Removing them now gives little intelligence benefit and unnecessarily touches stable code.

---

# Intelligence Responsibility Map for F

| Subsystem | Current behavior | F responsibility | Recommended influence |
|---|---|---|---|
| MAMA/FAMA | continuous ATR-normalized spread + slope | **MA Core / live trend geometry** | STATE |
| ACW EMA/MACD | binary direction/slope/momentum council | **MA Core propulsion + legacy ACW score** | STATE + QUALITY |
| ZigZag HH/HL | confirmed structural direction | **Confirmed structure authority** | STRUCTURE, with freshness |
| TDI Price Carrier | price persistence + EMA geometry | **Directional corroboration** | STATE, not independent confidence bonus |
| TDI oscillator Fusion | RSI-domain drive/cooling/pullback | **Momentum condition** | QUALITY + TIMING |
| OBV Flow | volume confirmation/opposition | **Participation / breath** | QUALITY only |
| ACW Compression | low price volatility + subdued MACD | **Price compression** | STATE/CONTEXT |
| TDI Squeeze/Chop | oscillator compression/inefficiency | **Oscillator condition** | QUALITY/READINESS |
| Exhaustion | stretched oscillator losing energy | **Risk warning / veto** | READINESS |
| TDI HTF row | currently display-only | **True MTF context** | CONTEXT |
| Divergence | display + alert | **Warning** | RISK/QUALITY only initially |
| READY/CONT/IMPULSE | threshold gates | **Trigger layer** | ACTION |

---

# Recommended F architecture

The safest F evolution is not a rewrite of E. Keep E's working signal engine as the control branch and add an interpreter above it.

## Layer 1 — STRUCTURE

Create an explicit **MA CORE** from information already present:

- MAMA/FAMA direction
- ATR-normalized MAMA/FAMA separation
- MAMA slope
- fast/slow EMA direction
- ATR-normalized fast/slow EMA separation
- change in EMA separation (expanding vs contracting)
- EMA slopes

Semantic states can be compact, for example:

- `BULL • EXPAND`
- `BULL • COOL`
- `COMPRESS`
- `FLIP ↑`
- `FLIP ↓`
- `BEAR • COOL`
- `BEAR • EXPAND`

Do **not** simply add MA Core as another weighted score on top of MAMA/MACD. That would double-count it. Use it as an interpretable state.

Add **structure freshness** to the confirmed ZigZag state so the HUD can distinguish a fresh confirmed HH/HL from an old HH/HL being challenged by a live reversal.

## Layer 2 — CONTEXT

Replace the fixed `HTF 60` concept with a genuine timeframe relationship. The exact ladder should be designed before coding, but the principle is:

- current chart = local state
- one or more strictly higher frames = context
- never call a lower timeframe "HTF"

Context should describe, not automatically override:

- `HTF SUPPORTS`
- `HTF OPPOSES`
- `LTF PULLBACK`
- `LTF RECOVERY`
- `MTF ALIGNED`
- `COUNTERTREND`

## Layer 3 — QUALITY

TDI oscillator momentum, OBV flow, efficiency, squeeze, divergence and exhaustion comment on the quality of the state.

Examples:

- `BULL • STRONG`
- `BULL • COOLING`
- `BULL • DRY`
- `BULL • OSC CHOP`
- `BEAR • EXHAUST`

Weak secondary evidence should normally reduce quality, not erase direction.

## Layer 4 — READINESS / TRIGGER

Only here should E's working gates decide:

- WAIT
- WATCH
- READY
- LONG/SHORT CONT
- LONG/SHORT IMPULSE

Squeeze/exhaustion can still block appropriate triggers without rewriting the underlying market state.

---

# Highest-value F priorities

**P0 — true MTF context:** current HTF row is display-only and can be a lower timeframe on HTF charts.  
**P1 — explicit MA Core:** surface the ribbon information the eye already sees, especially EMA separation/expansion.  
**P2 — structure freshness:** keep confirmed swings, but expose their age/staleness.  
**P3 — family-based confluence:** stop treating correlated price transforms as fully independent confirmation.  
**P4 — semantic HUD:** display STATE → CONTEXT → QUALITY → TIMING/ACTION.  
**P5 — cleanup:** remove dead variables only after F is behaviorally frozen.

---

## Final audit verdict

The "golden treasure" is not a missing indicator. It is already in the code:

1. MAMA/FAMA contains a strong continuous trend-geometry signal.
2. The EMA ribbon visually contains expansion/contraction information that the binary MACD council only partially captures.
3. ZigZag has reliable confirmed structure but no freshness concept.
4. TDI's price carrier is a good independent *role* (direction) but not truly independent *data* from ACW price trend.
5. OBV is already correctly demoted to confirmation/trust rather than direction authority.
6. ACW price compression and TDI oscillator squeeze are two distinct states and should stay distinct.
7. The supposed HTF context currently has almost no intelligence-layer effect and is the clearest unfinished piece.
8. Current confidence values are coherence scores, not calibrated win probabilities.

**Recommended next move:** freeze E logic as the control, design F around MA Core + true MTF context + state/quality/readiness separation, and avoid adding any new major engine until the Signal Audit later proves a real information gap.
