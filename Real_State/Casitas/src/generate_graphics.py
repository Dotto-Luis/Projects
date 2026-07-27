#!/usr/bin/env python3
"""
Casitas Graphics Generator
Generates PNG charts from ranking_final_*.csv
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import sys

PROJECT_ROOT = Path(__file__).parent.parent
DATA_OUTPUT = PROJECT_ROOT / "data" / "output"

# Load ranking (latest file or specified)
ranking_file = None
if len(sys.argv) > 1:
    ranking_file = Path(sys.argv[1])
else:
    # Find most recent ranking file
    import glob
    files = sorted(glob.glob(str(DATA_OUTPUT / "ranking_final_*.csv")))
    if files:
        ranking_file = Path(files[-1])

if not ranking_file or not ranking_file.exists():
    print(f"Ranking not found")
    sys.exit(1)

df = pd.read_csv(ranking_file)

# Filter: only recommended properties (exclude rentals and score=0)
df = df[(df["recommendation"] != "discard") & (df["score_total"] > 0)].copy()
df = df[~df["titulo"].str.contains("Alquiler", case=False, na=False)].copy()
df = df[df["precio"].notna()].copy()

timestamp = datetime.now().strftime("%Y%m%d_%H%M")

print(f"Reading: {ranking_file.name}")
print(f"Properties: {len(df)}")

# ─────────────────────────────────────────────────────────────────────────────
# CHART 1: Score vs Price (Large, detailed)
# ─────────────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(12, 7))

# Colors by recommendation (Pastel traffic light system)
rec_colors = {
    "strong_opportunity": "#A8D8A8",  # Pastel green (best)
    "worth_visit": "#FFD699",         # Pastel yellow (good - deserves visit)
    "price_only": "#F0A0A0"           # Pastel red (marginal - price negotiable)
}
colors = [rec_colors.get(str(r).lower(), "#999999") for r in df.get("recommendation", [])]

# Scatter plot
scatter = ax.scatter(df["precio"], df["score_total"], c=colors, s=120, alpha=0.7, edgecolors="black", linewidth=0.5)

# Labels with ranking numbers
for idx, row in df.iterrows():
    ax.annotate(f"{idx+1}", (row["precio"], row["score_total"]),
                fontsize=8, ha="center", va="center", weight="bold")

# Threshold lines
ax.axhline(y=85, color="lightgray", linestyle="--", alpha=0.5, linewidth=1)
ax.axhline(y=70, color="lightgray", linestyle="--", alpha=0.5, linewidth=1)

# Labels and formatting
ax.set_xlabel("Price (EUR)", fontsize=12, weight="bold")
ax.set_ylabel("Score", fontsize=12, weight="bold")
ax.set_title("Score vs Price — Recommended Properties Malaga 2026", fontsize=13, weight="bold", pad=20)
ax.grid(True, alpha=0.2, linestyle=":", linewidth=0.5)

# Legend
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor="#A8D8A8", edgecolor="black", label="strong_opportunity"),
    Patch(facecolor="#FFD699", edgecolor="black", label="worth_visit"),
    Patch(facecolor="#F0A0A0", edgecolor="black", label="price_only")
]
ax.legend(handles=legend_elements, loc="lower right", fontsize=10, framealpha=0.95)

plt.tight_layout()
output_file = DATA_OUTPUT / f"graphic_score-price_{timestamp}.png"
plt.savefig(str(output_file), dpi=150, bbox_inches="tight", facecolor="white")
plt.close()

print(f"Chart: {output_file.name} ({output_file.stat().st_size / 1024:.1f} KB)")

# ─────────────────────────────────────────────────────────────────────────────
# CHART 2: Recommendation Distribution (Pie Chart)
# ─────────────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(8, 8))

# Count by recommendation
rec_counts = df["recommendation"].value_counts()
rec_labels = {
    "strong_opportunity": "Strong Opportunity",
    "worth_visit": "Worth Visit",
    "price_only": "Price Only"
}
# Map colors to recommendations
color_map = {
    "strong_opportunity": "#A8D8A8",  # Green (best)
    "worth_visit": "#FFD699",          # Yellow (good)
    "price_only": "#F0A0A0"            # Red (marginal)
}
labels = [rec_labels.get(r, r) for r in rec_counts.index]
pastel_pie = [color_map.get(r, "#999999") for r in rec_counts.index]
wedges, texts, autotexts = ax.pie(
    rec_counts.values,
    labels=labels,
    autopct="%1.1f%%",
    colors=pastel_pie,
    startangle=90,
    textprops={"fontsize": 11, "weight": "bold"}
)
for autotext in autotexts:
    autotext.set_color("white")
    autotext.set_fontsize(10)

ax.set_title("Recommendation Distribution", fontsize=13, weight="bold", pad=20)

plt.tight_layout()
output_pie = DATA_OUTPUT / f"graphic_recommendation_distribution_{timestamp}.png"
plt.savefig(str(output_pie), dpi=150, bbox_inches="tight", facecolor="white")
plt.close()

print(f"Chart: {output_pie.name} ({output_pie.stat().st_size / 1024:.1f} KB)")

# ─────────────────────────────────────────────────────────────────────────────
# CHART 3: Price per m² Distribution (Histogram)
# ─────────────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(11, 5))

# Calculate price per m²
df_hist = df.copy()
df_hist["precio_por_m2"] = (df_hist["precio"] / df_hist["m2"]).round(0)

# Histogram
ax.hist(df_hist["precio_por_m2"], bins=20, color="#1565C0", alpha=0.7, edgecolor="black", linewidth=0.5)

# Labels and formatting
ax.set_xlabel("Price per m² (EUR)", fontsize=12, weight="bold")
ax.set_ylabel("Frequency", fontsize=12, weight="bold")
ax.set_title("Price per m² Distribution", fontsize=13, weight="bold", pad=20)
ax.grid(True, alpha=0.2, linestyle=":", linewidth=0.5, axis="y")

# Add mean line
mean_price_per_m2 = df_hist["precio_por_m2"].mean()
ax.axvline(mean_price_per_m2, color="red", linestyle="--", linewidth=2, label=f"Mean: EUR {mean_price_per_m2:.0f}/m²")
ax.legend(fontsize=10, loc="upper right")

plt.tight_layout()
output_hist = DATA_OUTPUT / f"graphic_price_per_sqm_histogram_{timestamp}.png"
plt.savefig(str(output_hist), dpi=150, bbox_inches="tight", facecolor="white")
plt.close()

print(f"Chart: {output_hist.name} ({output_hist.stat().st_size / 1024:.1f} KB)")

# ─────────────────────────────────────────────────────────────────────────────
# CHART 4: Price Range by Recommendation (Box Plot)
# ─────────────────────────────────────────────────────────────────────────────

fig, ax = plt.subplots(figsize=(11, 5))

# Prepare data for box plot
df_box = df.copy()
df_box["recommendation_label"] = df_box["recommendation"].map(rec_labels)

# Order by recommendation
rec_order = ["Strong Opportunity", "Worth Visit", "Price Only"]
data_by_rec = [df_box[df_box["recommendation_label"] == r]["precio"].values for r in rec_order]

# Box plot
bp = ax.boxplot(
    data_by_rec,
    tick_labels=rec_order,
    patch_artist=True,
    notch=False
)

# Color boxes (pastel traffic light) - order: strong_opp, worth_visit, price_only
pastel_colors = ["#A8D8A8", "#FFD699", "#F0A0A0"]
for patch, color in zip(bp["boxes"], pastel_colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.8)

# Style
for whisker in bp["whiskers"]:
    whisker.set(linewidth=1.5, color="gray")
for cap in bp["caps"]:
    cap.set(linewidth=1.5, color="gray")
for median in bp["medians"]:
    median.set(linewidth=2, color="darkred")

ax.set_ylabel("Price (EUR)", fontsize=12, weight="bold")
ax.set_title("Price Range by Recommendation", fontsize=13, weight="bold", pad=20)
ax.grid(True, alpha=0.2, linestyle=":", linewidth=0.5, axis="y")
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"€{x/1000:.0f}K"))

plt.tight_layout()
output_box = DATA_OUTPUT / f"graphic_price_range_by_recommendation_{timestamp}.png"
plt.savefig(str(output_box), dpi=150, bbox_inches="tight", facecolor="white")
plt.close()

print(f"Chart: {output_box.name} ({output_box.stat().st_size / 1024:.1f} KB)")
