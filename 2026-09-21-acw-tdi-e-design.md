# ACW ∞ + TDI ∞ — E Generation Design Specification

**Date:** 2026-09-21  
**Generation:** E  
**Target pair:** `ACW 1e` + `TDI 1e`  
**Status:** Design complete, awaiting user review before implementation planning

---

## 1. Purpose

E fixes a specific weakness revealed during D-generation testing: TDI can correctly detect that oscillator momentum has cooled, yet incorrectly present that condition as `MIXED` or `CHOP` even while price remains in a strong persistent directional trend.

The goal of E is to separate four distinct questions that were previously blended together:

1. **Direction** — where price is persistently travelling.
2. **Momentum** — whether that move is accelerating, cooling, pulling back, or recovering.
3. **Flow** — whether volume participation supports or opposes the price-direction story.
4. **Timing** — whether current TDI conditions permit a fresh action trigger.

E must preserve the strengths of D while removing the semantic ambiguity between "momentum cooled" and "trend disappeared."

---

## 2. System Roles

### ACW remains the environment / structure authority

ACW continues to own:
- MAMA/FAMA directional context.
- MACD council context.
- confirmed swing structure (`HH/HL`, `LH/LL`, mixed).
- ACW Fusion and native confidence.
- recovery / pullback structural interpretation.
- final confluence action language.

### TDI becomes a four-layer local timing engine

TDI E owns:
- **Trend Carrier** — local price-direction persistence.
- **Momentum Fusion** — existing TDI Fusion mathematics.
- **Flow Score** — OBV-derived participation support.
- **Timing / Regime** — existing squeeze, chop, expansion, exhaustion, quality-ready logic.

### HTF remains context only

The existing higher-timeframe TDI row remains visible as context, but **HTF data must not enter the Trend Carrier calculation**.

This avoids hidden double-counting when ACW and TDI are combined.

---

## 3. Non-Goals

E will not:
- merge ACW and TDI into one script.
- add automatic trading or order execution.
- replace the existing TDI Fusion engine.
- retune all D thresholds simultaneously.
- let OBV choose direction by itself.
- use confirmed swing pivots as the primary TDI carrier.
- use HTF values inside the local Trend Carrier.
- enlarge the mobile HUD significantly.
- optimize parameters specifically to one BTC move.

---

## 4. TDI Trend Carrier Architecture

The Trend Carrier is a new local price-domain score normalized approximately to `-100 … +100`.

It is built from two price components:

### 4.1 Price Persistence

Price Persistence measures whether price is travelling persistently rather than oscillating.

Initial E inputs/defaults:
- local persistence window: approximately 16 bars.
- ATR normalization: ATR(14).

Subcomponents:

#### Signed price efficiency

Concept:

`Signed Efficiency = signed net displacement / total path travelled`

Normalized to approximately `-100 … +100`.

This rewards sustained directional movement and penalizes noisy back-and-forth movement.

#### ATR-normalized displacement

Concept:

`Displacement = (price - price[n]) / ATR`

Then clamp / normalize to `-100 … +100`.

A single giant candle may create large displacement, but cannot create a perfect persistence score if follow-through efficiency is poor.

#### Persistence blend

Initial weighting:

- `60% Signed Efficiency`
- `40% ATR-normalized Displacement`

These are initial E defaults, not claims of universal optimum.

---

## 5. Trend Geometry

Trend Geometry measures the slower physical shape of price.

Initial geometry uses:
- EMA21.
- EMA50.
- ATR-normalized EMA separation.
- EMA21 slope / persistence.

Geometry should remain bullish while price stays above a rising local trend structure, even if RSI-derived momentum cools.

Geometry is normalized to approximately `-100 … +100`.

---

## 6. Price Core

The actual directional authority is **Price Core**, not OBV and not TDI Fusion.

Initial weighting:

- `55% Price Persistence`
- `45% Trend Geometry`

`Price Core` is normalized / clamped to `-100 … +100`.

The Trend Carrier state is derived from Price Core with hysteresis.

---

## 7. OBV Flow Engine

OBV is included because it provides information orthogonal to both price persistence and RSI momentum.

The principal memory anchor is approximately **30 bars**.

