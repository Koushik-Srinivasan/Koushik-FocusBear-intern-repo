# Merge Conflicts & Conflict Resolution

## Research: what causes merge conflicts in Git

A merge conflict happens when Git tries to combine two branches that have both changed the same part of a file in different ways, and Git can't automatically decide which version should win. Git is usually good at merging changes automatically when they touch different lines or different files, the conflict only comes up when both branches genuinely edited the same lines, so there's no way to guess the "correct" combined result without a human deciding.

## Test scenario

I used the same `calculator.py` file from the git bisect exercise (issue #37). From `main`, I created a branch (`feature-rounding`) and edited the `add` function to round its result to 2 decimal places. Then I switched back to `main` and edited the exact same line differently, converting the result to an integer instead, and committed that on `main`. When I ran `git merge feature-rounding` back into `main`, Git couldn't reconcile the two edits to the same line and stopped with a conflict.

**What Git showed inside the file:**

```
def add(a, b):
(HEAD marker) return int(a + b)
(divider)
(incoming branch marker) return round(a + b, 2)
```

Everything between the HEAD marker and the divider is the current branch's version (main, converting to an integer), everything between the divider and the incoming branch marker is the incoming branch's version (rounding to 2 decimals). Git leaves both versions in the file and expects you to edit it down to the one final version yourself.

**How I resolved it:**

I edited the file directly, removed all the conflict markers, and kept the version that made more sense for a calculator function, rounding to 2 decimal places rather than truncating to a whole number, since losing precision by converting to an integer isn't the right behaviour for an `add` function:

```python
def add(a, b):
    return round(a + b, 2)
```

Then `git add calculator.py` to mark it as resolved, and `git commit` to complete the merge. The resulting log shows both branch histories joining at a merge commit, rather than one edit simply overwriting the other.

## Reflection

**What caused the conflict?**

Both `main` and my feature branch edited the exact same line of `calculator.py`, one to round the result, one to convert it to an integer, after both branches had diverged from the same starting commit. Since Git had two genuinely different versions of the same line with no way to know which one was "correct," it stopped and asked me to decide.

**How did I resolve it?**

By opening the file, reading both versions inside the HEAD marker, divider, and incoming branch marker, and deciding which behaviour was actually correct for the function (rounding, not truncating), rather than blindly picking one side over the other. Then staging the file and committing to finish the merge.

**What did I learn?**

The conflict markers themselves aren't scary once you know what they mean, they're literally just Git showing you "here's your version, here's their version, you decide." What actually matters is understanding *why* each side changed the line, not just mechanically picking one, since blindly keeping "my" version or "their" version can silently lose an intentional change someone else made for a reason. Also, conflicts only happen on the specific lines that both branches touched, not the whole file, so a lot of a merge conflict often looks scarier at first glance (a whole file marked as "both modified") than the actual number of conflicting lines really is.
