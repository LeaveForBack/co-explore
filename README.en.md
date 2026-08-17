# CoExplore

[简体中文](README.md)

## Break the filter bubble with AI — without letting AI become the next bubble.

Search answers **questions you already know how to ask**.  
Recommendation systems show you **more of what you already like**.  
Deep Research digs deeper into **questions you already defined**.

**CoExplore does something else: human and AI leave familiar information paths together and discover things neither side would normally search for — sometimes things neither side knew how to ask about.**

> Not “show me the opposite opinion.” Help me encounter questions, communities, people, and worlds I did not know existed.

---

## No coding? Install it with one message

Copy this **entire message into Codex**:

```text
Install the English CoExplore Skill from this repository as my personal Codex Skill:
https://github.com/LeaveForBack/co-explore

The English Skill is in skills/co-explore.
After installation, confirm that $co-explore is available. If Codex needs a restart, tell me.
```

That's it. **No Git, no terminal, no manual file copying.**

If Codex does not automatically start installation, send:

```text
Use $skill-installer to install skills/co-explore from:
https://github.com/LeaveForBack/co-explore
```

---

## How do I use it?

### 1. Start

Start from a page:

```text
$co-explore
Start here and explore with me:
<paste a URL>

Our goal is to leave our familiar information paths. Do not decide in advance what we are supposed to find, and do not rush to summarize.
```

Start with no topic at all:

```text
$co-explore
I have no fixed goal. Pick any concrete starting point and begin exploring with me.
The starting point does not need to be obscure, interesting, old, weird, or topic-worthy; it only needs to make the first move possible.
Do not preselect a final topic or conclusion.
```

### 2. During exploration, just talk naturally

```text
Follow this detail.
This is too familiar. Go farther.
You are explaining again. Find something new.
Why does this exist?
This route is dull. Change direction.
Don't summarize yet. Keep moving.
```

### 3. Stop and get the exploration result

When you want to stop, say:

```text
End this exploration and give me the final exploration result.

Include:
1. the main path we actually traveled;
2. discoveries we would never have thought to search for at the start;
3. questions that appeared or changed during exploration;
4. prior explanations that concrete material forced us to revise;
5. the most promising unfinished branches;
6. key source links.

Do not manufacture a conclusion just to make the result look complete.
```

### What do you get at the end?

Not an automatically generated article, but a reusable **exploration result**:

- **Path** — where we started and how each meaningful hop led to the next;
- **Unexpected discoveries** — people, communities, rules, objects, or materials we would not normally search for;
- **New questions** — questions that became visible only after exploring;
- **Cognitive shifts** — explanations that were overturned, revised, or became insufficient;
- **Open branches** — the best places to continue next time;
- **Sources** — key pages and materials for review and verification.

If you later want a **story idea, article, research plan, or product opportunity**, ask Codex to transform the completed exploration result afterward. CoExplore does not force that goal onto the exploration itself.

**For your first run, explicitly use `$co-explore`.** Later, Codex may invoke it automatically when your intent matches the Skill.

---

## Who is it for?

| You are… | Use CoExplore to… |
|---|---|
| Creator / independent researcher | Escape repetitive topics and find unfamiliar material |
| Founder / product / strategy practitioner | Move beyond industry consensus and surface non-obvious needs |
| Cross-disciplinary researcher / learner | Leave familiar terminology, sources, and citation networks |
| Agent builder | Study open-ended exploration, curiosity, and premature convergence |
| Curious internet user | Recover the feeling of “I never expected to end up here” |

**Not for:** straightforward fact lookup, exhaustive literature review, urgent troubleshooting, or high-stakes decisions. Search and Deep Research are better tools for those jobs.

---

## Why CoExplore?

Because filter bubbles are not only a human problem.

**The human bubble:** familiar interests, keywords, platforms, communities, and questions.  
**The AI bubble:** high-probability semantic paths, familiar sources, common explanations, and premature synthesis.

If an AI simply “wanders” by itself, it often drifts back toward its own familiar paths. CoExplore is not about outsourcing wandering to an autonomous agent. It is about **human and AI interrupting each other's inertia**:

- AI moves quickly across languages, communities, and domains while preserving the path;
- the human detects genuine strangeness, repetition, and “why does this even exist?” moments;
- either side can redirect the other.

### First principle

> **Local causality, global non-predetermination.**

Every next hop comes from a concrete clue in the material in front of you, so the process is not pure randomness. But the destination, topic, and conclusion are not chosen in advance, so it is not just another search task either.

---

## How is it different?

```text
Search:         I know what to find  → find it
Deep Research:  I know what to ask   → investigate it deeply
Recommendation: I know what I liked  → give me more
CoExplore:      I don't know what I'll discover → explore together
```

A good exploration might look like:

```text
An ordinary concrete page
   ↓ because one detail is not yet understood
A different information environment
   ↓ because a behavior there does not fit the current explanation
An unexpected rule or practice
   ↓ because the material keeps pulling the route elsewhere
Another place you would not have chosen at the start
   ↓
A question you did not know existed when you started
```

**Every hop makes sense locally, while the destination remains unpredictable globally.**

---

## Where did these rules come from?

They were not invented as a polished prompt. They came from repeated human–AI exploration runs and the failures that kept showing up:

- supposedly “random” exploration repeatedly returned to familiar entry points;
- agents formed a topic too early and then started collecting evidence for it;
- polished mid-run summaries contaminated what the agent explored next;
- explanations grew deeper while no genuinely new material was being found;
- an unstated goal — “we must end with a good topic” — quietly returned;
- a human saying “too familiar,” “boring,” or “you are explaining again” often changed the route more effectively than the agent's own plan;
- fixed step counts and checkpoints made the model serve the process instead of the material, so they were removed;
- promoting “unfamiliar, old, marginal, forgotten” as preferences pulled models toward museum-, archive-, and old-web-like seeds, so the seed is no longer asked to be interesting.

See [`field-notes/README.md`](field-notes/README.md) for the full notes. These are practical observations, not universal claims about every model or situation.

---

## What's in the repo?

```text
skills/       Installable English and Chinese Skills
field-notes/  Lessons and failure patterns from repeated real exploration
examples/     Minimal usage examples
```

Those are the three core pieces. CoExplore is currently a **practical human–AI co-exploration method**, not a heavyweight research framework.

---

## Core principles

1. **Do not pre-program the exploration cadence.** No fixed step counts, scheduled checkpoints, or staged deliverables; keep moving while material is alive and reroute when a branch dries up.
2. **The seed only needs to make the first move possible.** If the user gives no seed, pick a concrete object or page without curating for obscurity, age, weirdness, or story value.
3. **Let the current material cause the next hop.** Avoid both pure randomness and preset keyword trees.
4. **Delay synthesis.** Observe and move before forcing a topic.
5. **Human and AI interrupt each other.** Either side can break repetition or premature convergence.
6. **Ask “why,” but use it to find material.** Why did this happen, why this person, why does it exist, why this form — use these questions to open the next hop, not to invent explanations in place.
7. **Reflect after exploration ends.** Only then describe what actually changed.

---

## Contributing

What we want most is not prettier prompt wording, but:

- real exploration experiences;
- failure cases;
- repeated model habits;
- multilingual adaptations;
- improvements that help humans and AI genuinely reach farther.

See [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Limits

CoExplore is a **discovery tool**, not a truth engine. Verify important claims independently before publication, investment, medical, legal, or other high-stakes action. Never commit credentials, private browsing histories, or sensitive personal information to the public repository.

## License

[MIT](LICENSE)
