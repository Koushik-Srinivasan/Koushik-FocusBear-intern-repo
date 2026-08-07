# Git Concepts: Staging vs. Committing

## Test scenario

I modified `notes.txt` and walked through all four steps for real:

1. **Staged only** (`git add notes.txt`): `git status` showed it under "Changes to be committed", but `git log` still showed only the original commit, confirming staging alone doesn't create history.
2. **Unstaged** (`git reset HEAD notes.txt`): `git status` moved the file back to "Changes not staged for commit". The actual file content was completely untouched, only the staging status changed.
3. **Staged again and committed** (`git add` then `git commit`): `git status` afterward showed "nothing to commit, working tree clean", and `git log` now showed the new commit.

## Reflection

**What is the difference between staging and committing?**

Staging (`git add`) marks a change as "ready to be included in the next commit", it's a holding area, not history yet. Committing (`git commit`) actually saves that staged snapshot permanently into the project's history. I confirmed this directly, the staged-only version never showed up in `git log`, only the committed version did.

**Why does Git separate these two steps?**

It lets you build a commit deliberately rather than committing every single change the moment you make it. If I've edited three files but only two of those edits are actually ready, I can stage just those two and leave the third out, so the commit reflects one intentional, complete change rather than whatever happened to be modified at that moment.

**When would you want to stage changes without committing?**

When I'm partway through a change and want to check exactly what I'm about to include (via `git status` or `git diff --staged`) before finalizing it, or when I've fixed multiple unrelated things in one working session and want to stage and commit them separately, as distinct, well-scoped commits, instead of lumping everything into one.