E does not use raw absolute OBV as a directional score. Instead it derives:

- OBV relative to its ~30-bar baseline.
- normalized slope of the OBV baseline.
- persistence of OBV remaining above/below its baseline.

These components produce:

`Flow Score = -100 … +100`

### 7.1 Flow authority rule

OBV Flow may:
- reinforce confidence.
- reduce confidence when opposing.
- create a `FLOW CONFIRM` / `FLOW OPPOSE` semantic state.

OBV Flow may not:
- flip BULL to BEAR.
- flip BEAR to BULL.
- create LONG / SHORT readiness.
- override Price Core direction.

Price remains the directional authority.

### 7.2 Missing or unreliable volume

If volume / OBV is unavailable or unusable:
- Flow becomes `N/A`.
- Flow contribution becomes zero.
- TDI remains fully functional from Price Core + Momentum + Timing.

---

## 8. Trend Carrier Score and Hysteresis

The displayed Trend Carrier score may receive a **small capped Flow influence** for confidence/display nuance, approximately within `±10` points.

However, **Trend State is derived from Price Core**, not from the flow-adjusted display score.

Initial hysteresis concept:

- enter BULL when Price Core > approximately `+24`.
- hold BULL while Price Core remains above approximately `+8`.
- enter BEAR when Price Core < approximately `-24`.
- hold BEAR while Price Core remains below approximately `-8`.

This prevents frequent `BULL → MIXED → BULL` flicker during normal consolidation.

Direct BULL→BEAR or BEAR→BULL transitions require genuine movement of Price Core through the opposite side rather than a temporary oscillator swing.

---

## 9. Momentum Engine

The existing TDI Fusion mathematics remains intact for the first E build.

Fusion is no longer treated as persistent trend direction.

Instead it describes **momentum phase relative to the Trend Carrier**.

For a bullish Trend Carrier:

- **DRIVING** — Fusion strongly reinforces trend.
- **COOLING** — Fusion relaxes toward neutral while Trend Carrier remains bullish.
- **PULLBACK** — Fusion temporarily points against the bullish carrier.
- **RECOVERING** — Fusion turns back toward the bullish carrier after cooling/pullback.
- **COUNTER** — sustained opposite momentum is materially challenging the carrier.

Bearish behavior mirrors the same semantics.

When Trend Carrier is MIXED, momentum state remains descriptive without pretending a persistent trend exists.

---

## 10. Regime and Timing

The D-generation regime engine remains initially unchanged:

- SQUEEZE
- CHOP
- EXHAUSTION
- EXPANSION
- TREND
- TRANSITION

The current quality-ready logic also remains initially unchanged.

This is deliberate: E changes **interpretation architecture first**, not every threshold simultaneously.

Trend and Timing are independent truths.

Examples:

- `TREND BULL + MOMENTUM COOLING + REGIME CHOP + TIMING WAIT`
- `TREND BULL + MOMENTUM DRIVING + REGIME EXPANSION + TIMING READY`
- `TREND BULL + MOMENTUM PULLBACK + FLOW CONFIRM + TIMING WAIT`

---

## 11. E Single-Bus Bridge

The bridge remains **one hidden plot / one manual connection**.

The E bus carries semantic information ACW actually needs:

1. Trend Carrier score (`-100 … +100`).
2. Trend State (`BEAR / MIXED / BULL`).
3. Momentum Fusion (`-100 … +100`).
4. Flow Score (`-100 … +100`, with N/A encoding support).
5. Confidence (`0 … 100`).
6. Regime enum.
7. Timing Ready (`SHORT / WAIT / LONG`).
8. Event Signal (`SHORT / NONE / LONG`).

TDI Energy remains internal and is removed from the bridge because it is redundant with Momentum Fusion for ACW confluence purposes.

The bus must remain exactly representable in Pine float precision and must preserve safe fallback behavior when unlinked.

---

## 12. ACW E Interpretation

### 12.1 Directional agreement

ACW direction continues to come from ACW Fusion / structure context.

TDI direction comes from **Trend State**, not from raw TDI Fusion.

Therefore:

