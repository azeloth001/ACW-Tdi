# ACW ∞ + TDI ∞ 1e4 — Core Sanitation Notes

**Baseline:** ACW 1e3 + TDI 1e3  
**Purpose:** Remove demonstrated mathematical/semantic anomalies before F without introducing F-generation intelligence.

## Intended mathematical behavior change

Only the ACW MACD/EMA Council changes mathematically in 1e4.

The 1e3 ten-vote Council contained two exact duplicate facts:

- `fastMA > slowMA` duplicated `macdLine > 0.0` because `macdLine = fastMA - slowMA`.
- `macdLine > macdSignal` duplicated `macdHist > 0.0` because `macdHist = macdLine - macdSignal`.

1e4 keeps eight unique binary observations with equal authority and re-normalizes the Council to `-100…+100` using `macdVotes * 12.5`. Existing ACW fusion weights remain MAMA 0.45 / MACD 0.35 / Structure 0.20, and downstream thresholds are intentionally not retuned yet.

## Semantic-only changes

- ACW and TDI HUD `CONFIDENCE` / `CONF` presentation is renamed to `QUALITY`.
- HUD quality values are shown as internal 0…100 scores without a `%` suffix; the formulas and TDI bridge field are unchanged.
- TDI's fixed `Higher-TF Context` / `HTF Mode` presentation becomes `Context TF` / `Context Mode`.
- The HUD context row is now `CTX <tf> ↑`, `CTX <tf> =`, or `CTX <tf> ↓` when chart and selected context durations are safely comparable; otherwise it falls back to neutral `CTX <tf>`.
- Context-TF relation is display-only in 1e4 and does not affect Fusion, Quality, regime, readiness, action, or bridge packing.
- Visible version/HUD identity is updated to 1e4 / E4.

## Removed proven-dead variables

ACW: `tdiImpulseReady`, `biasName`, `dashDetail`.

TDI: `biasBull`, `biasBear`, `fastBasisUp`, `fastBasisDn`, `longTimingReady`, `shortTimingReady`, `inExtOS`.

Stored swing timestamps (`lastHighTime`, `lastLowTime`) and `swingEvent` are intentionally preserved for F structure-freshness work.

## Explicitly deferred to F

No MA-Core expansion/contraction intelligence, structure freshness weighting, adaptive MTF ladder, MTF action influence, evidence-family weighting, ADX/new engines, or Signal Audit/TP-SL lab is introduced here.

## Preserved E architecture

TDI Price Core / Trend Carrier, Momentum, OBV Flow, squeeze/chop/exhaustion definitions, readiness and continuation thresholds, 1e3 exhaustion semantics, bridge magic/radices/packing, ACW context-assisted continuation, MAMA/FAMA logic, ZigZag confirmation, and alert semantics are preserved.

## Local verification

The local Python sanitation/regression suite passes all 18 tests. Protected TDI decision expressions and bridge packing match 1e3, ACW bridge decode math is preserved, parser-risk checks pass, and plot/plotshape/fill/bgcolor/alertcondition counts do not increase.

This is **static/local verification only**. TradingView remains the final Pine v6 compile/runtime gate.

## Benchmark protocol before threshold tuning

Compare 1e3 vs 1e4 on the existing stable subjects without changing thresholds: BTC bullish continuation, GOLD bearish continuation, HYPE mixed/continuation/exhaustion, plus one squeeze/chop case. Observe the effect of Council de-duplication first; any later threshold adjustment must be evidence-driven rather than bundled into sanitation.
