# Author: Sean Coggeshall
#
# Microservice 2: Advanced Calculator with HTML form interface. Delegates basic
# arithmetic to Service 1 via HTTP, provides allInOneDict/allInOneList aggregate
# operations, and includes a calculation history page backed by SQLite.

from flask import Flask, render_template, request, jsonify
import sqlite3
import os
import datetime
import requests
from multiprocessing import Process
import time

app = Flask(__name__)

# Database setup
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, 'w7_sean_coggeshall.db')

# Service 1 URL
SERVICE1_URL = "http://localhost:5001"

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

class AdvancedCalculator:
    """Class for advanced arithmetic operations that calls Service 1."""
    
    def __init__(self, service1_url):
        self.service1_url = service1_url
    
    def allInOneDict(self, first_number, second_number):
        """Perform all operations and return results as a dictionary."""
        operations = ["add", "sub", "mul", "div"]
        results = {}
        
        for op in operations:
            url = f"{self.service1_url}/{op}"
            payload = {"first_number": first_number, "second_number": second_number}
            response = requests.post(url, json=payload)
            results[op] = response.json()["result"]
        
        return results
    
    def allInOneList(self, first_number, second_number):
        """Perform all operations and return results as a list."""
        operations = ["add", "sub", "mul", "div"]
        results = []
        
        for op in operations:
            url = f"{self.service1_url}/{op}"
            payload = {"first_number": first_number, "second_number": second_number}
            response = requests.post(url, json=payload)
            results.append(response.json()["result"])
        
        return results

calculator = AdvancedCalculator(SERVICE1_URL)

def save_calculation(first_number, second_number, operation, result):
    """Save calculation details to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO calculations (first_number, second_number, operation, result, timestamp, service)
                      VALUES (?, ?, ?, ?, ?, ?)''', (first_number, second_number, operation, str(result), timestamp, "Service2"))
    conn.commit()
    conn.close()

@app.route("/")
def home():
    """Default route with instructions for the advanced calculator service."""
    return (
        "<h2>Welcome to Service 2: Advanced Calculator Microservice</h2>"
        "<p>Available endpoints:</p>"
        "<ul>"
        "<li>All operations (Dict): <code>/allInOneDict</code> (POST)</li>"
        "<li>All operations (List): <code>/allInOneList</code> (POST)</li>"
        "</ul>"
        "<p>To use the calculator form: <a href='/form'>Click here</a></p>"
        "<p>To view calculation history: <a href='/history'>Click here</a></p>"
    )

@app.route("/form")
def show_form():
    """Render the calculator form."""
    return render_template('index.html', result={"fnum": "", "snum": "", "hid": ""}, retres="")

@app.route("/allInOneDict", methods=["POST"])
def api_all_dict():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    results = calculator.allInOneDict(first_number, second_number)
    save_calculation(first_number, second_number, "allInOneDict", str(results))
    return jsonify({"results": results})

@app.route("/allInOneList", methods=["POST"])
def api_all_list():
    data = request.get_json()
    first_number = float(data.get("first_number"))
    second_number = float(data.get("second_number"))
    results = calculator.allInOneList(first_number, second_number)
    save_calculation(first_number, second_number, "allInOneList", str(results))
    return jsonify({"results": results})

@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle form submission and perform calculations."""
    if request.method == 'POST':
        result = request.form
        try:
            fnum = float(result["fnum"])
            snum = float(result["snum"])
            operation = result["hid"]
            
            if operation in ["add", "sub", "mul", "div"]:
                # Call Service 1 for basic operations
                url = f"{SERVICE1_URL}/{operation}"
                payload = {"first_number": fnum, "second_number": snum}
                response = requests.post(url, json=payload)
                calc_result = response.json()["result"]
                retres = f"{operation} res = {calc_result}"
            
            elif operation == "allInOneDict":
                # Call the local allInOneDict method
                calc_results = calculator.allInOneDict(fnum, snum)
                result_string = " | ".join([f"{op}: {val}" for op, val in calc_results.items()])
                calc_result = result_string
                retres = result_string
                save_calculation(fnum, snum, operation, calc_result)
            
            elif operation == "allInOneList":
                # Call the local allInOneList method
                all_results = calculator.allInOneList(fnum, snum)
                labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                result_string = " | ".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
                calc_result = result_string
                retres = result_string
                save_calculation(fnum, snum, operation, calc_result)
            
            elif operation == "save":
                last_op = result.get("last_operation", "add")
                
                if last_op in ["add", "sub", "mul", "div"]:
                    # Call Service 1 for basic operations
                    url = f"{SERVICE1_URL}/{last_op}"
                    payload = {"first_number": fnum, "second_number": snum}
                    response = requests.post(url, json=payload)
                    calc_result = response.json()["result"]
                    retres = f"{last_op} res = {calc_result} (Saved)"
                
                elif last_op == "allInOneDict":
                    calc_results = calculator.allInOneDict(fnum, snum)
                    result_string = " | ".join([f"{op}: {val}" for op, val in calc_results.items()])
                    calc_result = result_string
                    retres = f"{result_string} (Saved)"
                    save_calculation(fnum, snum, last_op, calc_result)
                
                elif last_op == "allInOneList":
                    all_results = calculator.allInOneList(fnum, snum)
                    labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                    result_string = " | ".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
                    calc_result = result_string
                    retres = f"{result_string} (Saved)"
                    save_calculation(fnum, snum, last_op, calc_result)
                
                else:
                    calc_result = "Unknown operation"
                    retres = "Unknown operation"
                
                operation = last_op
            
            else:
                retres = "Invalid operation"
                calc_result = "Invalid operation"
            
            return render_template('index.html',
                                  result={"fnum": fnum, "snum": snum, "hid": operation},
                                  retres=retres,
                                  last_operation=operation)
        
        except ValueError:
            return render_template('index.html',
                                  result=result,
                                  retres="Error: Please enter valid numbers")
        except requests.exceptions.ConnectionError:
            return render_template('index.html',
                                  result=result,
                                  retres="Error: Service 1 is not available. Please ensure it's running.")

@app.route("/history")
def show_history():
    """Retrieve and display all calculations from the database."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM calculations ORDER BY timestamp DESC')
    calculations = cursor.fetchall()
    conn.close()
    return render_template('history.html', calculations=calculations)

def start_service1():
    """This function would ideally start Service 1, but in practice, both services should be started separately."""
    import subprocess
    subprocess.run(["python", "server1.py"])

if __name__ == "__main__":
    # Start Service 1 in a separate process
    # Note: In a real implementation, you might want to start both services separately
    # service1_process = Process(target=start_service1)
    # service1_process.start()
    
    # Allow time for Service 1 to start up
    # time.sleep(2)
    
    print("Starting Service 2: Advanced Calculator Microservice")
    print("Make sure Service 1 is running at", SERVICE1_URL)
    app.run(host='0.0.0.0', port=5002, debug=True)
    
    # Cleanup
    # service1_process.terminate()
    # service1_process.join()