- ACW bullish + TDI Trend BULL = directional alignment.
- ACW bearish + TDI Trend BEAR = directional alignment.
- opposite ACW/TDI Trend states = true directional conflict.
- temporary opposite Momentum Fusion inside a persistent Trend Carrier is **not** directional conflict.

This is the central semantic improvement of E.

### 12.2 Momentum phase

ACW receives Momentum Fusion and interprets it relative to Trend State.

Momentum influences:
- action quality.
- timing language.
- confidence / saturation.

Momentum does not erase persistent direction by itself.

### 12.3 Flow

Flow modifies trust only.

Flow confirmation may add a modest confidence reinforcement.

Flow opposition may subtract a modest confidence amount and surface a `FLOW OPPOSE` state.

Initial cap: approximately `±8–10 confidence points`.

Flow may not create a synchronized LONG/SHORT action by itself.

### 12.4 Timing

A premium synchronized action still requires TDI timing permission.

Examples:

- aligned direction + DRIVING momentum + Flow confirm + READY → eligible for `LONG SYNC` / `SHORT SYNC`.
- aligned direction + COOLING momentum + CHOP → `WAIT TIMING`.
- aligned direction + EXHAUSTION → `WAIT • EXHAUST`.
- aligned direction + SQUEEZE → `WAIT • SQUEEZE`.

---

## 13. Recovery / Pullback Semantics

D-generation structural language remains.

Examples:

- bullish TDI Trend while ACW confirmed structure is still bearish → `RECOVERY ↑`.
- bearish TDI Trend while ACW confirmed structure is still bullish → `PULLBACK ↓`.

E improves these states by separating momentum/timing from directional persistence.

For example:

- `RECOVERY ↑ / COOLING`
- `RECOVERY ↑ / EXHAUST`
- `PULLBACK ↓ / RECOVERING`

The exact mobile wording must remain compact.

---

## 14. ACW E Dashboard

The linked ACW dashboard keeps approximately the same mobile footprint.

Target rows:

1. PROFILE
2. REGIME
3. STRUCTURE
4. ACW
5. TDI TREND
6. MOM / FLOW
7. CONFLUENCE
8. CONFIDENCE
9. TIMING
10. ACTION

Example:

```text
ACW ∞ CONFLUENCE
PROFILE       SCALP 3–5m
REGIME        TREND
STRUCTURE     HH / HL ↑
ACW           +71
TDI TREND     BULL +68
MOM / FLOW    COOL -4 • +57
CONFLUENCE    ALIGNED 76
CONFIDENCE    68%
TIMING        WAIT • CHOP
ACTION        WAIT TIMING
```

---

## 15. TDI E Dashboard

TDI remains compact and mobile-first.

Target semantic rows:

- ACTION
- REGIME
- TREND
- MOMENTUM
- FLOW
- CONF
- VOL / EFF
- ENGINE
- HTF 60
- ZONE
- STATE

Example:

```text
∞ TDI E
ACTION        WAIT
REGIME        CHOP
TREND         BULL +74
MOMENTUM      COOLING -3
FLOW          CONFIRM +61
CONF          46%
VOL / EFF     27% / .31
ENGINE        AUTO 7–15m
HTF 60        BULL C
ZONE          ENTRY ↑
STATE         COOL
```

---

## 16. Visual Readability Rules

### 16.1 ACW zigzag

Current bright cyan/green bullish zigzag is too bright on the user's light blue/white chart background.

E default bullish structural line becomes a deeper emerald/teal green around:

`#00A878`

Bearish zigzag remains clearly red/magenta.

Default structural width remains 3.

### 16.2 ACW HUD text

All meaningful value text on colored ACW HUD cells becomes **white**.

Color communicates through the cell background, not through low-contrast colored letters.

The colorful HUD itself remains.

### 16.3 Semantic color language

- green/teal = bullish direction / support.
- red/magenta = bearish direction / support.
- gold = squeeze / coil / caution.
- violet = exhaustion.
- gray-blue = neutral / chop.

Important HUD text remains white wherever the background already carries semantic color.

---

## 17. Candle Coloring

ACW E candle coloring should follow **confluence direction**, not raw TDI Fusion.

Momentum may influence color saturation / transparency but may not reverse the underlying directional color unless the persistent TDI Trend Carrier and/or ACW context changes accordingly.

