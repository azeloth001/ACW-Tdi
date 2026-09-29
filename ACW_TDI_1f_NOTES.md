# ACW + TDI 1f — F Market Interpreter Candidate

## Status

`1f` is the first locally verified F-generation candidate built from the sanitized `1e4` baseline. It has passed the local static/math/interpreter regression suite, but it is **not production-frozen** until both Pine scripts compile and run correctly in TradingView and the BTC/GOLD/HYPE live validation matrix is completed.

## What F adds

F changes the system from a largely score-oriented confluence engine into a semantic market interpreter:

`STRUCTURE → MA CORE → MTF CONTEXT → QUALITY/RISK → READINESS → ACTION`

### ACW-owned intelligence

- **MA Core** from the existing MAMA/FAMA + EMA geometry, with `BULL/BEAR • EXPAND/HOLD/CONTRACT`, plus `COMPRESS` and `FLIP`.
- **Structure Freshness** from the existing confirmed swing event timing: `FRESH`, `MATURE`, `AGING`. Aging never invalidates a confirmed HH/HL or LH/LL structure.
- **Structure relationship** semantics such as confirmed, cooling, reversal pressure, recovery pressure, building, unresolved.
- Final F interpretation and action vocabulary.

### TDI-owned intelligence

- Local Trend Carrier, Momentum, Flow and E timing heritage remain intact.
- **Two-layer MTF Context Spine:** LOCAL + NEAR + ANCHOR.
- Automatic context ladder with manual Near/Anchor overrides.
- Confirmed context is authoritative. `Context Mode = Developing` is a HUD preview only and cannot promote/downgrade ACW readiness in 1f.
- Divergence becomes a **Risk** family with a `FRESH → ACTIVE → EXPIRED` lifecycle instead of being only a drawing/alert.

## Automatic Near / Anchor ladder

- 1m → 3m / 15m
- 3m → 7m / 45m
- 5m–7m → 15m / 45m
- 15m → 45m / 2h
- 30m / 45m / 1h → 2h / 6h
- 2h → 6h / 1D
- 4h / 6h → 1D / 3D
- 1D → 3D / 1W
- 2D–3D → 1W / 1M
- 1W → 1M / 3M

Manual Near and Anchor timeframes remain available for experiments.

## Quality / Risk philosophy

Quality measures the health/coherence of a directional state; it is **not a win probability** and it never creates direction.

Soft penalties are intentionally modest and capped at 20:

- Flow opposes: -6
- fresh opposing divergence: -8
- active opposing divergence: -4
- Near opposes: -4
- Anchor opposes: -4
- structure reversal pressure: -6

Flow N/A has no penalty.

Fresh opposing divergence can downgrade `READY → WATCH` only when another warning corroborates it (for example MA contraction, cooling/pullback momentum, Near disagreement, or aging structure). ACTIVE divergence remains a quality/risk warning only.

Hard readiness semantics remain small:

- SQUEEZE can block fresh impulse timing.
- Same-direction EXHAUSTION blocks chasing that direction.
- Opposite-direction exhaustion does not veto the local action.

## Readiness and action vocabulary

Readiness stays simple: `WAIT / WATCH / READY`.

Action scope is separate:

- `LOCAL` = valid on this chart, but higher context does not fully support it.
- `MTF` = Near + Anchor meaningfully support the local action.

F preserves the important archetypes: `IMPULSE`, `CONT`, `RECOVERY`, `PULLBACK`, `COUNTERTREND`.

Context disagreement normally downgrades **scope before readiness**. A valid local move is not erased merely because Anchor disagrees.

## HUDs — both are mandatory

Both ACW and TDI now expose:

- **Descriptive** — the richer explanatory HUD.
- **Compact** — reduced-height mobile HUD.
- **Diagnostic** — raw/internal research view.

HUD layout and text size are independent. In particular, **Descriptive + Tiny** is supported for phone use.

ACW Descriptive explains: PROFILE, STRUCTURE + freshness, MA CORE, CONTEXT, TDI, QUALITY + Flow, RISK, ACTION.

