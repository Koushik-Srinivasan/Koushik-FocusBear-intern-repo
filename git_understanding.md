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
