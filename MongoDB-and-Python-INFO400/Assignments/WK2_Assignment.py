"""
Week 2 Assignment: JSON, APIs, Databases, and MongoDB
Author: Sean Coggeshall

Covers JSON file I/O, REST API consumption with the requests library,
complex JSON normalization and reconstruction with Pandas, one-to-many
SQL joins using MySQL Connector, and inserting/querying documents in
MongoDB with PyMongo.
"""

#Exercise 5: Opening JSON Files
import json

cars_data = {
    "cars": [
        {"Year": "1997", "Make": "Ford", "Model": "E350", "Price": "3200.00"},
        {"Year": "1999", "Make": "Chevy", "Model": "Venture", "Price": "4800.00"},
        {"Year": "1996", "Make": "Jeep", "Model": "Grand Cherokee", "Price": "4900.00"}
    ]
}

with open("cars.json", "w") as json_file:
    json.dump(cars_data, json_file, indent=4)

with open("cars.json", "r") as json_file:
    cars_obj = json.load(json_file)

for car in cars_obj["cars"]:
    for key, value in car.items():
        print(f"{key}: {value}")
    print("\n")


#Exercise 6: Accessing an API with Requests
import requests
import json

params = {
    'q': 'Python programming language',
    'apiKey': 'YOUR_API_KEY_HERE',
    'pageSize': 5
}

response = requests.get('https://newsapi.org/v2/everything', params=params)

news_data = response.json()

if 'articles' in news_data:
    for article in news_data['articles']:
        print(f"Title: {article['title']}")
        print(f"Published Date: {article['publishedAt']}")
        print(f"URL: {article['url']}\n")
else:
    print("No articles found or invalid API response.")

#Exercise 7: Manipulating Complex JSON Structures
import pandas as pd
import json

data = [
    {"Emp": "Jeff Russell", "Emp_email": "jeff.russell", "POs": [
        {"Pono": 2608, "Total": 35}, {"Pono": 2617, "Total": 35}, {"Pono": 2620, "Total": 139}]},
    {"Emp": "Jane Boorman", "Emp_email": "jane.boorman", "POs": [
        {"Pono": 2621, "Total": 95}, {"Pono": 2626, "Total": 218}]}
]

df = pd.json_normalize(data, "POs", ["Emp", "Emp_email"]).set_index(["Emp", "Emp_email", "Pono"])

df = df.reset_index()

json_doc = (df.groupby(["Emp", "Emp_email"], as_index=True)
            .apply(lambda x: x[["Pono", "Total"]].to_dict("records"), include_groups=False)
            .reset_index()
            .rename(columns={0: "POs"})
            .to_json(orient="records"))

print("Reconstructed JSON:")
print(json.dumps(json.loads(json_doc), indent=2))

total_spend = df.groupby(["Emp", "Emp_email"])["Total"].sum()
print("\nAnalysis - Total Spend per Employee:")
for (emp, email), total in total_spend.items():
    print(f"{emp} ({email}): ${total:.2f}")

#Exercise 8: Performing a One-to-Many Join
import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to the MySQL database
    cnx = mysql.connector.connect(
        user='root', 
        password='YOUR_PASSWORD_HERE',
        host='127.0.0.1', 
        database='sampledb'
    )

    cursor = cnx.cursor()

    # Define SQL query for joining emps and orders table
    query = """SELECT o.pono, e.empname, o.total  
               FROM emps e 
               JOIN orders o ON e.empno = o.empno 
               WHERE e.empno > %s"""

    empno = 9001  # Define the parameter for filtering
    cursor.execute(query, (empno,))  

    # Print output header
    print("\nOrder Number, Employee Name, Order Total")
    print("--------------------------------------")

    # Fetch and print results
    for (pono, empname, total) in cursor:
        print(f"{pono}, {empname}, {total}")

except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))

# Close resources
finally:
 cursor.close()
 cnx.close()
 print("\nDatabase connection closed.")

#Exercise 9: Inserting and Querying Multiple Documents
 from pymongo import MongoClient

try:
    # Connect to MongoDB
    client = MongoClient('localhost', 27017)
    db = client['sampledb']
    emps_collection = db['emps']

    # Insert multiple employee records
    employees = [
        {"empno": 9026, "empname": "Bob Dores", "orders": [4608, 4617, 4620]},
        {"empno": 9027, "empname": "Tony Aaron", "orders": [4708, 4717, 4720]}
    ]
    result = emps_collection.insert_many(employees)
    print(f"Inserted document IDs: {result.inserted_ids}")

    # Query and display all employee records
    print("\nAll Employees:")
    for emp in emps_collection.find():
        print(f"Employee ID: {emp['empno']}\nName: {emp['empname']}\nOrders: {', '.join(map(str, emp['orders']))}\n")

except Exception as e:
    print(f"Error: {e}")

finally:
    client.close()

