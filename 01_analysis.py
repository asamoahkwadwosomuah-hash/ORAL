"""
01_analysis.py
----------------
Analyzes the pace and framing of Ghana's ORAL initiative over time.
"""

import pandas as pd

df = pd.read_csv("../data/oral_timeline.csv", parse_dates=["date"])

print("=" * 65)
print("Q1. How has the reported case count evolved over the timeline?")
case_metrics = df.dropna(subset=["metric"])[["date", "category", "metric"]]
print(case_metrics.to_string(index=False))

print("\n" + "=" * 65)
print("Q2. How many milestones fall into each category?")
print(df["category"].value_counts())

print("\n" + "=" * 65)
print("Q3. What's the time gap between major public updates (SONA mentions, AG briefings)?")
df["days_since_previous"] = df["date"].diff().dt.days
print(df[["date", "category", "days_since_previous"]].to_string(index=False))

print("\n" + "=" * 65)
print("Q4. Was there a shift in tone between the 2025 SONA and 2026 SONA mentions of ORAL?")
sona_events = df[df["category"] == "Presidential Update"]
print(sona_events[["date", "event"]].to_string(index=False))
print("\nNote: 2025 SONA actively cited ORAL 3x with specific numbers; 2026 SONA did not")
print("name ORAL directly, despite ORAL remaining an active, ongoing initiative in the same period.")

print("\n" + "=" * 65)
print("Q5. Longest gap between any two consecutive milestones in this record:")
max_gap_idx = df["days_since_previous"].idxmax()
print(df.loc[max_gap_idx, ["date", "category", "days_since_previous"]])
