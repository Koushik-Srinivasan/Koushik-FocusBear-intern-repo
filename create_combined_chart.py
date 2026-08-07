"""
Basic Charting & Data Visualization with Matplotlib & Seaborn - issue #19
All 5 visualizations combined into a single image file using subplots.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

np.random.seed(42)

# --- Sample dataset: daily focus session usage over 2 weeks ---
dates = pd.date_range("2026-07-01", periods=14, freq="D")
df = pd.DataFrame({
    "date": dates,
    "focus_minutes": np.random.randint(20, 120, size=14),
    "sessions_completed": np.random.randint(1, 6, size=14),
    "device": np.random.choice(["desktop", "mobile"], size=14),
})

fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle("Focus Bear Usage: Matplotlib & Seaborn Practice (Issue #19)", fontsize=14, fontweight="bold")

# 1. Line chart
axes[0, 0].plot(df["date"], df["focus_minutes"], marker="o", color="#2E86AB")
axes[0, 0].set_title("Daily Focus Minutes Over Time")
axes[0, 0].set_xlabel("Date")
axes[0, 0].set_ylabel("Focus Minutes")
axes[0, 0].tick_params(axis="x", rotation=45)

# 2. Bar chart
sessions_by_device = df.groupby("device")["sessions_completed"].sum()
axes[0, 1].bar(sessions_by_device.index, sessions_by_device.values, color=["#F18F01", "#2E86AB"])
axes[0, 1].set_title("Total Sessions by Device")
axes[0, 1].set_xlabel("Device")
axes[0, 1].set_ylabel("Total Sessions")

# 3. Scatter plot
colors = df["device"].map({"desktop": "#2E86AB", "mobile": "#F18F01"})
axes[0, 2].scatter(df["sessions_completed"], df["focus_minutes"], c=colors, s=80, edgecolor="black")
axes[0, 2].set_title("Focus Minutes vs Sessions")
axes[0, 2].set_xlabel("Sessions Completed")
axes[0, 2].set_ylabel("Focus Minutes")

# 4. Histogram (Seaborn)
sns.histplot(df["focus_minutes"], bins=6, kde=True, color="#2E86AB", ax=axes[1, 0])
axes[1, 0].set_title("Distribution of Focus Minutes")
axes[1, 0].set_xlabel("Focus Minutes")
axes[1, 0].set_ylabel("Count")

# 5. Heatmap (Seaborn)
correlation = df[["focus_minutes", "sessions_completed"]].corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm", vmin=-1, vmax=1, ax=axes[1, 1])
axes[1, 1].set_title("Correlation Heatmap")

# 6th slot unused, hide it
axes[1, 2].axis("off")

plt.tight_layout()
plt.savefig("data_visualization_combined.png", dpi=100)
plt.close()

print("Combined chart saved.")
print("\nCorrelation matrix:")
print(correlation)
