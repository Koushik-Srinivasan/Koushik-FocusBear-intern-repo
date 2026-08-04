# Python for Analytics Reflection

## Setting up a virtual environment

I set up a virtual environment to keep this project's libraries isolated from other Python projects on my machine:

```powershell
python -m venv venv
venv\Scripts\activate
pip install pandas matplotlib seaborn numpy
```

Once activated, I installed the four core libraries the issue asked about and confirmed they all imported correctly before writing the actual script.

## Task: loading and printing a dataset

I wrote `load_and_print_dataset.py`, which loads a small sample CSV (`sample_dataset.csv`, representing daily focus session usage) into a pandas DataFrame, then prints the full dataset, its column info, and summary statistics. I ran it and confirmed all three sections printed correctly.

## Reflection

**Why is Python preferred for data analytics over other languages?**

For me, the biggest reason is the ecosystem, pandas, numpy, matplotlib, and seaborn all work together smoothly, so I can go from raw data to a cleaned table to a chart without switching tools or languages. I also find the syntax itself easier to read and write quickly compared to something more verbose, which matters when I'm exploring data and want to iterate fast rather than fight the language itself.

**What role does Pandas play in data analysis?**

Pandas is what I actually load, clean, and reshape my data with, the DataFrame is the central structure I work in for basically everything: filtering rows, grouping and aggregating, joining separate datasets, handling missing values. I already practiced this directly in issue #21, and it's clearly the backbone that the rest of the Python data stack builds on top of.

**How do Matplotlib and Seaborn help with data visualization?**

Matplotlib is the lower level plotting library, it gives me full control over a chart but takes more code to get something polished. Seaborn sits on top of it and gives me nicer looking statistical charts (like distributions or comparisons across categories) with much less code, since a lot of the styling and common chart types are already built in. In practice I'd probably reach for Seaborn first for a quick exploratory chart, and drop down to Matplotlib when I need to customize something Seaborn doesn't handle directly.

**What are some use cases for data analytics in Focus Bear?**

Based on what I've picked up so far in this internship, I can see Python being used for things like analysing usage patterns (focus minutes, session counts, device breakdowns, similar to what I practiced with pandas in issue #21), tracking trends over time (like whether engagement drops after a missed day, connecting to what I read about ADHD/executive functioning support in issue #9), and building the kind of reports or dashboards that would come from combining pandas for the data work with matplotlib/seaborn for the visuals.
