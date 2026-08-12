# Pull Requests

## Research: what a PR is and why it's used

A Pull Request proposes a set of changes on a branch and asks for them to be reviewed before merging into the main codebase. It's the mechanism that makes code review actually happen, rather than changes going straight into `main` unreviewed.

## Task: creating a branch and committing a small change

I created a branch (`docs/add-contact-info`), made a small change (added a contact line to README.md), and committed it:
```
git checkout -b docs/add-contact-info
# edited README.md
git commit -m "Add contact info to README"
```
This is the local half of the task, actually opening the PR on GitHub needs to happen for real in your repo (push the branch, then GitHub will prompt "Compare & pull request").

## Task: reviewing a real open-source PR

I reviewed [facebook/react PR #36236, "[Flight] Add more cycle protections"](https://github.com/facebook/react/pull/36236), a real, merged security fix.

What I observed:
- **The PR description was one sentence**: "This fixes security vulnerabilities in Server Functions." Short, but sufficient, the actual code change and tests carry the detail, the description just states the purpose.
- **Automated checks ran automatically**: a size-comparison bot (`react-sizebot`) posted a comment showing exactly how the change affected bundle size across multiple build targets, before any human even reviewed it.
- **Specific reviewers were requested** (`gnoff` and `unstubbable`), rather than the PR being left open for anyone to review, review responsibility was assigned deliberately.
- **One approval was enough to merge**: `gnoff` approved, and the author merged shortly after, no lengthy back-and-forth was needed since this was a small, well-scoped fix.
- **The branch was deleted immediately after merging**, keeping the repo's branch list clean.
- This PR was also directly referenced in React's own release notes for version 19.2.5, showing how a single PR traces directly through to a versioned release.

## Reflection

**Why are PRs important in a team workflow?**

They create a checkpoint before code reaches `main`, a place for another person (or an automated check) to catch a problem before it affects everyone. The React example showed this clearly, a bundle-size bot flagged the impact automatically, and a specific reviewer signed off, before the change was allowed to merge.

**What makes a well-structured PR?**

A clear, specific description of what changed and why, even if brief. React's PR description was just one sentence, but it was the *right* one sentence, stating the purpose plainly. Small, focused changes also help, this PR was one commit fixing one specific issue, not a sprawling mix of unrelated changes, which is part of why it could be reviewed and merged quickly.

**What did I learn from reviewing an open-source PR?**

I hadn't thought about how much of "review" can be automated before a human ever looks at it, the size-bot comment gave concrete, objective data (bundle size impact) that a human reviewer would otherwise have to check manually. I also noticed that reviewers were explicitly requested rather than left open-ended, review isn't just "wait for someone," it's often a deliberate assignment to the person best placed to judge that specific change.
