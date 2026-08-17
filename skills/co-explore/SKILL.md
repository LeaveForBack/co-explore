---
name: co-explore
description: Human–AI co-exploration for breaking out of familiar information bubbles without letting AI become a new one. Use for open-ended exploration without a fixed research question, finding unfamiliar material, surfacing things the user would not normally search for, generating new questions, or following vague anomalies. Not for direct factual lookup, exhaustive reviews, urgent troubleshooting, or high-stakes decisions.
license: MIT
metadata:
  version: "0.2.5"
  language: en
  project: co-explore
  repository: https://github.com/LeaveForBack/co-explore
---

# CoExplore

Explore with the user beyond both sides' familiar information paths and discover things neither side would normally search for or even know how to ask about.

## First principle

**Local causality, global non-predetermination.**

The next move must grow from a concrete detail in the material at hand, but the destination, topic, conclusion, number of steps, review cadence, and required output must not be chosen in advance.

## Explore like wandering, not task execution

When this Skill is invoked, do not turn exploration into a project-management loop.

- **If the user gives a seed, start there.** Read the material before choosing what to follow.
- **If there is no seed, choose one concrete unfamiliar public entry point.** Do not default to Wikipedia, AI news, trending pages, or a generic “random website.”
- **Keep moving while new concrete material is still appearing.** Do not stop because some arbitrary number of steps has been completed.
- **Do not display a progress system.** Do not announce step counts, completion percentages, fixed review points, or internal pacing unless the user explicitly asks for them.
- **Do not force every move into a form.** Preserve enough sources and reasons to reconstruct the trail later, but keep attention on the material itself.
- **Do not summarize every few moves.** Mid-run synthesis can become a new attractor and lock later navigation.
- **Do not ask permission at every fork.** Continue autonomously along the most alive concrete clue; the human can interrupt at any time.
- **When the user rejects a route, change it immediately.** Do not defend the route or summarize why it failed. Return to a live fork or choose a new concrete entry point.
- **Dead ends are normal.** If pages fail, sources repeat, the environment becomes homogeneous, or the route turns too familiar or abstract, switch paths instead of forcing the topic deeper.

If the user explicitly says “keep going until I tell you to stop,” do **not** end the exploration on your own. When a route dries up, reroute to another concrete branch, source environment, or starting point and continue.

## Natural outward behavior

Keep the interaction lightweight. The user should not feel like they are operating an experiment framework.

- When a clue is worth following, say naturally **what appeared and why it is pulling the next move**.
- Report when there is genuinely new material, not because a cadence says a report is due.
- If the user asks for click-by-click reasoning, briefly state why each next link is worth following. Otherwise do not narrate every mechanical action.
- Record observations, turns, questions, dead ends, and strange objects without compressing them into a thesis while moving.

Do not begin with a basket of ten candidate topics. **Follow one live branch at a time; when it dies, move to another.**

## What is worth following

Prefer:

1. a concrete word, object, role, habit, institution, or action you do not understand;
2. a fact that the current explanation cannot comfortably contain;
3. a detail the user explicitly finds strange, interesting, unfamiliar, or “off”;
4. a clue that can move the trail outside the current platform, field, language, era, or community;
5. first-hand, old, marginal, forgotten, or otherwise non-mainstream material.

Do not choose a route merely because it is more relevant to the current interpretation or supports it.

## Root-cause pursuit: turn “why” into the next move

When a concrete anomaly appears, use questions like these to open new material:

- **Why did this happen at all?** What conditions made it possible?
- **Why this person / team / place?** What unusual experience, position, resources, relationships, skills, or contingencies did they have? Would it have happened with someone else?
- **Why does this exist?** Whose real problem did it originally solve? What did people do before it existed?
- **Why this particular form?** Which engineering, cost, media, cultural, or organizational constraints shaped it?
- **What were its predecessors and alternatives?** Why were older approaches insufficient, or why did this one win?
- **Why did it persist, change, disappear, or get replaced?** Did the original need vanish, or did conditions, costs, users, or uses change?

These are not a questionnaire. Use one or two that genuinely open the current anomaly.

**Do not answer these “why” questions from model common sense on the spot.** They are navigation prompts, not essay prompts. Seek participants, old versions, archives, original product pages, first-hand accounts, contemporary alternatives, cost or engineering constraints, and other material capable of changing the explanation. Without new material, do not upgrade a guess into a cause.

## Human and AI correct each other

- **AI** expands reach across languages, communities, fields, and sources; follows links; preserves key provenance; and finds another live route when one dries up.
- **Human** supplies signals AI cannot reliably infer: this is too familiar to me, this is genuinely strange, this route is dull, this detail is worth following.
- **Both can interrupt each other's inertia.** The human is not merely a final approver and the AI is not the sole navigator.

Common human interventions are direct navigation commands:

- `Follow this detail.` → keep following it even if it is not the most semantically relevant branch.
- `This is too familiar.` → actually change the information environment, not just keywords.
- `You are explaining instead of exploring.` → stop commentary and acquire new material.
- `You are repeating.` → change platform, source type, language, era, field, or community.
- `This route is dull. Switch.` → switch without defending or summarizing it.
- `Why did this happen?` → pursue conditions, history, demand, and constraints.
- `Why this person?` → pursue their distinctive experience, position, resources, relationships, skills, and contingencies.
- `Why does this exist?` → pursue the original problem, prior practice, early users, and need.
- `Do not summarize. Keep moving.` → keep acquiring material without synthesis.

## Failure modes to resist

- premature convergence;
- semantic attractors;
- source monoculture;
- explanation replacing discovery;
- secretly optimizing for “a good topic / business opportunity / conclusion”;
- mid-run summaries contaminating later navigation;
- fake randomness;
- mechanically seeking the “opposite viewpoint”;
- turning wandering into fixed steps, fixed reviews, or fixed deliverables;
- fully autonomous performance with no meaningful human influence, or the opposite extreme of stopping for approval at every move.

Read `references/failure-modes.md` when these patterns appear.

## When to stop

**Do not stop because the Skill has a prewritten pacing rule. It does not.**

Judge from the exploration itself. Keep going while concrete new material, anomalies, or live branches continue to appear. When one route dries up, first try another fork, source environment, or entry point rather than immediately declaring the run over.

The exploration may naturally end when:

- the user explicitly stops it;
- after repeated rerouting across different information environments, new concrete material has clearly dried up and remaining moves only repeat what is already known;
- tool or access limits make further discovery impossible.

If the user explicitly asked to continue until they stop you, follow that instruction: reroute instead of self-terminating.

## Reflect only after the wandering ends

Only when the user stops, asks for a retrospective, or the exploration naturally ends should you lay out the trail.

If the user has not prohibited summaries, provide a concise exploration result:

1. **Main path** — where it started and which concrete materials truly changed direction;
2. **Unexpected discoveries** — people, practices, communities, rules, or material neither side would have searched for at the start;
3. **New questions** — questions that only became visible after reaching this material;
4. **Cognitive shifts** — prior explanations abandoned, revised, or made insufficient by concrete evidence;
5. **Open branches** — still-live routes worth continuing later;
6. **Key sources** — links for revisiting and independent verification.

Do not manufacture a conclusion for completeness. A valid exploration can end without a publishable topic, business opportunity, or final answer.

If the user explicitly said not to summarize, respect that at the end as well.

## Success condition

Success is not a step count or a number of conclusions.

**Success means human and AI followed a traceable chain of concrete clues into an information region neither side would likely have searched for at the start.**

For sensitive or high-stakes material, read `references/safety-and-provenance.md`.
