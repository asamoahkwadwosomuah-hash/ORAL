"""
02_build_timeline_viz.py
---------------------------
Builds a visual timeline of ORAL milestones, plus a simple chart of how
the reported case/docket count has grown over time.
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv("../data/oral_timeline.csv", parse_dates=["date"])

GREEN = "#046A38"
GOLD = "#FCD116"
RED = "#CE1126"

CATEGORY_COLORS = {
    "Announcement": GOLD,
    "Report Submitted": GREEN,
    "Presidential Update": "#2E5C8A",
    "Process Update": "#888888",
    "Prosecution Announced": RED,
    "Public Criticism": "#B23A48",
    "Institutional Defense": GREEN,
}

fig, axes = plt.subplots(2, 1, figsize=(14, 12), gridspec_kw={"height_ratios": [1.4, 1]})
fig.suptitle("Operation Recover All Loot (ORAL) — Institutional Timeline, Dec 2024–Aug 2026",
             fontsize=15, fontweight="bold", y=0.99)
fig.text(0.5, 0.955, "Compiled from public news reporting (Graphic Online, GhanaWeb, Pulse Ghana, GBC Ghana) — see README for sources and caveats",
         ha="center", fontsize=8.5, style="italic", color="gray")

# --- Panel 1: Timeline (lollipop style) ---
ax = axes[0]
for i, row in df.iterrows():
    color = CATEGORY_COLORS.get(row["category"], "black")
    ax.vlines(row["date"], 0, 1, color=color, linewidth=2, alpha=0.7)
    ax.scatter(row["date"], 1, color=color, s=90, zorder=3, edgecolor="black", linewidth=0.5)
    label = row["category"]
    y_text = 1.05 if i % 2 == 0 else -0.15
    va = "bottom" if i % 2 == 0 else "top"
    ax.annotate(label, (row["date"], 1), xytext=(row["date"], y_text),
                rotation=30, ha="left", va=va, fontsize=8.5,
                arrowprops=dict(arrowstyle="-", color=color, alpha=0.5))

ax.set_ylim(-0.6, 1.6)
ax.get_yaxis().set_visible(False)
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
plt.setp(ax.get_xticklabels(), rotation=45, ha="right")
ax.set_title("Milestone Timeline", pad=45)
for spine in ["top", "right", "left"]:
    ax.spines[spine].set_visible(False)

# --- Panel 2: Reported case/docket count over time ---
ax2 = axes[1]
metrics = df.dropna(subset=["metric"]).copy()
# Exclude raw complaint counts (Report Submitted: 2,417 complaints; Presidential
# Update: 2,000 complaints) — these are a different unit from "cases/dockets
# confirmed for prosecution" and plotting them together would misleadingly
# suggest a collapse from thousands of cases down to dozens, when in fact the
# 2,000-2,417 figures are unvetted raw complaints, not prosecutable cases.
metrics = metrics[metrics["category"].isin(
    ["Prosecution Announced", "Process Update", "Institutional Defense"]
)]
ax2.plot(metrics["date"], metrics["metric"], marker="o", color=RED, linewidth=2, markersize=9)
for _, row in metrics.iterrows():
    ax2.annotate(f"{int(row['metric'])}", (row["date"], row["metric"]),
                 textcoords="offset points", xytext=(0, 10), ha="center", fontsize=9, fontweight="bold")
ax2.set_title("Cases/Dockets Confirmed for Prosecution Over Time\n(excludes raw complaint counts, which are a different, unvetted unit — see README)")
ax2.set_ylabel("Number of Cases/Dockets")
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax2.get_xticklabels(), rotation=45, ha="right")
ax2.grid(alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig("../outputs/timeline_dashboard.png", dpi=150, bbox_inches="tight")
print("Saved ../outputs/timeline_dashboard.png")
