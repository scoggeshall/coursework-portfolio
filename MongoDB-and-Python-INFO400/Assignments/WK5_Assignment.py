"""
Week 5 Assignment: Geospatial Analysis and Stock Metrics
Author: Sean Coggeshall

Implements geospatial cab-dispatch algorithms using Shapely polygons and
Geopy distance calculations, demonstrates list comprehension filtering on
order data, and performs stock volatility analysis with rolling metrics
using yfinance and NumPy.
"""
# ------------------------------------------------------------

from shapely.geometry import Point, Polygon
from geopy.distance import distance
import numpy as np
import pandas as pd
import yfinance as yf

# -------------------------
# Exercise 14: Defining Two or More Polygons
# -------------------------
print("\n--- Exercise 14: Defining Two or More Polygons ---")

coords1 = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395, 38.997684),
           (46.073822, 39.007297), (46.081741, 39.008842)]
coords2 = [(40.102991, 35.977384), (40.065489, 35.977599), (40.109395, 35.997684),
           (40.073822, 36.007297), (40.081741, 36.008842)]

poly1 = Polygon(coords1)
poly2 = Polygon(coords2)

cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
pick_up = Point(46.080074, 38.991289)
cabs = {'cab_26': cab_26, 'cab_112': cab_112}
polygons = {'Area1': poly1, 'Area2': poly2}
cabs_dict = {}

for area_name, poly in polygons.items():
    if pick_up.within(poly):
        cabs_dict[area_name] = []
        for cab_name, cab in cabs.items():
            if cab.within(poly):
                cabs_dict[area_name].append(cab_name)
        break

if not cabs_dict:
    print("Pickup location is not within any defined area.")
else:
    dists = {}
    for cab_name in list(cabs_dict.values())[0]:
        dist_m = distance((pick_up.y, pick_up.x), (cabs[cab_name].y, cabs[cab_name].x)).m
        dists[cab_name] = round(dist_m)
    closest_cab = min(dists, key=dists.get)
    print("Grouped cab dictionary:", cabs_dict)
    print("Distances (in meters):", dists)
    print("The closest cab is:", closest_cab, "with a distance of", dists[closest_cab], "meters")

# -------------------------
# Exercise 15: Further Improving the Pick-Up Algorithm
# -------------------------
print("\n--- Exercise 15: Further Improving the Pick-Up Algorithm ---")

coords = [(46.082991, 38.987384), (46.075489, 38.987599), (46.079395, 38.997684),
          (46.073822, 39.007297), (46.081741, 39.008842)]
area_polygon = Polygon(coords)

cab_26 = Point(46.073852, 38.991890)
cab_112 = Point(46.078228, 39.003949)
cabs = [cab_26, cab_112]
cabs_names = ['cab_26', 'cab_112']
pick_up = Point(46.080074, 38.991289)
entry_point = Point(46.075357, 39.000298)

closest_dist = float('inf')
closest_cab = ''

for i, cab in enumerate(cabs):
    if cab.within(area_polygon):
        dist = distance((pick_up.x, pick_up.y), (cab.x, cab.y)).m
    else:
        dist = distance((cab.x, cab.y), (entry_point.x, entry_point.y)).m + \
               distance((entry_point.x, entry_point.y), (pick_up.x, pick_up.y)).m
    print(f"{cabs_names[i]}: {round(dist)} meters")

    if dist < closest_dist:
        closest_dist = dist
        closest_cab = cabs_names[i]

print(f"Closest cab: {closest_cab} ({round(closest_dist)} meters)")

# -------------------------
# Exercise 16: Filtering Data with a List Comprehension
# -------------------------
print("\n--- Exercise 16: Filtering Data with a List Comprehension ---")

orders = [
    ('order_039', 'open', 'cab_14'),
    ('order_034', 'open', 'cab_79'),
    ('order_032', 'open', 'cab_104'),
    ('order_026', 'closed', 'cab_79'),
    ('order_021', 'open', 'cab_45'),
    ('order_018', 'closed', 'cab_26'),
    ('order_008', 'closed', 'cab_112')
]

unavailable_list = [x[2] for x in orders if x[1] == 'open']
print("Unavailable Cabs:", unavailable_list)

# -------------------------
# Exercise 17: Adding More Metrics to Analyze Dependencies
# -------------------------
print("\n--- Exercise 17: Adding More Metrics to Analyze Dependencies ---")

ticker = 'TSLA'
tkr = yf.Ticker(ticker)
df = tkr.history(period='1mo')
df = df[['Close', 'Volume']].rename(columns={'Close': 'Price'})

df['priceRise'] = np.log(df['Price'] / df['Price'].shift(1))
df['volumeRise'] = np.log(df['Volume'] / df['Volume'].shift(1))
df['volumeSum'] = df['Volume'].shift(1).rolling(2).sum().fillna(0).astype(int)
df['nextVolume'] = df['Volume'].shift(-1).fillna(0).astype(int)
df['priceTrend'] = df['priceRise'].shift(1).rolling(2).sum().fillna(0)

volatility_df = df[abs(df['priceRise']) > 0.05].replace(0, np.nan).dropna()

print("Days with Price Volatility > 5%:\n")
print(volatility_df[['Price', 'Volume', 'priceRise', 'priceTrend',
                     'volumeRise', 'volumeSum', 'nextVolume']])
