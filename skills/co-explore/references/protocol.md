# Co-exploration protocol

## Session contract

Record five settings before movement begins:

| Field | Meaning |
|---|---|
| Seed | The concrete material from which the first hop starts |
| Budget | Minutes or meaningful hops, not a promise of future background work |
| Checkpoint cadence | How often human and AI inspect the route |
| Mode | Guided, relay, timed or comparison |
| Non-goals | What must not be forced, such as a topic, article or business answer |

A meaningful hop changes source, object of attention or information environment. Scrolling the same page, paraphrasing or running a nearly identical query does not count.

## Modes

### Guided

Pause at every checkpoint for human route selection. Best for early method learning and strong human curiosity signals.

### Relay

The AI explores for a fixed number of hops, reports a checkpoint, then continues unless redirected. Best for longer sessions where the human wants steering without micromanagement.

### Timed

The session follows an explicit real-time boundary when the environment can observe time. If it cannot, use a step budget and say so. Never claim to have explored for elapsed time that was not actually observed.

### Comparison

Run the same seed and budget in separate arms: human-only, AI-only and human+AI. Keep arms independent until evaluation.

## Trail record

Each step should include:

- step number and timestamp;
- actor choosing the hop;
- source title, URL and source type;
- concrete observation;
- what is unfamiliar or difficult to explain;
- next-hop reason;
- observation/inference/speculation label;
- uncertainty note.

The route is the product during exploration. Preserve failed and abandoned branches when they explain later movement.

## Source diversification

Change information environment when the trail repeats. Useful dimensions include:

- platform;
- source type;
- language;
- discipline;
- historical period;
- community position;
- official versus first-hand versus adversarial source;
- current versus archived material.

Diversification is not a quota. A source change must still be causally connected to current material.

## Checkpoint discipline

A checkpoint must not name a final topic. It should answer:

1. What concrete route occurred?
2. What genuinely unfamiliar material appeared?
3. Where is the trail repeating or narrowing?
4. Which routes remain open because of observed details?
5. What human reaction should change the next segment?

## Retrospective discipline

Retrospective pattern discovery is allowed only after the stop condition. Review the trail from the beginning rather than polishing the last interpretation. Look for discontinuities, discarded explanations and moments when the human or AI changed the other side's route.
