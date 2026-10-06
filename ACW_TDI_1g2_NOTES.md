# ACW ∞ 1g2 Market Phase Context — Runtime Candidate

## Purpose

G2 adds larger-swing awareness without changing the TDI bridge or the established G lifecycle. ACW now estimates where price sits inside the currently developing confirmed swing leg and uses that context in two ways:

- **Earlier observation:** `A?↑ / A?↓` can appear when a mature prior leg is recovering and at least the required number of independent evidence families agree. `A?` is lower certainty, confirmed-bar only, and is not counted as a trade.
- **Late-chase protection:** a fresh normal `READY` can be downgraded to `WATCH • LATE MOVE` / `WATCH • NEAR PRIOR HIGH/LOW` when the move is already mature/retesting **and** weakness corroborates it. Strong expanding breakouts are not blocked by location alone.

## Market Phase vocabulary

- `EARLY LEG ↑/↓`
- `MID LEG ↑/↓`
- `LATE LEG ↑/↓`
- `NEAR PRIOR HIGH/LOW`
- `EARLY RECOVERY ↑/↓ • A?`

Balanced remains the default Signal Personality. Selective requires stronger early evidence and protects from late chasing sooner; Active allows earlier observations and tolerates later continuation longer.

## Signal lifecycle

The confirmed lifecycle stays:

`READY → A → ACTIVE → CAUTION → X / INV → RE-ARM`

G2 adds an earlier observation doorway:

`A? → A` when full G confirmation later arrives in the same direction.

`A?` never owns the confirmed entry price, never gets the dotted trade connector, and never enters confirmed trade accounting.

## Presentation changes

- A/A?/X/INV labels are anchored at the exact event price; numerical entry/exit price is **not printed inside the label**.
- Lifecycle label fills target ~50% transparency.
- Completed X/INV labels show direction-normalized **price movement**, e.g. `X +$624` or `INV -$137` for USD-like quote currencies.
- The dotted confirmed `A → X/INV` connector remains.
- Descriptive HUD adds `MARKET PHASE`.
- Active ENTRY EVENT shows signal + age, not printed entry price.
- LAST TRADE shows terminal type + move + bars.

## Frozen invariants

- ACW adds **0** new `request.security()` calls.
- TDI 1g is unchanged; SHA256: `17c3a59a392d021178912be98924e765bd97950443fb430ba26d64e7a32598e6`.
- TDI bridge decoder block is unchanged.
- Existing X/INV terminal authority is unchanged by Market Phase.
- G2 adds no lifecycle `plotshape()` and no new `alertcondition()` registrations.
- A? optional notifications use `alert()` only and are OFF by default.

## Local verification

Python behavioral/static regression suite plus a static Pine sanity pass are used locally. TradingView compilation and real-chart runtime remain the final gate.

## Final self-review corrections

- The A? MTF evidence family counts only when at least one of Near/Anchor supports the candidate **and neither context opposes it**. A mixed support/opposition pair no longer earns the context-family vote.
- If a full confirmed `A` is earned on the same confirmed bar as an early `A?`, the lower-certainty `A?` marker/alert is suppressed. The chart records only the full-confidence event on that bar.
