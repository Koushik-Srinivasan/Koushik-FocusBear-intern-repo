# Jupyter Notebooks Reflection

## Research: what are Jupyter Notebooks and why use them for data analytics

A Jupyter Notebook is an interactive document made up of cells, code cells you can run individually, and Markdown cells for writing explanations, right in the same file. Unlike a regular Python script that runs top to bottom as one block, each cell in a notebook runs independently and keeps its output visible underneath it. That's exactly why it fits data analytics so well, you can load a dataset in one cell, inspect it in the next, and adjust just that one step without re-running everything else. Practicing this in `jupyter_notebook_practice.ipynb`, the loop was genuinely load, then inspect, then summarise, each as its own cell with the result sitting right there.

## Task notes

I installed Jupyter, built a notebook, loaded a small sample dataset with pandas, inspected its shape and missing values, ran a quick summary with `.describe()`, and documented findings in Markdown cells alongside the code. The notebook is included in this repo as `jupyter_notebook_practice.ipynb`.

## Reflection

**What are the advantages of using Jupyter Notebooks for data analysis?**

The biggest one is immediate feedback, run a cell, see the result right there, adjust, run again, without re-running the whole script from scratch every time something needs tweaking. It also keeps the output attached to the code that produced it, so scrolling back through a notebook later shows both what was run and what it returned, which is much easier to review than a script's output that's already scrolled off a terminal.

**How does Jupyter improve workflows compared to writing standalone Python scripts?**

With a standalone script, changing one part usually means re-running the entire file to see the effect, even if 90% of it hadn't changed. In the notebook, I could load the dataset once, then freely experiment with different inspection or summary steps in separate cells without reloading the data each time. For genuinely exploratory work, where you don't know in advance exactly what you're looking for, that back and forth is much faster than the edit-run-repeat cycle of a script.

**What are Markdown cells, and why are they useful in notebooks?**

Markdown cells are plain text cells (supporting headings, bullet points, formatting) that sit alongside the code cells but don't execute as code. I used them to explain what each step was doing and to write up the actual insights at the end. They matter because a notebook full of just code and raw output is hard for someone else (or future me) to follow, the markdown cells are what turn a sequence of commands into something that actually reads as an analysis with reasoning attached, rather than a wall of disconnected outputs.

**How could Jupyter Notebooks be used for analysing Focus Bear's user trends?**

The same load, inspect, summarise pattern from this practice notebook would apply directly to real usage data, for example checking trends in focus session length, completion rates, or device usage over time. Being able to quickly test a hypothesis (like "do mobile users complete more/fewer sessions than desktop users") in one cell, see the result immediately, and then write up what it means in a markdown cell right next to it, is a natural fit for the kind of exploratory analysis this internship is aimed at, rather than committing to a fixed script before knowing what's actually in the data.