This avoids visual contradiction such as bearish candle coloring during a bullish persistent trend merely because TDI Fusion temporarily cooled below zero.

---

## 18. Signal Rules

Native ACW signals remain available.

Premium synchronized signals require:

- ACW directional qualification.
- TDI Trend State agreement.
- no true directional conflict.
- TDI Timing Ready in the same direction.
- confidence floor.
- no exhaustion block.

Momentum and Flow may strengthen or weaken quality, but neither may independently create a premium synchronized signal.

D-generation cooldown/re-arm behavior remains unless testing reveals a specific repeatable failure.

---

## 19. Failure Safeguards

E must safely handle:

- missing volume.
- weak / flat OBV.
- one-candle price spikes.
- oscillator cooling inside strong trends.
- high-volume sideways chop.
- squeeze conditions.
- genuine trend reversals.
- TDI bridge unlinked / malformed source.
- different crypto symbols and timeframes.

Fallback rules:

- invalid bridge → native ACW behavior.
- missing Flow → Flow N/A, zero flow influence.
- no confirmed Trend Carrier → Trend MIXED, no invented directional certainty.

---

## 20. Primary Test Matrix

Primary instruments:
- BTCUSDT.
- ETHUSDT.

Primary timeframes:
- 1m.
- 3m.
- 5m.
- 7m.
- 15m.

Context sanity checks:
- 45m.
- 1h.
- 2h.
- 4h.
- 6h.

Required market behaviors:

1. strong directional trend.
2. healthy consolidation inside trend.
3. pullback inside trend.
4. sideways chop.
5. squeeze / coil.
6. squeeze release.
7. exhaustion.
8. one-candle spike.
9. genuine reversal.
10. volume disagreement / weak volume.

---

## 21. E Success Criteria

E is considered successful when all of the following hold:

1. sustained trends can remain BULL/BEAR while Momentum independently cools.
2. temporary opposite Fusion does not automatically create directional conflict.
3. genuine reversals eventually move Price Core through hysteresis and change Trend State.
4. Trend Carrier does not remain stale indefinitely after real reversal.
5. OBV Flow cannot create direction by itself.
6. Flow confirmation/opposition changes trust modestly rather than dominating.
7. missing volume does not break TDI.
8. HTF remains context-only.
9. ACW receives Direction, Momentum, Flow and Timing as separate meanings.
10. premium sync still requires timing permission.
11. `RECOVERY ↑` / `PULLBACK ↓` remain coherent.
12. ACW HUD remains compact on Android.
13. ACW HUD values are readable in white text over colored cells.
14. bullish zigzag is clearly visible on a light chart background without neon glare.
15. TDI/ACW bridge remains one manual source connection.
16. no new Pine plot-count failure is introduced.
17. no illegal series-length behavior is introduced.
18. BTC and ETH both show coherent behavior before E is considered stable.

---

## 22. Versioning and Freeze Rule

First implementation pair:

- `TDI 1e`
- `ACW 1e`

Corrections during E testing use:

- `1e1`
- `1e2`
- etc.

E does **not** advance to F until the Direction / Momentum / Flow / Timing architecture is trustworthy across BTC and ETH.

Once E passes its freeze criteria, F begins the next major roadmap step: multi-timeframe intelligence.

---

## 23. Roadmap Context

- **D** — communication / confluence foundation. Complete.
- **E** — directional intelligence. This specification.
- **F** — multi-timeframe intelligence.
- **G** — final calibration / production freeze.

The project should stop at G unless later real-world testing exposes a genuinely new problem.

---

## 24. Design Summary

E changes the conceptual model from:

`TDI Fusion ≈ direction + momentum + timing`

into:

`Trend Carrier = persistent local direction`

`Momentum Fusion = acceleration / cooling / pullback phase`

`OBV Flow = participation confirmation / opposition`

`Regime + Ready = timing permission`

ACW then combines these distinct meanings without double-counting them.

This design is intended to preserve the useful caution of TDI while eliminating the misleading behavior where a strong persistent trend is repeatedly shown as `MIXED / CHOP` merely because oscillator momentum has cooled.
