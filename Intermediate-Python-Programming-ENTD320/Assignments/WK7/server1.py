# Author: Sean Coggeshall
#
# Microservice 1: Basic Calculator API. A Flask service exposing JSON POST
# endpoints for individual arithmetic operations (add, sub, mul, div).
# Saves each calculation to a shared SQLite database.

from flask import Flask, jsonify, request
import sqlite3
import os
import datetime

app = Flask(__name__)

# Database setup
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, 'w7_sean_coggeshall.db')

def init_db():
    """Initialize the database by creating the calculations table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_number REAL NOT NULL,
        second_number REAL NOT NULL,
        operation TEXT NOT NULL,
        result TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        service TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

class BasicCalculator:
    """Class for basic arithmetic operations."""
    def add(self, first_number, second_number):
        return first_number + second_number

    def sub(self, first_number, second_number):
        return first_number - second_number

    def mul(self, first_number, second_number):
        return first_number * second_number

    def div(self, first_number, second_number):
        return "You cannot divide by Zero" if second_number == 0 else first_number / second_number

calculator = BasicCalculator()

def save_calculation(first_number, second_number, operation, result):
    """Save calculation details to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO calculations (first_number, second_number, operation, result, timestamp, service)
                      VALUES (?, ?, ?, ?, ?, ?)''', (first_number, second_number, operation, str(result), timestamp, "Service1"))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    """Default route with instructions for the basic calculator service."""
    return (
        "<h2>Welcome to Service 1: Basic Calculator Microservice</h2>"
        "<p>Available endpoints:</p>"
        "<ul>"
        "<li>Add: <code>/add</code> (POST)</li>"
        "<li>Subtract: <code>/sub</code> (POST)</li>"
        "<li>Multiply: <code>/mul</code> (POST)</li>"
        "<li>Divide: <code>/div</code> (POST)</li>"
        "</ul>"
        "<p>All endpoints expect a JSON payload with 'first_number' and 'second_number' fields.</p>"
    )

@app.route("/add", methods=["POST"])
def api_add():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    result = calculator.add(first_number, second_number)
    save_calculation(first_number, second_number, "add", result)
    return jsonify({"result": result})

@app.route("/sub", methods=["POST"])
def api_sub():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    result = calculator.sub(first_number, second_number)
    save_calculation(first_number, second_number, "sub", result)
    return jsonify({"result": result})

@app.route("/mul", methods=["POST"])
def api_mul():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    result = calculator.mul(first_number, second_number)
    save_calculation(first_number, second_number, "mul", result)
    return jsonify({"result": result})

@app.route("/div", methods=["POST"])
def api_div():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    result = calculator.div(first_number, second_number)
    save_calculation(first_number, second_number, "div", result)
    return jsonify({"result": result})

if __name__ == "__main__":
    print("Starting Service 1: Basic Calculator Microservice")
    app.run(host='0.0.0.0', port=5001, debug=True)