ACW Compact explains the same market using: STR, MA, CTX, TDI, QLTY, RISK, ACT.

TDI Descriptive shows Trend, Momentum, Flow, Near, Anchor, Quality, Risk, Regime/Timing and Action. TDI Compact condenses this into Trend, CTX, Mom/Flow, Quality/Risk and Action/Timing.

## F bridge

F still uses exactly **one hidden `TDI Bridge Bus` plot**. It carries evidence rather than final ACW conclusions.

F has 15 packed fields: local Trend score/state, Momentum, Flow, Quality, Regime, readiness, signal, Near state/score, Anchor state/score, divergence direction/freshness, and hard-risk direction.

### Version safety

The approved positive F envelope overlapped the historical E4 positive numeric range. To make version mismatch exact rather than heuristic, F transmits its bus using a **negative envelope**:

`bridgeBus = -(F_MAGIC + payload)`

E4 buses are positive, normal price sources are ordinary-sized, and F buses are negative. ACW can therefore report **TDI VERSION MISMATCH** instead of silently decoding an E4 source as F.

### Exact-float budget

Mixed-radix product: `4,958,740,783,038,420`

Maximum F bus magnitude: `5,958,740,783,038,419`

IEEE-754 / Pine exact-integer boundary: `2^53 = 9,007,199,254,740,992`

So the packed integer remains inside the exact range.

To fit 15 evidence fields while preserving exact packing, bridge transport uses these deliberate quantizers:

- Trend / Momentum: integer score points
- Flow: 5-point steps (plus N/A code)
- Quality: integer score points
- Near / Anchor scores: 10-point steps

This affects **transport precision only**. TDI's local calculations and HUD retain full internal precision. Small ACW/TDI displayed differences near quantization boundaries are therefore expected and should not be mistaken for local TDI calculation changes.

## Protected 1e4 heritage

The F work deliberately did not retune the verified E thresholds/engines. Static regression checks preserve the existing Price Core, Flow, Trend Carrier, Fusion, Quality, regime, impulse readiness, continuation thresholds (`55` hard continuation / `32` medium watch), ACW fusion weights (`45/35/20`), E continuation promotion, and E action/confluence expressions.

Existing legacy plotted signal/alert registrations are also preserved in this candidate. F's semantic `ACTION` is being live-validated first; migrating alert semantics to F actions, if desired, should be a separate bounded decision after validation rather than a silent behavior change.

## Local verification

Fresh final local result:

- `pytest`: **35/35 passed**
- `unittest`: **35/35 passed**
- render registration budget unchanged from 1e4
- exactly one hidden bridge plot
- parser-risk scan: no bare assignment continuation and no trailing multiline ternary hazards
- confirmed/developing context patterns verified
- F bridge round-trip and `2^53` bound verified
- wrong E4 bridge range is distinguishable from F

Local checks are **not** a TradingView Pine compiler/runtime substitute.

## TradingView validation matrix

1. Compile `TDI_1f.pine` and `ACW_1f.pine` as Pine v6.
2. In ACW, reconnect the TDI source to **TDI 1f → TDI Bridge Bus**.
3. Check both HUDs on Android: **Descriptive + Tiny** and **Compact + Tiny**.
4. Deliberately select an E4 bus once and verify ACW visibly reports **VERSION MISMATCH**.
5. BTC: 1m / 3m / 15m / 45m / 2h / 6h.
6. GOLD: 3m / 15m / 45m / 1h / 2h / 6h, especially Flow N/A and EXHAUST cases.
7. HYPE: 1m / 3m / 5m / 45m / 1h / 2h / 4h / 6h, especially LOCAL-vs-Anchor conflict.
8. Capture one fresh divergence case and verify it appears as Risk without directly flipping the trend.
9. Switch TDI context to Developing and verify it previews faster context in TDI while ACW's decision remains based on confirmed context.

Recommended starting display for the first live pass: **Descriptive + Tiny** on both indicators. Once semantics are trusted, compare the Compact mobile layout.
