"""
Week 1 Assignment: Python Data Fundamentals
Author: Sean Coggeshall

Demonstrates core Python data structures and libraries including set operations
for photo tag analysis, NumPy array operations for salary statistics, Pandas
Series/DataFrame construction, and various join strategies (inner, outer) for
combining employee and salary data.
"""

#EXERCISE #1: IMPROVED PHOTO TAG ANALYSIS
photo_list = [
    {
        "name": "photo1.jpg",
        "tags": {'coffee', 'breakfast', 'drink', 'table', 'tableware', 'cup', 'food'}
    },
    {
        "name": "photo2.jpg",
        "tags": {'food', 'dish', 'meat', 'meal', 'tableware', 'dinner', 'vegetable'}
    },
    {
        "name": "photo3.jpg",
        "tags": {'city', 'skyline', 'cityscape', 'skyscraper', 'architecture', 'building', 'travel'}
    },
    {
        "name": "photo4.jpg",
        "tags": {'drink', 'juice', 'glass', 'meal', 'fruit', 'food', 'grapes'}
    }
]

def intersection(tags1, tags2):
    return "_".join([tag for tag in tags1 if tag in tags2])

photo_groups = {}

for i in range(1, len(photo_list)):
    for j in range(i + 1, len(photo_list) + 1):
        print(f"Processing intersection: {photo_list[i-1]['name']} and {photo_list[j-1]['name']}")
        common_key = intersection(photo_list[i-1]["tags"], photo_list[j-1]["tags"])
        if common_key:
            photo_groups.setdefault(common_key, list((photo_list[i-1]["name"], photo_list[j-1]["name"])))

print("\nPhoto groups based on common tags:")
print(photo_groups)

#EXERCISE 2: USING NUMPY STATISTICAL FUNCTIONS
import numpy as np

# Base salaries
jeff_salary = [2700, 3000, 3000]
nick_salary = [2600, 2800, 2800]
tom_salary = [2300, 2500, 2500]
base_salary = np.array([jeff_salary, nick_salary, tom_salary])

# Bonuses
jeff_bonus = [500, 400, 400]
nick_bonus = [600, 300, 400]
tom_bonus = [200, 500, 400]
bonus = np.array([jeff_bonus, nick_bonus, tom_bonus])

# Calculate total salary (base salary + bonus)
total_salary = base_salary + bonus

print("\nType of total_salary array:", type(total_salary))
print("\nTotal Salary (Base + Bonus):\n", total_salary)

max_salary_per_month = np.amax(total_salary, axis=0)
print("\nMaximum salary per month:", max_salary_per_month)

overall_max_salary = np.amax(max_salary_per_month)
print("\nHighest salary recorded:", overall_max_salary)

avg_max_salary = np.average(max_salary_per_month)
print("\nAverage of max salaries per month:", avg_max_salary)

#EXERCISE 3: COMBINING THREE SERIES
import pandas as pd

email_data = ['jeff.russell', 'jane.boorman', 'tom.heints']
emps_emails = pd.Series(email_data, index=[9001, 9002, 9003], name='emails')

name_data = ['jeff.russell', 'jane.boorman', 'tom.heints']
emps_names = pd.Series(name_data, index=[9001, 9002, 9003], name='names')

phone_data = ['+1 246 111-xxxx', '+1 246 222-xxxx', '+1 246 333-xxxx']
emps_phones = pd.Series(phone_data, index=[9001, 9002, 9003], name='phones')

employee_df = pd.concat([emps_names, emps_emails, emps_phones], axis=1)

print("\nEmployee DataFrame:")
print(employee_df)

#Exercise 4: Using Different Joins
import json
import pandas as pd

# Load salary data from JSON
data = [
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]
json_data = json.dumps(data)
salary = pd.DataFrame([
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]).set_index('Empno')

print("\nSalary Data:")
print(salary)

# Load employee data
emp_data = [['9001', 'Jeff Russell', 'sales'],
            ['9002', 'Jane Boorman', 'sales'],
            ['9003', 'Tom Heints', 'sales']]
employees = pd.DataFrame(emp_data, columns=['Empno', 'Name', 'Job'])
col_types = {'Empno': int, 'Name': str, 'Job': str}
employees = employees.astype(col_types)
employees = employees.set_index('Empno')

print("\nEmployee Data:")
print(employees)

emps_salary = employees.join(salary)

print("\nEmployees with Salaries (Inner Join):")
print(emps_salary)

# Adding a new employee (using pd.concat instead of append)
new_employee = pd.Series({'Name': 'John Hardy', 'Job': 'sales'}, name=9004)
employees = pd.concat([employees, pd.DataFrame([new_employee])])

emps_salary = employees.join(salary, how='inner')

print("\nUpdated Employees with Salaries (After Adding John Hardy):")
print(emps_salary)

# Adding a new salary record (using pd.concat instead of append)
new_salary = pd.Series({'Salary': 2400}, name=9006)
salary = pd.concat([salary, pd.DataFrame([new_salary])])

emps_salary = employees.join(salary, how='inner')

print("\nUpdated Employees with Salaries (After Adding Salary for Emp 9006):")
print(emps_salary)

emps_salary = employees.join(salary, how='outer')

print("\nFinal Employee-Salary Data (Outer Join):")
print(emps_salary)

#EXERCISE 4: USING DIFFERENT JOINS (Alternate Implementation)
import pandas as pd

# Load salary data into a DataFrame
salary_df = pd.DataFrame([
    {"Empno": 9001, "Salary": 3000},
    {"Empno": 9002, "Salary": 2800},
    {"Empno": 9003, "Salary": 2500}
]).set_index('Empno')

print("\nSalary Data:")
print(salary_df)

employees_df = pd.DataFrame([
    [9001, 'Jeff Russell', 'sales'],
    [9002, 'Jane Boorman', 'sales'],
    [9003, 'Tom Heints', 'sales']
], columns=['Empno', 'Name', 'Job']).set_index('Empno')

print("\nEmployee Data:")
print(employees_df)

emps_salary = employees_df.join(salary_df)

print("\nEmployees with Salaries (Inner Join):")
print(emps_salary)

# Adding a new employee (using pd.concat instead of append)
new_employee_df = pd.DataFrame({'Name': ['John Hardy'], 'Job': ['sales']}, index=[9004])
employees_df = pd.concat([employees_df, new_employee_df])

emps_salary = employees_df.join(salary_df, how='inner')

print("\nUpdated Employees with Salaries (After Adding John Hardy):")
print(emps_salary)

# Adding a new salary record (using pd.concat instead of append)
new_salary_df = pd.DataFrame({'Salary': [2400]}, index=[9006])
salary_df = pd.concat([salary_df, new_salary_df])

emps_salary = employees_df.join(salary_df, how='inner')

print("\nUpdated Employees with Salaries (After Adding Salary for Emp 9006):")
print(emps_salary)

emps_salary = employees_df.join(salary_df, how='outer')

print("\nFinal Employee-Salary Data (Outer Join):")
print(emps_salary)
