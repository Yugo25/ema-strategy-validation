# 200EMA strategy — trend pullback with a structure-break trigger

> Concept-level description. The detailed scoring rubric I use to grade each setup
> (and the thresholds behind it) is kept private; see [Disclosure](#disclosure).

## Idea in one paragraph

Trade in the direction of an established trend, after price has pulled back to the
200EMA, at the moment the pullback's own structure breaks. A real pullback is driven by
counter-trend traders taking positions and profits, which leaves **clear swing highs and
lows**. A line through those swings marks where they are positioned; a close through it
means they have given up, and the impulse is likely to resume.

## Two separate confirmations

| Confirmation | What it answers | Tool |
|---|---|---|
| **Bias** | Which side am I looking for? | 20EMA / 200EMA golden or dead cross |
| **Trend evidence** | Is the market actually trending that way? | **Slope** of the 200EMA on two higher timeframes |

A cross on its own only says where to look. Reviewing early backtests showed that losses
clustered when I traded crosses while the higher-timeframe 200EMA was **flat**: a cross
inside a range is noise. The slope check was added as a separate gate for that reason.

## Rules

**STEP 0 — Higher-timeframe filter (pass/fail).**
The 200EMA on both reference timeframes (30m and 1h for 5m execution; 4h and daily for 1h
execution) must slope in the trade direction. Flat or disagreeing slopes mean no trade.

**STEP 1 — Bias.** 20EMA / 200EMA cross in the trade direction.

**STEP 2 — Pullback.** Price retraces to the 200EMA.

**STEP 3 — Trigger.** A candle **body** closes through a trendline drawn across the
pullback's swing highs (for longs) or swing lows (for shorts). The line is valid only if:

- it connects swings that price **actually reacted to** (two or more, ideally a third touch);
- those swings form a recognisable reversal structure (double top/bottom, head and shoulders);
- it is drawn from pivots that existed **before** the break, never redrawn afterwards.

## What a valid line looks like, and what it doesn't

A drift (slow grind against the trend) or a tight range is **build-up, not a pullback**.
No clear swings form, so a line can be drawn many ways, and its "break" is noise; these
often resolve through the 200EMA, i.e. into the stop.

Practical heuristics:

- If you're tempted to draw the line through the **middle** of a price cluster, skip it.
- If three equally reasonable lines can be drawn, skip it.
- A line price never reacted to is a line *you* imposed, not one the market drew.

## Main failure mode

The setup aims for a **bounce** off the 200EMA. The expensive failure is when that bounce
becomes a **break** of the 200EMA. Warning signs: price squeezed between the 200EMA and the
trendline, or chopping around the 200EMA. The slope filter (context level) catches most of
these, and the line-validity rules (structure level) catch the ones that slip through. A
sloped 200EMA can still produce a cramped flag right after a strong impulse.

## Exits

- **Stop:** beyond the last swing high/low of the pullback.
- **Target:** measured move (N-wave projection) of the prior impulse; it must clear the
  most recent swing high/low.
- **Break-even exit:** close the trade if the EMAs cross back against it.
- Reward-to-risk must fall between 1:1 and 1:3.

## Disclosure

The building blocks here (EMA cross, higher-timeframe trend filter, pullback, trendline
break, measured-move target) are widely known. In practice the result depends on how
consistently they are judged. I grade every candidate setup against a fixed, multi-factor
rubric with numeric thresholds computed from market data. That rubric and its tooling are
not published.
