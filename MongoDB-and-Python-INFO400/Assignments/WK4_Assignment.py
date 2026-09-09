"""
Week 4 Assignment: Data Visualization
Author: Sean Coggeshall

Creates data visualizations using Matplotlib and Cartopy, including a
salary distribution pie chart with merged low-count bins and a geographic
map of Florida cities plotted on a Mercator projection with coastline
outlines and population-based labeling.
"""
# ------------------------------------------------------------------------------

# EXERCISE 12: COMBINING BINS INTO AN “OTHER” SLICE
import numpy as np
import matplotlib.pyplot as plt

# Sample salary data
salaries = [
    1215, 1221, 1263, 1267, 1271, 1274, 1275, 1318, 1320, 1324, 1324, 1326,
    1337, 1346, 1354, 1355, 1364, 1367, 1372, 1375, 1376, 1378, 1378, 1410,
    1415, 1415, 1418, 1420, 1422, 1426, 1430, 1434, 1437, 1451, 1454, 1467,
    1470, 1473, 1477, 1479, 1480, 1514, 1516, 1522, 1529, 1544, 1547, 1554,
    1562, 1584, 1595, 1616, 1626, 1717
]

# Build a histogram with $50 increments
count, bins = np.histogram(salaries, bins=np.arange(1100, 1900, 50))

# Create bin labels formatted as "$1100-$1150"
labels = [f'${bins[i]:.0f}-${bins[i+1]:.0f}' for i in range(len(bins) - 1)]

# Filter out empty bins
nonzero_indices = [i for i, c in enumerate(count) if c != 0]
count = [count[i] for i in nonzero_indices]
labels = [labels[i] for i in nonzero_indices]

# Merge slices with 2 or fewer employees into a single "Others" slice
merged_labels = []
merged_counts = []
others_sum = 0
for lbl, c in zip(labels, count):
    if c <= 2:
        others_sum += c
    else:
        merged_labels.append(lbl)
        merged_counts.append(c)
if others_sum > 0:
    merged_labels.append("Others")
    merged_counts.append(others_sum)

# Create and name the figure window for Exercise 12
plt.figure(num='EXERCISE 12: Salary Pie Chart')
plt.pie(merged_counts, labels=merged_labels, autopct='%1.1f%%')
plt.title('Monthly Salaries in the Sales Department')
plt.show()

# ------------------------------------------------------------------------------

# EXERCISE 13: DRAWING A MAP WITH CARTOPY AND MATPLOTLIB
import pandas as pd
import cartopy.crs as ccrs
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

# Load the dataset of US cities from GitHub
us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")

# Filter for Florida cities
fl_cities = us_cities[us_cities['State'].eq('Florida')]

# Define North Florida latitude and longitude ranges (approximate)
lat_min, lat_max = 27, 33  # Covers from south Florida to the northern border
lon_min, lon_max = -88, -80  # Covers the western to eastern parts of Florida

# Filter for cities in North Florida within the defined ranges
norfl_cities = fl_cities[
    (fl_cities['lat'] >= lat_min) & (fl_cities['lat'] <= lat_max) &
    (fl_cities['lon'] >= lon_min) & (fl_cities['lon'] <= lon_max)
]

# Filter for major cities (population >= 200,000) for labeling
top_norfl_cities = norfl_cities[norfl_cities['Population'] >= 200000]

# Create figure and axes with Mercator projection
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.Mercator()})

# Add coastal outlines with 10m resolution
ax.coastlines('10m')

# Set latitude and longitude ticks at 1-degree intervals
ax.set_yticks(range(lat_min, lat_max + 1), crs=ccrs.PlateCarree())
ax.set_xticks(range(lon_min, lon_max + 1), crs=ccrs.PlateCarree())

# Format tick labels to display as degrees with directional symbols
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

# Set map extent to focus on North Florida
ax.set_extent([lon_min, lon_max, lat_min, lat_max], crs=ccrs.PlateCarree())

# Plot all North Florida cities as red dots
ax.scatter(norfl_cities['lon'], norfl_cities['lat'], color='red', marker='o', transform=ccrs.PlateCarree())

# Add labels for major cities (population >= 200,000)
for i in top_norfl_cities.index:
    label = top_norfl_cities['City'][i]
    ax.text(top_norfl_cities['lon'][i], top_norfl_cities['lat'][i] + 0.05, label, 
            clip_on=True, fontsize=10, horizontalalignment='center', transform=ccrs.Geodetic())

# Add a figure-level title naming the exercise
plt.suptitle("Exercise #13: Map of North Florida Cities", fontsize=16)

# Display the final map
plt.show()
