# Understanding git bisect

## Research: what does `git bisect` do?

`git bisect` finds the exact commit that introduced a bug using binary search instead of checking every commit one by one. You tell it one commit you know is "good" (before the bug existed) and one you know is "bad" (where the bug is present), and it automatically checks out the commit halfway between them for you to test. Based on whether that midpoint is good or bad, it narrows the range in half again, repeating until only one commit is left, the one that introduced the problem.

## Test scenario

I built a small test repo with 5 commits, each adding one function to a `calculator.py` file (`add`, `subtract`, `multiply`, `divide`, `power`). I deliberately introduced a bug in commit 4, where `divide(a, b)` was written as `a / b + 1` instead of just `a / b`.

I wrote a small test script (`test_calculator.py`) that checks `divide(10, 2)` returns `5`, and exits with a non zero code if it doesn't, so `git bisect` could use it (or in my case, I ran it manually at each step) to tell good commits from bad ones.

**The actual session:**

```
git bisect start
git bisect bad                    # HEAD (commit 5) has the bug
git bisect good 8ba23c8            # first commit is known good

# git checks out the midpoint automatically:
# -> Commit 3 (multiply function, divide doesn't exist yet)
# tested it, no bug possible since divide isn't defined yet
git bisect good

# git checks out the next midpoint:
# -> Commit 4 (divide function added)
python3 test_calculator.py
# FAIL: divide(10, 2) returned 6.0, expected 5
git bisect bad

# result:
# 2aad871e... is the first bad commit
# Commit 4: add divide function
```

Out of 5 commits, `git bisect` only needed to actually test 2 of them (the midpoints) to land on the exact bad commit, rather than checking commits 2, 3, and 4 individually one at a time.

## Reflection

**What does `git bisect` do?**

It automates the process of narrowing down which commit broke something, using binary search rather than a linear commit by commit check. You just need a reliable way to tell "good" from "bad" at each step, either manually testing like I did, or automatically via `git bisect run <script>` if you have an actual test script that returns a pass/fail exit code.

**When would you use it in a real world debugging situation?**

Any time something that used to work stops working, and you don't know which of many recent commits caused it. It's especially useful once a project has accumulated a lot of commits since the bug was introduced, since checking each one manually would be slow, but bisect only needs roughly log2(n) tests to find it, in my 5 commit example, only 2 actual tests were needed.

**How does it compare to manually reviewing commits?**

