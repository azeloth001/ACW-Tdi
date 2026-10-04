# ACW ∞ + TDI ∞ 1g — TradingView Runtime Validation Matrix

**Generation:** G / 1g  
**Purpose:** Final runtime gate before any production-freeze decision.  
**Important:** Local tests verify semantics and source invariants; they do **not** replace TradingView Pine v6 compilation/runtime validation.

## Setup

1. Add `TDI ∞ Adaptive Spectral Engine 1g — Fusion` and `ACW ∞ Spectral Fusion PRO 1g` to the same normal-candle chart.
2. In ACW, set **TDI Bridge Bus** to `TDI ∞ 1g → TDI Bridge Bus`.
3. Confirm ACW no longer reports `UNLINKED` / `VERSION MISMATCH`.
4. Leave **Signal Personality = Balanced** for the reference pass.
5. Use confirmed/closed candles when judging lifecycle transitions.
6. Run both **Descriptive** and **Compact** HUD checks; Compact must remain readable on Android.

## Core lifecycle checks

| Case | Trigger / observation | Expected 1g behavior | Evidence to capture |
| --- | --- | --- | --- |
| Entry | A real ACW `READY` episode begins | Exactly one `A↑` or `A↓` marker on the first confirmed READY bar; lifecycle becomes ACTIVE | Screenshot including marker + HUD |
| Signal age | ACTIVE remains valid for several bars | Descriptive HUD increments `LONG/SHORT ACTIVE • N bars`; `ENTRY EVENT` reports A marker age | Screenshot after 2+ bars |
| Persistent READY | READY remains true across consecutive bars | No repeated A marker spam | Screenshot covering full READY stretch |
| Soft deterioration | READY/ACTIVE weakens with one warning | CAUTION may appear; no automatic X from a lone weak warning | Screenshot if available |
| Recovery | CAUTION warning clears without terminal failure | Returns to ACTIVE without a new A marker | Screenshot if available |
| Exit | Strong exhaustion, corroborated fresh opposing divergence, or sufficient deterioration | One `X`; lifecycle ends; thesis need not have reversed | Screenshot + reason in HUD |
| Invalidation | Two directional authorities flip, or opposite READY + one authority flip | One `INV`; no same-bar opposite A | Screenshot only if a genuine flip occurs |
| Re-arm | After X/INV | Same direction must spend two confirmed bars not READY before a later READY transition can create a new A | Sequence screenshot if practical |

## Personality checks — same chart, same bars

Switch **Selective → Balanced → Active** without changing other settings.

- Market-state meanings must remain identical: structure, MA Core, TDI Trend Carrier, momentum state, Near/Anchor context, divergence state, exhaustion state.
- Only promotion cadence may change.
- **Selective:** may demote marginal Balanced READY to WATCH; must not promote WATCH/WAIT.
- **Balanced:** reference behavior; intended default.
- **Active:** may promote eligible WATCH earlier, but must not bypass squeeze, strong exhaustion, severe conflict, or corroborated fresh opposing divergence.
- Historical A markers may differ between personalities because each preset has its own promotion history; the underlying market-state labels must not.

## BTC museum pass — compression / mixed MTF

Use a BTC section similar to the F1.3 screenshots where lower TFs rebound while medium TFs are compressed or mixed and higher anchors disagree.

Expected:
- Genuine squeeze/compression remains `WAIT • MARKET COMPRESSED` or equivalent.
- Active must **not** manufacture an A marker inside a hard squeeze.
- Mixed local-vs-Anchor context remains visible rather than being flattened into one direction.
- A local continuation may become actionable only after hard blocks clear.

Suggested TF sweep: **1m, 3m, 5m, 7m, 15m, 45m, 1h, 2h, 4h, 6h**.

## GOLD museum pass — divergence / Flow N/A / continuation

Use XAUUSD where volume is unavailable or unreliable and where a fresh divergence is visible.

Expected:
- HUD explicitly shows `FLOW N/A`; missing Flow contributes no lifecycle deterioration vote.
- Fresh opposing divergence is a risk/timing modifier, not an automatic reversal signal.
- Older plotted divergence may remain visible while no longer being ACTIVE risk.
- Clean higher-TF/local continuation can still become WATCH/READY when other evidence supports it.
- A corroborated fresh opposing divergence can produce X without falsely producing INV.

Suggested TF sweep: **1m, 3m, 5m, 7m, 15m, 45m, 1h, 2h, 4h, 6h**.

## HYPE museum pass — counter-Anchor / Flow opposition / exhaustion

Use HYPE where local direction can conflict with broader bullish/bearish context and Flow can oppose price.

Expected:
- `ANCHOR OPPOSES` and `FLOW OPPOSES` remain visible risk facts.
- Active may be more responsive, but cannot bypass strong exhaustion or severe context conflict.
- Selective can demand cleaner agreement without changing the displayed market state.
- A mature exhaustion case should demonstrate `TREND TIRED/CAUTION` before `X` when the evidence sequence permits it; strong exhaustion may go directly to X if already corroborated.
- Countertrend classification must remain descriptive rather than silently relabeled as normal continuation.

## HUD / mobile pass

### Descriptive
Confirm readable plain-language rows:
- `TRADE STATE`
- `ENTRY EVENT`
- `LONG ACTIVE • N bars` / `SHORT ACTIVE • N bars`
- `CAUTION • <reason>`
- `EXIT • <reason>` on the terminal bar
- `INVALIDATED • TREND FLIPPED` on a genuine invalidation bar
- directional Flow wording such as `BULL FLOW SUPPORTS 24`, `BEAR FLOW SUPPORTS 30`, `FLOW OPPOSES 18`, `FLOW N/A`

### Compact
Confirm the panel stays short and legible on Android:
- `L ACTIVE +Nb` / `S ACTIVE +Nb`
- `L ! <reason>` / `S ! <reason>`
- `EXIT`
- `INV`

## Acceptance gate

G may be called **production-frozen** only after:

1. Both scripts compile in TradingView Pine v6.
2. The TDI→ACW bridge links correctly.
3. BTC, GOLD, and HYPE passes show no semantic regression in the frozen F architecture.
4. At least one real A event is observed with correct age/no-spam behavior.
5. Exit/caution behavior is observed where the market naturally supplies it; INV is required only when a genuine directional invalidation occurs.
6. Selective/Balanced/Active alter promotion cadence only.
7. The user accepts the chart/HUD behavior.

If a reproducible defect appears, capture the symbol, timeframe, candle/time, personality, screenshot, and expected vs actual state. Fix it as a new test-first calibration rather than loosening the G invariants.
