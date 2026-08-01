# Get to Know the Focus Bear Product

## Task: help centre and onboarding research

I went through the Focus Bear knowledge base (support.focusbear.io) and the product's public materials to build a working understanding of the app.

## 3-5 things about how the app works, relevant to a Data Analyst role

1. **Cross device blocking, one config applies everywhere.** Starting a focus block on one device (say desktop) applies the same block across Mac, Windows, iOS, and Android automatically. For analytics, this means usage data isn't per-device in isolation, a single user's session could legitimately span devices, which matters for how session/usage data should be joined or deduplicated.

2. **No keystroke logging or screenshots, only "what app/site is in focus."** Focus Bear explicitly does not capture keystrokes or take screenshots, it only tracks which app or website is currently in focus to decide whether to block it. This is a hard privacy boundary worth knowing before ever touching real usage data, the granularity available is "time in app/site," not content.

3. **The Time Tracker feature (Windows) records app usage, website URLs, and even separate Google profile activity, and stores this locally for privacy.** This is the closest thing to a raw usage dataset a data analyst might work with, time spent per app, per site, even per Google profile. Worth knowing this exists as a distinct feature from the core blocking functionality.

4. **Break reminders are "call-aware."** The app detects when a user is in a call or meeting and holds off on break reminders until they're free, rather than interrupting. This is a good example of a feature that would show up as a gap or delay in raw notification/interaction timestamps, not a bug, if I were ever looking at that kind of data.

5. **Cuddly Bear Mode vs Grizzly Bear Mode, and an AI feature that adjusts focus modes.** The app has different "strictness" levels for blocking (gentler vs stricter), plus an AI component that can make focus modes smarter over time. Relevant because any usage analysis would need to account for which mode a user is in, engagement or block-bypass behaviour likely looks very different in Cuddly vs Grizzly mode.

## Reflection

**What did I learn about the product that I didn't know before?**

I hadn't realized how deliberately the app avoids anything resembling surveillance, no keystrokes, no screenshots, just app/site focus state. Given this internship also covered data privacy policy work (issue #11), it's a good concrete example of privacy-by-design actually showing up in a real feature, not just a policy document. I also hadn't known about the separate Time Tracker feature or Google profile tracking, since most of the help centre content is about blocking and routines rather than the analytics-adjacent side of the product.

**Did I spot anything in the help centre that seems out of date or inconsistent with the current app?**

Yes, one worth flagging: the **Focus Bear Time Tracker** article says its data is "stored locally for privacy reasons." But Focus Bear's actual privacy policy (reviewed in issue #11) describes habit and usage data as being double encrypted and processed by the company, implying it's synced/stored beyond just the local device, not purely local. These two statements don't obviously line up, either the Time Tracker genuinely is local-only and separate from the synced habit data, or the help article is stating something that's no longer accurate. This seems worth flagging to the team so someone can confirm which is correct and update the article if needed.