Manually reviewing means reading through the diff of each commit in order, hoping to spot the bug by eye, which is slow and easy to miss subtle issues (like my `+ 1` typo, which reads fine at a glance if you're not specifically checking the maths). `git bisect` instead relies on actually running the code and checking a real result, so it catches things that would be easy to miss by just reading a diff, and it scales much better as the number of commits between good and bad grows, since it's a binary search rather than a linear scan.

---

# Merge Conflicts & Conflict Resolution

## Research: what causes merge conflicts in Git

A merge conflict happens when Git tries to combine two branches that have both changed the same part of a file in different ways, and Git can't automatically decide which version should win. The conflict only comes up when both branches genuinely edited the same lines, so there's no way to guess the "correct" combined result without a human deciding.

## Test scenario

I used the same `calculator.py` file from the git bisect exercise. From `main`, I created a branch (`feature-rounding`) and edited the `add` function to round its result to 2 decimal places. Then I switched back to `main` and edited the exact same line differently, converting the result to an integer instead, and committed that on `main`. Running `git merge feature-rounding` back into `main` produced a conflict.

**What Git showed inside the file:**

```
def add(a, b):
(HEAD marker) return int(a + b)
(divider)
(incoming branch marker) return round(a + b, 2)
```

**How I resolved it:**

I edited the file directly, kept the version that made more sense for a calculator function (rounding, not truncating, since losing precision by converting to an integer isn't right for `add`):

```python
def add(a, b):
    return round(a + b, 2)
```

Then `git add calculator.py` and `git commit` to complete the merge.

## Reflection

**What caused the conflict?**

Both `main` and my feature branch edited the exact same line of `calculator.py` differently after diverging from the same starting commit, so Git had no way to know which version was correct.

**How did I resolve it?**

By reading both versions inside the HEAD marker, divider, and incoming branch marker, and deciding which behaviour was actually correct (rounding, not truncating), rather than blindly picking one side.

**What did I learn?**

The conflict markers just mean "here's yours, here's theirs, you decide." What matters is understanding why each side changed the line, not mechanically picking one, since blindly keeping "my" version can silently lose an intentional change someone else made for a reason.

---

# Advanced Git Commands & When to Use Them

## Test scenario

I built a small repo (`notes.txt`, 3 commits on `main`) and ran all four commands for real.

### 1. `git checkout main -- <file>`

I edited `notes.txt` to add a stray line, then restored it:

```
git checkout main -- notes.txt
```

The stray line was gone immediately after, the file matched `main`'s last committed version exactly, with the edit completely discarded (not just staged differently, actually reverted).

### 2. `git cherry-pick <commit>`

I created `feature-branch`, made two separate commits on it (one genuinely useful fix, one unrelated experimental change), then switched to `main` and cherry-picked only the first commit's hash:

```
git cherry-pick c4a7d37
```

`main` ended up with the fix (Line 5) but NOT the unrelated experimental change (Line 6), confirming cherry-pick grabs exactly the one commit specified, not everything on the branch after it.

### 3. `git log`

Plain `git log` showed the full commit history with author, date, and message for each commit. `git log --oneline --graph --all` gave a more compact view across all branches at once, useful for seeing the whole shape of history rather than one commit at a time.

### 4. `git blame notes.txt`

Ran against the final file and it correctly attributed each line to the exact commit that introduced it, matching the real commit history I'd built, down to the specific commit hash and timestamp for each line.

## Reflection

**What does each command do?**

`checkout main -- <file>` restores one specific file to match another branch/commit, without touching anything else in the working directory. `cherry-pick` applies one specific commit's changes onto the current branch, without merging the whole branch it came from. `log` shows the commit history, who changed what and when. `blame` shows, line by line, which commit last touched each line of a file.

**When would I use each in a real project?**

`checkout main -- <file>` is for when I've made a mess of one specific file and want to throw those changes away without touching my other in-progress work. `cherry-pick` is for grabbing one genuinely useful fix off a branch that isn't ready to be merged as a whole yet, exactly what I tested, pulling the real fix without the unrelated experimental commit. `log` is for understanding how a project got to its current state, useful when picking up unfamiliar code. `blame` is for tracking down when and why a specific line was introduced, especially useful when a bug traces back to a particular line and I want the context of the commit that added it.

**What surprised me while testing these commands?**

Cherry-picking the fix commit onto `main` produced the exact same commit hash (`c4a7d37`) as it had on `feature-branch`, since the commit's parent, content, author, and message were all identical between the two branches at that point. I hadn't expected cherry-pick to ever produce an identical hash, I assumed it always creates a brand new commit, but it only does that when something is actually different (like a different parent commit).

---

# Branching & Team Collaboration

## Test scenario

I created a new branch (`add-changelog`) off `main`, added a new file (`CHANGELOG.md`) and committed it there. Then I switched back to `main` and confirmed the file genuinely wasn't there:

```
git checkout main
ls
# README.md only, CHANGELOG.md not present

git log --oneline
# e2dd9a1 Initial commit
# (no changelog commit shown, since that commit only exists on add-changelog)
```

`main` still showed only its original single commit, the new file and commit existed exclusively on the branch until I choose to merge it.

## Reflection

**Why is pushing directly to `main` problematic?**

`main` is usually what gets deployed or what everyone else builds on top of, so an untested or half-finished change pushed straight there affects everyone immediately, with no chance for anyone to review it first. Branches give a safe space to make and test changes without touching that shared, trusted version.

**How do branches help with reviewing code?**

Because a branch's changes stay isolated until merged, a pull request can show exactly what's different, and a reviewer can look at that diff, leave comments, or request changes, all before anything reaches `main`. I confirmed this practically, `main` stayed completely clean while I was actively committing on `add-changelog`, exactly the isolation that makes review possible.

**What happens if two people edit the same file on different branches?**

Nothing breaks until someone tries to merge both branches into `main`. If both branches touched different lines, Git usually merges them automatically without any issue. If both touched the exact same lines, that's a merge conflict (which I tested directly in issue #35), Git flags it and a person has to manually decide how to combine the two versions.

---

# Writing Meaningful Commit Messages

## Research: analyzing a real open-source project's history

I looked through Facebook's React repo (`facebook/react`) commit history. What stood out most: even React's *shortest* commit messages (things like "Add ReactDOM `browser()` API" or "Clean up flag to enable microtasks in RN") stay specific and scoped to exactly what changed, never vague filler like "fix" or "update stuff". I also looked at one full, well-structured commit message in detail, which explained the bug being fixed, why it happened (with the technical reasoning), what the fix does, and how it was tested, all as separate sections. That's a good model: a short subject line for scanning history quickly, and a body that explains *why*, not just what, for anyone who needs the full context later.

## Task: three real commits, three styles

I made three commits in a test repo against the same file, one of each style, and confirmed all three actually appear in `git log`:

1. **Vague**: `fixed stuff` — a real commit with this exact message, gives no information about what was fixed or why.
2. **Overly detailed**: a single run-on paragraph explaining every step I took in first person, testing process included, with no structure or line breaks, technically informative but exhausting to actually read.
3. **Well-structured**: a short subject line (`Fix ZeroDivisionError in calculate_average on empty input`) plus a body explaining the bug and the fix, following the same subject+body pattern I saw in React's history.

## Reflection

**What makes a good commit message?**

A short, specific subject line describing what changed, plus (when the change isn't self-explanatory) a body explaining *why* it changed, not just what. Looking at React's real history confirmed this, their shortest messages were still specific, never vague, and their longer ones used the extra space to explain reasoning, not to narrate the process.

**How does a clear commit message help in team collaboration?**

It lets someone understand a change from `git log` alone, without needing to open every commit's full diff or ask the author directly. My well-structured commit ("Fix ZeroDivisionError...") tells a teammate exactly what bug existed and why the fix works, in a few seconds of reading.

**How can poor commit messages cause issues later?**

The vague one ("fixed stuff") is genuinely useless months later, there's no way to know what it actually touched without opening the diff, and if there are many commits like it, `git log` becomes useless for understanding history at a glance. The overly detailed one has the opposite problem, real information is buried in one dense paragraph, so most of it gets skipped or skimmed past. Both make tools like `git blame` (from issue #36) less useful too, since the whole point of blame is to jump straight to the commit that explains a line, and a bad message defeats that purpose even if you find the right commit.

---

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

When I'm partway through a change and want to check exactly what I'm about to include (via `git status` or `git diff --staged`) before finalizing it, or when I've fixed multiple unrelated things in one working session and want to stage and commit them separately, as distinct, well-scoped commits, instead of lumping everything into one. It also matters directly for issue #38 (commit messages), a well-structured, specific commit message is much easier to write when staging was deliberate about exactly what's included.
