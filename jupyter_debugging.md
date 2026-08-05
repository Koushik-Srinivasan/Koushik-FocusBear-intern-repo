# Jupyter Debugging Techniques

## What I tested

I ran a small script (`demo_magics.py`) in a real Python session to try these tools out myself, rather than just reading about them. The script has two things in it: a function that's deliberately slow (adds up a million numbers in a loop), and a function that has a real bug (it tries to divide two numbers from a dictionary, but I called it with one of those numbers missing, so it crashes).

## Ways to find out why code crashed

- **`%debug`** — After your code crashes, this command opens up an inspector right at the exact spot where it broke, so you can look at what all your variables actually were at that moment. It's like pausing time right when the error happened.
- **`%pdb on`** — Turns on that same inspector automatically for the rest of your session, so you don't have to remember to type `%debug` every time something crashes.
- **`%xmode`** — Controls how much detail you see in an error message. You can ask for just a short version, a medium version, or a very detailed version that shows the actual values of every variable involved when it crashed. The detailed version is most useful when you're trying to figure out exactly what value caused the problem.
- **`%%debug`** — Same idea as `%debug`, but for stepping through an entire block of code from the very start, not just after it crashes.

I actually triggered the bug in my test script and confirmed it fails with:
```
KeyError: 'goal_minutes'
```
This just means: "I tried to look up something in a dictionary that wasn't there." This is exactly the kind of crash where `%debug` would let you immediately see what the dictionary actually contained at that moment, instead of having to guess.

## The visual debugger in JupyterLab

JupyterLab has a built in point-and-click debugging tool. Instead of typing commands, you can click directly next to a line of code to pause there, then see all your current variables and their values in a side panel, plus a list showing which functions called which other functions to get you there. The older-style notebooks don't have this, you'd have to type commands instead. The visual version is just an easier way to do the same basic thing, look at what's happening step by step.

## Checking why code is running slowly

I tested these for real on the slow function (the one adding up a million numbers):

- **`%time`** — times one run. Mine took about 28 milliseconds.
- **`%timeit`** — runs it several times and gives you an average, so one unusually fast or slow run doesn't throw off your measurement. Mine averaged about 28 milliseconds too, which matched `%time`, a good sign the measurement was reliable.
- **`%prun`** — gives you a full breakdown of exactly which part of your code ate up the time. When I ran it, it confirmed almost all the time really was spent inside my slow function, not somewhere else I wasn't expecting.
- **`%lprun`** — like `%prun`, but even more zoomed in, it shows you the timing for each individual line inside a function, so if one specific line is the slow part, this points right at it.
- **`%memit`** — same idea as timing, but for memory instead of speed. Useful when a notebook is using way more memory than expected, rather than running slowly.

## Which approach to reach for, and when

- **Just printing values out** is the quickest option for a fast check, but it gets messy if you leave prints scattered everywhere, and you have to remember to remove them afterward.
- **`%debug`** is better once something has actually broken, since it shows you everything at the exact moment of the crash without you having to guess in advance where to add a print statement.
- **The point-and-click debugger** is best when you want to slowly step through your code and watch it, especially when something isn't crashing, it's just giving a wrong answer.
- **Tools like `icecream` or `snoop`** sit in between, they print out variable names and values automatically with less typing than doing it by hand, or in the case of `snoop`, automatically show you every single line as it runs.

For notebooks specifically, since they tend to run for a long time and cells can get run out of order, `%debug` tends to be the most practical everyday tool, it works on whatever just failed using things exactly as they currently are, no need to plan ahead or restart anything.

## Trickier notebook-specific problems

- **The notebook seems frozen and won't respond** — this usually means there's a loop that never ends, or the code is waiting on something (like typed input, or a slow network request) that never arrives. The fix is to stop it and add a limit or timeout, a debugging command won't help here since a frozen notebook can't respond to anything.
- **The notebook is using way more memory than it should** — notebooks keep every variable from every cell you've run alive in memory, even old ones you're done with. Over time this piles up. Checking memory usage (with `%memit`) helps spot it, and the real fix is usually just restarting and re-running everything cleanly from the top.
- **Things behave differently than what's on screen** — this happens because you can run cells out of order (like re-running an earlier cell after a later one), so what's actually stored in memory might not match what you'd expect just from reading top to bottom. The safest way to check is to restart everything and run every cell in order, so what you see genuinely matches what ran.
- **Editing code in a separate file doesn't seem to update anything** — normally, once you import code from another file, your notebook keeps using the old version even if you edit that file, unless you restart everything. There's a shortcut for this: turning on "autoreload" makes the notebook automatically pick up your edits to that file without needing a restart. Debugging tools also work fine on code from these separate files, not just code typed directly into the notebook.
