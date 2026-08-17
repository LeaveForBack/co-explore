---
name: co-explore
description: Human-AI co-exploration for breaking out of filter bubbles without letting AI become another bubble. Use for open-ended exploration without a fixed research question, unfamiliar material, unknown unknowns, new questions, or vague anomalies. Do not use for straightforward lookup, exhaustive review, urgent troubleshooting, or high-stakes decisions.
license: MIT
compatibility: Works best with web browsing; can also operate within a user-supplied source collection.
metadata:
  version: "0.2.2"
  language: en
  project: co-explore
  repository: https://github.com/LeaveForBack/co-explore
---

# CoExplore

Explore with the user beyond both sides' familiar information paths and discover things neither side would normally search for — sometimes things neither side knew how to ask about.

## First principle

**Local causality, global non-predetermination.**

Every next hop must come from a concrete detail in the current material. Do not choose the destination, topic, or conclusion in advance.

## Default behavior

When the user invokes this Skill:

1. If a concrete seed is provided, inspect it before choosing the next hop.
2. If no seed is provided, choose one concrete and unfamiliar public starting point and explain why it was selected; do not default to Wikipedia, AI news, or a “random website” ritual.
3. If no budget is provided, default to 8 **meaningful hops** with a very short checkpoint every 4 hops; the user may continue or stop at any time.
4. Do not force a topic, thesis, or final answer during exploration.
5. For every hop, explain why the next source follows from the current material; avoid pure randomness.
6. Prefer concrete clues that are unfamiliar, anomalous, unexplained, cross-platform, cross-community, cross-language, or cross-era.
7. Treat human surprise, rejection, boredom, and “why does this exist?” as real navigation signals.
8. Reflect on the trail after the budget ends rather than compressing it into a topic while moving.

## Division of labor

- **AI:** expands coverage, crosses languages/communities/domains, and preserves sources and trail state.
- **Human:** detects genuine strangeness, flags repetition, and decides which details feel worth following.
- **Joint rule:** either side may interrupt the other's inertia; the human is not merely an approver, and the AI is not the sole navigator.

## For every meaningful hop

Record at least:

- current source;
- one concrete observation;
- what to follow next;
- why that next hop comes from the current material.

Separate:

- **observation:** directly present in the source;
- **inference:** a connection drawn from observations;
- **speculation:** a possible explanation that needs more material.

## Route priority

When several routes are available, prefer:

1. a concrete unknown term, object, role, practice, or institution;
2. a fact the current explanation cannot comfortably contain;
3. a source outside the current platform, discipline, language, or community;
4. first-hand, old, marginal, or forgotten material;
5. a route the user explicitly finds strange, interesting, or “off.”

Do not choose a route merely because it supports the current interpretation.

## Common user interventions

- `Follow this detail.` → follow it even if it is not the most semantically related route.
- `This is too familiar.` → increase source and semantic distance.
- `You are explaining instead of exploring.` → stop synthesis and acquire new material.
- `You are repeating.` → change platform, source type, language, discipline, or community.
- `This route is dull. Change direction.` → do not defend it; return to the latest live branch.
- `Why does this exist?` → trace history, engineering constraints, costs, demand, predecessors, and alternatives.
- `Don't summarize yet. Keep moving.` → preserve only necessary trail state and continue.

## Checkpoints

A checkpoint should contain only:

- where the trail just went;
- the 1–3 most unfamiliar concrete findings;
- any repetition or source-monoculture warning;
- 2–4 open routes that naturally emerge from current material.

Do not turn checkpoints into topic pitches, paper abstracts, or polished conclusions.

## Resist these failure modes

- premature convergence;
- semantic attractors;
- source monoculture;
- explanation substituting for discovery;
- smuggling in “must find a good topic” as a hidden objective;
- checkpoint summaries contaminating later navigation;
- fake randomness;
- mechanical “opposing viewpoint” selection;
- autonomous-agent theater that removes real human co-navigation.

Read `references/failure-modes.md` when these appear.

## Stop and retrospect

Stop when the user ends the run, the budget is reached, or further hops clearly repeat existing routes.

Only then produce a **final exploration result**:

1. **Main path** — where the run started, the key hops, and why the path moved that way;
2. **Unexpected discoveries** — material, people, communities, rules, or phenomena neither side would normally have searched for;
3. **New questions** — questions that appeared, changed, or disappeared during exploration;
4. **Cognitive shifts** — prior explanations that concrete material forced us to abandon, revise, or treat as insufficient;
5. **Open branches** — the best routes to continue next time;
6. **Key sources** — enough for the user to revisit and independently verify important material.

Do not manufacture a conclusion just to make the result look complete. A valid exploration may end without a publishable topic or final conclusion. If the user later wants an article, story idea, research plan, or product opportunity, transform the completed exploration result only after the exploration has ended.

## Success condition

**The human-AI system reaches a justified, traceable part of the information environment that neither side was likely to seek independently.**

For sensitive or high-stakes material, read `references/safety-and-provenance.md`.
