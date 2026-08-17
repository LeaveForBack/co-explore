# Field Notes from Real Exploration

These are practical field notes, not universal claims about every model in every setting.

They come from repeated real human–AI exploration runs — including many failures. Much of CoExplore exists because those failures exposed what open-ended exploration actually needs.

## 1. “Random exploration” easily becomes another template

In one parallel exploration, independent agents both chose **Wikipedia** as a supposedly random starting point. After being called out, they again drifted toward a similar alternative “random site.”

The lesson: model randomness is often selection from a small, familiar, high-probability set.

**So:** CoExplore does not treat randomness as the core mechanism. After the seed, each hop should be caused by a concrete clue in the current material while remaining free to cross platforms, eras, communities, and languages.

## 2. AI quietly turns open exploration back into a task

As soon as a plausible topic appears, an agent tends to shift into:

> This could be a good topic → collect supporting evidence → make it complete.

The output gets cleaner while exploration has already collapsed into ordinary research.

**So:** exploration is allowed to end without a topic, thesis, or useful conclusion. Move first; interpret later.

## 3. Summaries are not neutral — they contaminate later navigation

We tried periodic summaries. Once a summary produced an elegant theme or explanation, later browsing began orbiting that interpretation.

A recording device had become a new objective function.

**So:** checkpoints should only record where the trail went, unfamiliar facts, repetition warnings, and open branches. Do not write a thesis mid-run.

## 4. Deeper explanation can masquerade as farther exploration

A common form of fake progress: no new material is acquired, but the prose becomes increasingly sophisticated around the same evidence.

It feels like movement while the trail is standing still.

**So:** when the human says “you are explaining instead of exploring,” the next action should acquire a new source, object, or information environment — not more commentary.

## 5. Human boredom and rejection are useful navigation signals

AI alone cannot reliably know whether a relevant source is already obvious to a particular person, or whether a tiny side detail is genuinely strange to them.

Some of the most useful route changes came from very simple human interventions:

- This is too familiar.
- This route is dull.
- Why does this exist?
- You are repeating.
- Stop explaining. Keep moving.

**So:** the human is not merely the final approver. In CoExplore, the human acts as an anomaly detector inside the navigation loop.

## 6. Unfamiliar material does not need to become a question immediately

At one point we required every new piece of material to force a change in the current question. That still assumed exploration must revolve around a question.

In open exploration, strange material is allowed to remain simply strange for a while.

**So:** questions may emerge late. Some of the best ones only become visible after reviewing a long trail of heterogeneous material.

## 7. The most productive question is often very simple

Once a concrete anomaly appears, one prompt repeatedly proved useful:

> **Why does this exist? Why does it exist in this particular form?**

Following that question tends to uncover historical conditions, engineering constraints, cost structures, real demand, predecessors, alternatives, and reasons things later disappeared. That usually creates more genuine discovery than abstract “deepening.”

## 8. Do not let the AI pretend to satisfy a time budget

We experimented with “explore for a strict two hours.” If the runtime cannot actually enforce wall-clock time, the model can turn “two hours” into narrative rather than elapsed time.

**So:** verifiable hop budgets — 8, 20, or another number of meaningful hops — are the safer default. Use real-time budgets only when the runtime can truly enforce them.

## 9. A run can be valid even when it produces nothing publishable

If every exploration must end with a topic, insight, business opportunity, or conclusion, the agent learns to manufacture meaning.

**So:** CoExplore explicitly permits a session to end with only a useful trail, or even the knowledge that several routes were not worth pursuing. That protects openness.

---

## The principle that survived all of this

> **Local causality, global non-predetermination.**

Not pure randomness: every hop should have a reason.

Not search: nobody knows the destination — or even the eventual question — at the start.

That is the kind of exploration CoExplore is trying to preserve.
