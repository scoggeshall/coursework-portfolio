"""
Week 3 Assignment: DataFrames and NumPy Arrays
Author: Sean Coggeshall

Demonstrates advanced Pandas DataFrame operations including multi-level
grouping with subtotals, filtering aggregated rows from a sales dataset,
and NumPy array manipulation (concatenation, computed columns, appending
rows) for employee salary analysis.
"""

# EXERCISE 10: EXCLUDING TOTAL ROWS FROM THE DATAFRAME
import pandas as pd

# Step 1: Create DataFrames from sample data
orders = [
    (9423517, '2021-08-04', 9001), (4626232, '2021-08-04', 9003), (9423534, '2021-08-04', 9001),
    (9423679, '2021-08-05', 9002), (4626377, '2021-08-05', 9003), (4626412, '2021-08-05', 9004),
    (9423783, '2021-08-06', 9002), (4626490, '2021-08-06', 9004)
]
df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])

details = [
    (9423517, 'Jeans', 'Rip Curl', 87.0, 1), (9423517, 'Jacket', 'The North Face', 112.0, 1),
    (4626232, 'Socks', 'Vans', 15.0, 1), (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
    (9423534, 'Socks', 'DC', 10.0, 2), (9423534, 'Socks', 'Quiksilver', 12.0, 2),
    (9423679, 'T-shirt', 'Patagonia', 35.0, 1), (4626377, 'Hoody', 'Animal', 44.0, 1),
    (4626377, 'Cargo Shorts', 'Animal', 38.0, 1), (4626412, 'Shirt', 'Volcom', 78.0, 1),
    (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2), (9423783, 'Shorts', 'Globe', 26.0, 1),
    (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1), (4626490, 'Sweater', 'Dickies', 56.0, 1)
]
df_details = pd.DataFrame(details, columns=['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])

emps = [
    (9001, 'Jeff Russell', 'LA'), (9002, 'Nick Boorman', 'San Francisco'),
    (9003, 'Tom Heints', 'NYC'), (9004, 'Maya Silver', 'Philadelphia')
]
df_emps = pd.DataFrame(emps, columns=['Empno', 'Empname', 'Location'])

locations = [
    ('LA', 'West'), ('San Francisco', 'West'), ('NYC', 'East'), ('Philadelphia', 'East')
]
df_locations = pd.DataFrame(locations, columns=['Location', 'Region'])

# Step 2: Merge DataFrames and calculate totals per order line
df_sales = df_orders.merge(df_details)
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
print("\n--- EXERCISE 10: Raw Sales Data ---")
print(df_sales)
df_sales = df_sales[['Date', 'Empno', 'Total']]

df_sales_emps = df_sales.merge(df_emps, on='Empno')
df_result = df_sales_emps.merge(df_locations, on='Location')
df_result = df_result[['Date', 'Region', 'Total']]

# Step 3: Group by Date and Region, then aggregate
df_date_region = df_result.groupby(['Date', 'Region']).sum()

# Step 4: Add subtotal and grand total rows
ps = df_date_region.sum(axis=0)
ps.name = ('All', 'All')
df_date_region_total = pd.concat([df_date_region, ps.to_frame().T])

df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level=0):
    df_totals = pd.concat([df_totals, date_df])
    subtotal = date_df.sum(axis=0)
    subtotal.name = (date, 'All')
    df_totals = pd.concat([df_totals, subtotal.to_frame().T])
df_totals = pd.concat([df_totals, df_date_region_total.loc[[('All', 'All')]]])
df_totals.sort_index(ascending=True, inplace=True)

print("\n--- EXERCISE 10: DataFrame With Totals ---")
print(df_totals)

# Step 5: Exclude subtotal and grand total rows
valid_dates = df_totals.index.get_level_values(0).unique().tolist()
valid_dates.remove('All')
valid_regions = ['East', 'West']
filtered_df = df_totals.loc[(slice(valid_dates[0], valid_dates[-1]), valid_regions), :]

print("\n--- EXERCISE 10: Filtered DataFrame (Excluding Totals) ---")
print(filtered_df)

# ------------------------------------------------------------------------------

# EXERCISE 11: ADDING NEW ROWS/COLUMNS TO A NUMPY ARRAY
import numpy as np

# Step 1: Base salaries for 3 employees (first 3 months)
jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary  = [2300, 2500, 2500]
base_salary1 = np.array([jeff_salary, nick_salary, tom_salary])

# Step 2: Base salaries for 2 more employees
maya_salary = [2200, 2400, 2400]
john_salary = [2500, 2700, 2700]
base_salary2 = np.array([maya_salary, john_salary])

# Combine all 5 employees
base_salary = np.concatenate((base_salary1, base_salary2), axis=0)

# Step 3: Add 4th month salaries
month_4 = np.array([[3000], [2900], [2500], [2500], [2700]])
base_salary = np.concatenate((base_salary, month_4), axis=1)

# Step 4: Add two more months using a 5% raise
month_5 = base_salary[:, -1] * 1.05
month_6 = month_5 * 1.05
month_5_6 = np.column_stack((month_5, month_6))
base_salary = np.concatenate((base_salary, month_5_6), axis=1)

# Step 5: Add new employee row
new_employee = np.array([[2400, 2600, 2600, 2700, 2750, 2850]])
base_salary = np.append(base_salary, new_employee, axis=0)

# Final output
print("\n--- EXERCISE 11: Final base_salary array (6 employees × 6 months) ---")
print(base_salary)
print(f"\nShape: {base_salary.shape}")
