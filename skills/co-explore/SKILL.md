---
name: co-explore
description: Human-AI open-ended exploration for moving beyond familiar information paths and discovering unknown unknowns. Use when the user wants to explore without a fixed research question, break an information bubble, find unfamiliar materials, generate better questions, or investigate a vague anomaly. Do not use for straightforward lookup, exhaustive review, urgent troubleshooting, or high-stakes decisions.
license: MIT
compatibility: Works best with web browsing or a user-supplied source collection; uses no vendor-specific runtime features.
metadata:
  version: "0.1.0"
  language: en
  project: co-explore
---

# CoExplore

Help the human and AI leave their familiar information paths together.

## First principle

**Local causality, global non-predetermination.**

Every next hop must come from a concrete detail in the current material. Do not choose the destination, topic or conclusion in advance.

## Division of labor

- AI expands reach through browsing, translation, cross-domain movement, memory and trail capture.
- The human detects meaningful strangeness, rejects repetition, redirects attention and decides what feels worth following.
- Neither side is the sole navigator. Treat human interventions as route-changing evidence, not merely approval.

## Start the session

Establish:

- a concrete seed;
- a budget in time or meaningful hops;
- a checkpoint cadence;
- a mode: `guided`, `relay`, `timed`, or `comparison`;
- explicit non-goals, especially “do not force a topic or final answer.”

If the user gives no seed, select one concrete, unfamiliar item from an available heterogeneous public feed or supplied collection and disclose how it was selected. Do not default to Wikipedia, a random-site ritual, or an AI-news feed.

If browsing is unavailable, explore only the supplied materials and state that boundary.

## Exploration loop

For each meaningful hop:

1. Inspect the current source before searching elsewhere.
2. Record concrete observations, not only summaries.
3. Identify one or more details that are unfamiliar, anomalous, unexplained or structurally important.
4. Choose the next hop from one of those details.
5. State the causal bridge: “I am following X because the current material contains Y.”
6. Record source, source type, observation, uncertainty, actor and next-hop reason.
7. Continue without turning the trail into a topic prematurely.

Prefer a chain of materially justified hops over either pure randomness or repeated keyword search.

## Route selection order

When several routes are available, prefer:

1. a concrete unknown term, object, role, practice or institution;
2. a fact the current explanation cannot comfortably contain;
3. a source outside the current platform, discipline, language or community;
4. an abandoned, old, marginal or first-hand source;
5. a route explicitly selected by the human's surprise or discomfort.

Do not choose a route merely because it supports the current interpretation.

## Checkpoints

At the agreed cadence, give a brief checkpoint containing only:

- where the trail went;
- the most unfamiliar concrete observations;
- repetition or source-monoculture warnings;
- two to four open routes derived from actual material;
- the human's latest intervention, if any.

Do not convert the checkpoint into a thesis, topic pitch or polished summary. In `timed` or `relay` mode, continue after the checkpoint unless the user asked to choose each route.

## Human interventions

Interpret these as protocol actions:

- “Continue this detail” → follow it even if it is not the most semantically related route.
- “This is familiar” → increase source and semantic distance.
- “You are explaining instead of exploring” → stop synthesis and acquire new material.
- “You are repeating” → change platform, source type, language, discipline or community.
- “Drop the topic” → discard the current framing without defending it.
- “Why does this exist?” → trace historical conditions, engineering constraints, costs, demand and predecessors.

## Resist these failure modes

- premature convergence;
- semantic attractors;
- source monoculture;
- explanation substituting for discovery;
- hidden objective smuggling;
- checkpoint summaries contaminating later navigation;
- fake randomness;
- mechanical “opposing viewpoint” selection;
- autonomous-agent theater that removes the human from co-exploration.

Read `references/failure-modes.md` when one of these appears.

## Provenance and uncertainty

Preserve source titles and URLs where available. Separate:

- **observation:** directly present in the material;
- **inference:** a connection drawn from observations;
- **speculation:** a route worth testing.

Do not interrupt every hop with exhaustive verification, but mark uncertainty. Verify important claims before publication, recommendation or action. Read `references/safety-and-provenance.md` for sensitive or high-stakes material.

## Stop and retrospect

Stop when the agreed budget ends, the user ends the session, or further hops are only repeating existing routes.

Only then produce a retrospective:

1. route map;
2. materials neither side would likely have sought alone;
3. how questions changed, appeared or disappeared;
4. explanations that were discarded or revised;
5. the clearest cognitive shift;
6. unresolved routes worth another session;
7. provenance gaps and claims needing verification.

A valid run may end without a publishable topic or final conclusion.

## Success condition

The run succeeds when the joint system reaches a justified, traceable part of the information environment that the human and AI were both unlikely to seek independently—and can show how it got there.

Use the templates in `templates/` when the user asks to save the session. Use `references/evaluation.md` only after the run; never optimize evaluation scores during exploration.
