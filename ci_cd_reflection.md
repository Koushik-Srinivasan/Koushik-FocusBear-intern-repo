# CI/CD Reflection

## Research: what CI/CD is and why it's used

CI (Continuous Integration) means automatically checking every change (tests, linting, builds) as soon as it's pushed or opened as a PR, rather than manually running checks yourself and hoping you didn't forget one. CD (Continuous Deployment/Delivery) extends that by automatically shipping changes that pass those checks. The point of both is catching problems early and consistently, the same checks run every time, on every change, regardless of who made it or whether they remembered to run them locally.

## Task: setting this up and actually testing it

**GitHub Actions workflow** (`markdown-checks.yml`): runs on every pull request that touches a `.md` file, installs `markdownlint-cli` and `cspell`, then runs both against all markdown files in the repo.

**Husky pre-commit hook**: I installed Husky and `lint-staged`, and configured the pre-commit hook to run `markdownlint` and `cspell` specifically on staged `.md` files before a commit is allowed to complete.

I tested this wasn't just theoretical by actually trying to commit a broken file, one with a missing space after a heading hash, inconsistent spacing, and two genuinely misspelled words ("mispeled", "wrod"). The commit was **actually blocked**:
```
✖ markdownlint:
test_doc.md:1:1 error MD018/no-missing-space-atx No space after hash on atx style heading
...
husky - pre-commit script failed (code 1)
```
I then fixed the file (correct heading spacing, correct spelling) and staged it again, this time the commit succeeded:
```
✔ markdownlint
✔ cspell
✔ Done running tasks for staged files!
[master (root-commit) 9c6a73c] Test commit with a clean markdown file
```

This confirmed the whole pipeline actually works, not just that the config files exist.

## Reflection

**What is the purpose of CI/CD?**

To catch problems automatically and consistently, at the moment a change is made, rather than relying on every contributor to remember to run checks manually, or catching issues only after they're already merged.

**How does automating style checks improve project quality?**

It removes the need to manually review markdown formatting or catch typos by eye, which I confirmed directly, the linter caught 6 real formatting issues and the spell checker caught 2 real typos in my test file, all without me having to spot them myself. It also means the same standard applies to every contributor automatically, not just whoever happens to be careful that day.

**What are some challenges with enforcing checks in CI/CD?**

From testing this myself, the pre-commit hook adds real friction, if I write a commit with markdown issues, I genuinely cannot commit until I fix them, which is the point, but it does mean checks need to be fast and accurate, or they become an annoyance people try to bypass (like using `--no-verify` to skip the hook). Balancing strictness (catching real problems) against noise (flagging things that aren't actually issues) is a real design decision, not just a setup step.

**How do CI/CD pipelines differ between small projects and large teams?**

For a small project like this test repo, one straightforward workflow (lint + spellcheck on PRs) is enough. Larger teams typically need more stages, running different check types in parallel, requiring passing checks before merge is even allowed (branch protection), and potentially different pipelines for different parts of a larger codebase, since one team's changes shouldn't need to wait on unrelated checks for a totally different part of the project.
