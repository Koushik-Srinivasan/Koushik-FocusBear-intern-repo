# Creating & Reviewing Pull Requests

## Research: what a PR is and why it's used

A Pull Request proposes a set of changes on a branch and asks for them to be reviewed before merging into the main codebase. It's the mechanism that makes code review actually happen, rather than changes going straight into `main` unreviewed.

## My PR: evidence

- **Repo:** Koushik-FocusBear-intern-repo
- **PR title:** Add contact info to README (#56)
- **Branch:** `docs/add-contact-info`, merged into `main`
- **Change made:** added contact info to README.md
- **Linked issue:** PR description included "closes issue #39", so merging automatically closed this issue
- **Feedback requested from:** not yet done at time of writing, still outstanding
- **Status:** Merged (1 commit merged into `main`), and the `docs/add-contact-info` branch was deleted immediately after.

## Task: reviewing a real open-source PR

I reviewed [facebook/react PR #36236, "[Flight] Add more cycle protections"](https://github.com/facebook/react/pull/36236), a real, merged security fix.

What I observed:
- The PR description was one sentence, but the right one, stating the purpose plainly.
- A size-comparison bot (`react-sizebot`) posted automated bundle-size impact before any human reviewed it.
- Specific reviewers were requested (`gnoff` and `unstubbable`) rather than left open-ended, unlike my own PR where I hadn't requested a reviewer.
- One approval was enough to merge, since it was a small, well-scoped fix.
- The branch was deleted immediately after merging, same as mine.

## Reflection

**Why are PRs important in a team workflow?**

They create a checkpoint before code reaches `main`, a place for another person or automated check to catch a problem before it affects everyone. My own PR followed the mechanical shape of this (branch, change, merge, delete), though I still need to close the loop by actually getting a second person to look at it, which is the part of the process I haven't completed yet.

**What makes a well-structured PR?**

A clear, specific description of what changed and why, even if brief, plus small, focused changes rather than a mix of unrelated edits, and linking the related issue so merging closes it automatically, which I did via "closes issue #39" in the description.

**What did I learn from reviewing an open-source PR?**

I hadn't thought about how much of "review" can be automated before a human ever looks at it, and that reviewers are often deliberately assigned rather than left open-ended. That's actually the gap in my own PR right now, no reviewer was requested, so the next real step for me is asking someone directly for feedback rather than treating the merge as the finish line.
