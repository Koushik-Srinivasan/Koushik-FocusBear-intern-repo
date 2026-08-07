# Data Visualization Reflection

## Task: charts created

I built 5 charts using a sample dataset of daily focus session usage over 2 weeks (`focus_minutes`, `sessions_completed`, `device`):

- **Line chart** (Matplotlib) — focus minutes over time, showing day-to-day fluctuation.
- **Bar chart** (Matplotlib) — total sessions completed, grouped by device.
- **Scatter plot** (Matplotlib) — focus minutes vs sessions completed, colored by device.
- **Histogram with KDE** (Seaborn) — distribution of daily focus minutes.
- **Heatmap** (Seaborn) — correlation between focus minutes and sessions completed.

All were customized with titles, axis labels, and consistent colors rather than left at Matplotlib's plain defaults. Ran the script end to end and confirmed all 5 PNG files generated correctly, and the heatmap's correlation value (-0.26) matched the actual computed correlation on the sample data, not a made-up number.

## Reflection

**Why is data visualization important in analytics?**

A chart lets you see a pattern (a trend, an outlier, a relationship between two variables) in seconds that would take much longer to spot by scanning raw numbers in a table. The line chart alone made the day-to-day swings in focus minutes immediately obvious, something I would have had to mentally calculate from a plain list of numbers otherwise.

**What types of charts are most useful for different types of data?**

Line charts fit anything ordered over time (like daily usage). Bar charts fit comparing totals across separate categories (like device type). Scatter plots fit checking whether two numeric variables move together. Histograms fit understanding the shape of a single variable's distribution (is it clustered, spread out, skewed). Heatmaps fit comparing many pairs of variables against each other at once, which doesn't scale well as separate scatter plots once you have more than 2-3 variables.

**How do Seaborn's advanced visualizations compare to Matplotlib's basic charts?**

Seaborn sits on top of Matplotlib and handles a lot of statistical detail automatically, the histogram I built included a KDE (smoothed distribution curve) with one extra argument, and the heatmap automatically color-scaled and annotated every cell with its correlation value. The same results are technically possible in plain Matplotlib, but would take noticeably more code to get looking right. Matplotlib gives more granular control when you need to customize something specific; Seaborn gets you to a polished statistical chart faster for common cases.

**How could Focus Bear use visualizations to improve product decision-making?**

Based on what I practiced here directly: a line chart could track engagement trends over time (are focus minutes trending up or down after a feature change), a bar chart could compare metrics across device or plan type (similar to what I explored in issue #21's Pandas practice), and a heatmap could quickly reveal which usage metrics tend to move together, useful for spotting, for example, whether users who complete more sessions also tend to have longer average sessions, or whether those are actually unrelated, which is exactly the kind of relationship a heatmap surfaces faster than scanning a table of numbers.
