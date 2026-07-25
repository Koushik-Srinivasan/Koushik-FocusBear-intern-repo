# Help Strategy

## Research: best practices for troubleshooting

Before jumping to a fix, it helps to actually understand the error first, reading the message properly rather than skimming it, checking what line and what state the program was in, and trying to reproduce it reliably. A lot of the standard advice comes down to isolating the problem (does it happen with smaller input, does it happen every time), checking recent changes first since bugs are usually introduced by whatever changed last, and only then searching or asking, once you can actually describe what's wrong rather than just "it's broken".

I also spent time talking through this with an AI chat tool specifically about when AI is and isn't a good fit for coding help. The useful parts of that conversation: AI tools are strong for explaining unfamiliar concepts, generating a first draft or boilerplate, and rubber-duck style reasoning through a problem out loud. They're weaker when the problem depends on context the AI can't see, like the actual internal codebase, environment specific bugs, or anything involving real company data, and they can confidently produce answers that sound right but are subtly wrong, so anything AI suggests still needs to be checked rather than trusted outright.

## Decision framework

I mapped this out as a flowchart (exported as `help_decision_framework.svg` in this repo) covering the three factors from the task: complexity, sensitivity, and urgency.

The logic in short: if the problem involves sensitive or company specific information, go straight to a colleague rather than pasting it into an external tool. If it doesn't, and it's a common or well documented issue like a syntax error or known bug, Google or the official docs are usually fastest. If it's not something with a quick documented answer but needs actual reasoning, explanation, or a first draft, an AI tool is a good fit. If none of that resolves it, or the problem is genuinely complex or time sensitive, that's when it's worth pulling in a colleague directly rather than continuing to search alone.

## Reflection

**When do I prefer using AI vs. searching Google?**

It really depends on the type of problem rather than one being a fixed first choice. For something that's a known, well documented issue, like a specific error message or a syntax question, Google or the official docs tend to get me a precise answer faster. For something that needs actual reasoning, an explanation of a new concept, or a first draft of something I'd otherwise write from scratch, AI is more useful since it can respond to my specific context rather than giving a generic result.

**How do I decide when to ask a colleague instead?**

Two triggers: if the problem touches anything sensitive or company specific that shouldn't go into an external tool, that goes straight to a colleague, no search or AI step first. Otherwise, if I've already tried searching and an AI tool and I'm still stuck, or the problem is genuinely complex or time sensitive, that's when it's worth asking directly rather than continuing to dig alone.

**What challenges do developers face when troubleshooting alone?**

The biggest one is not knowing when to stop and ask, it's easy to keep trying variations of the same fix for far longer than is actually productive, especially when you're new and don't yet have a good sense of what's "normal" difficulty versus a genuinely tricky bug. There's also a risk of tunnel vision, getting so focused on one theory about the cause that you stop questioning whether the actual problem is somewhere else entirely. Having a clear framework like this one helps put a boundary on how long to search alone before switching approach.
