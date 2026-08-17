# Minimal example: from start to a usable result

**User starts:**

```text
$co-explore
I have no fixed goal. Pick a concrete unfamiliar starting point and explore with me. Do not rush to summarize.
```

**During exploration, the user can simply say:**

```text
Follow this detail.
This is too familiar. Go farther.
You are explaining again. Find something new.
Why does this exist?
```

**The AI should:**

1. provide one concrete seed and explain why it starts there;
2. inspect the material before choosing the next hop;
3. explain the reason for every hop;
4. give only a tiny checkpoint after 4 meaningful hops;
5. actually change information environments when the user says “this is too familiar,” rather than merely changing keywords;
6. by default, stop and reflect after 8 meaningful hops unless the user continues or ends earlier.

**User ends:**

```text
End this exploration and give me the final exploration result.
```

**The final result should contain:**

- **Main path** — the important hops and why the route moved that way;
- **Unexpected discoveries** — things neither side would have thought to search for at the start;
- **New questions** — questions that became visible only after reaching this material;
- **Cognitive shifts** — prior explanations changed by concrete evidence;
- **Open branches** — the best routes to continue next time;
- **Key sources** — links for revisiting and verification.

It is completely fine if the run ends without a neat conclusion. CoExplore is meant to discover things you did not know to look for, not to force every session into a “good topic.”

**The AI should not:**

- begin with ten “research directions”;
- name a topic as soon as something interesting appears;
- replace new material with increasingly polished explanation;
- turn “break the bubble” into “find the opposite viewpoint”;
- pretend to be random while repeatedly starting from familiar sites.
