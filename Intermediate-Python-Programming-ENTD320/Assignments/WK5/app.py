# Author: Sean Coggeshall
#
# Flask calculator app with SQLite database integration. Performs arithmetic
# operations via RESTful routes and an HTML form, saves calculations to a
# database, and provides a history page to review past computations.

from flask import Flask, render_template, request
import sqlite3
import os
import datetime

app = Flask(__name__)

# Check that the database directory exists
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, 'w5_sean_coggeshall.db')

# Initialize the database
def init_db():
    """Create the calculations table if it doesn't exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS calculations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_number REAL NOT NULL,
        second_number REAL NOT NULL,
        operation TEXT NOT NULL,
        result TEXT NOT NULL,
        timestamp TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize database when the app starts
init_db()

class Use_Calculator:
    """Class for basic arithmetic operations with private methods."""

    def __add(self, first_number, second_number):
        return first_number + second_number

    def __sub(self, first_number, second_number):
        return first_number - second_number

    def __mul(self, first_number, second_number):
        return first_number * second_number

    def __div(self, first_number, second_number):
        return "You cannot divide by Zero" if second_number == 0 else first_number / second_number

    def allInOneDict(self, first_number, second_number):
        return {
            "add": self.__add(first_number, second_number),
            "sub": self.__sub(first_number, second_number),
            "mul": self.__mul(first_number, second_number),
            "div": self.__div(first_number, second_number)
        }

    def allInOneList(self, first_number, second_number):
        return [
            self.__add(first_number, second_number),
            self.__sub(first_number, second_number),
            self.__mul(first_number, second_number),
            self.__div(first_number, second_number)
        ]

calculator = Use_Calculator()

@app.route("/")
def home():
    """Default route with instructions."""
    return (
        "<h2>Welcome to Week 5: Database Calculator</h2>"
        "<p>RESTful Routes Examples:</p>"
        "<ul>"
        "<li>Add: <code>/mycalc/add/7/5/</code></li>"
        "<li>Subtract: <code>/mycalc/sub/14/7/</code></li>"
        "<li>Multiply: <code>/mycalc/mult/6/3/</code></li>"
        "<li>Divide: <code>/mycalc/div/10/2/</code></li>"
        "<li>All operations (Dict): <code>/mycalc/allInOneDict/8/4/</code></li>"
        "<li>All operations (List): <code>/mycalc/allInOneList/8/4/</code></li>"
        "</ul>"
        "<p>To use the form: <a href='/form'>Click here</a></p>"
        "<p>To view calculation history: <a href='/history'>Click here</a></p>"
    )

# RESTful Routes for individual operations
@app.route("/mycalc/add/<int:first_number>/<int:second_number>/")
def calc_add(first_number, second_number):
    result = calculator.allInOneDict(first_number, second_number)['add']
    return f"{first_number} + {second_number} = {result}"

@app.route("/mycalc/sub/<int:first_number>/<int:second_number>/")
def calc_sub(first_number, second_number):
    result = calculator.allInOneDict(first_number, second_number)['sub']
    return f"{first_number} - {second_number} = {result}"

@app.route("/mycalc/mult/<int:first_number>/<int:second_number>/")
def calc_mult(first_number, second_number):
    result = calculator.allInOneDict(first_number, second_number)['mul']
    return f"{first_number} * {second_number} = {result}"

@app.route("/mycalc/div/<int:first_number>/<int:second_number>/")
def calc_div(first_number, second_number):
    result = calculator.allInOneDict(first_number, second_number)['div']
    return f"{first_number} / {second_number} = {result}"

# RESTful Routes for all operations
@app.route("/mycalc/allInOneDict/<int:first_number>/<int:second_number>/")
def calc_all_dict(first_number, second_number):
    results = calculator.allInOneDict(first_number, second_number)
    return "<br>".join([f"{op}: {val}" for op, val in results.items()])

@app.route("/mycalc/allInOneList/<int:first_number>/<int:second_number>/")
def calc_all_list(first_number, second_number):
    results = calculator.allInOneList(first_number, second_number)
    labels = ["Addition", "Subtraction", "Multiplication", "Division"]
    return "<br>".join([f"{label}: {val}" for label, val in zip(labels, results)])

# Route for the HTML form
@app.route("/form")
def show_form():
    """Render the initial form with empty values."""
    return render_template('index.html', result={"fnum": "", "snum": "", "hid": ""}, retres="")

# Function to save calculation to database
def save_calculation(first_number, second_number, operation, result):
    """Save the calculation details to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
    INSERT INTO calculations (first_number, second_number, operation, result, timestamp) 
    VALUES (?, ?, ?, ?, ?)
    ''', (first_number, second_number, operation, str(result), timestamp))
    
    conn.commit()
    conn.close()

# Route to handle form submission
@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle form submission and calculate the result."""
    if request.method == 'POST':
        result = request.form
        try:
            fnum = float(result["fnum"])
            snum = float(result["snum"])
            operation = result["hid"]

            calc_results = calculator.allInOneDict(fnum, snum)
            
            if operation == "add":
                calc_result = calc_results['add']
                retres = f"add res = {calc_result}"
            elif operation == "sub":
                calc_result = calc_results['sub']
                retres = f"sub res = {calc_result}"
            elif operation == "mult":
                calc_result = calc_results['mul']
                retres = f"mult res = {calc_result}"
            elif operation == "div":
                calc_result = calc_results['div']
                retres = f"div res = {calc_result}"
            elif operation == "allInOneDict":
                # Format dict results as a simple string
                result_string = " | ".join([f"{op}: {val}" for op, val in calc_results.items()])
                calc_result = result_string
                retres = result_string
            elif operation == "allInOneList":
                # Format list results as a simple string
                labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                all_results = calculator.allInOneList(fnum, snum)
                result_string = " | ".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
                calc_result = result_string
                retres = result_string
            elif operation == "save":
                # Get the last operation from the form
                last_op = result.get("last_operation", "add")
                if last_op == "add":
                    calc_result = calc_results['add']
                    retres = f"add res = {calc_result} (Saved)"
                elif last_op == "sub":
                    calc_result = calc_results['sub']
                    retres = f"sub res = {calc_result} (Saved)"
                elif last_op == "mult":
                    calc_result = calc_results['mul']
                    retres = f"mult res = {calc_result} (Saved)"
                elif last_op == "div":
                    calc_result = calc_results['div']
                    retres = f"div res = {calc_result} (Saved)"
                elif last_op == "allInOneDict":
                    result_string = " | ".join([f"{op}: {val}" for op, val in calc_results.items()])
                    calc_result = result_string
                    retres = f"{result_string} (Saved)"
                elif last_op == "allInOneList":
                    labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                    all_results = calculator.allInOneList(fnum, snum)
                    result_string = " | ".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
                    calc_result = result_string
                    retres = f"{result_string} (Saved)"
                else:
                    calc_result = "Unknown operation"
                    retres = "Unknown operation"
                
                # Save the calculation to the database
                save_calculation(fnum, snum, last_op, calc_result)
                
                # Update the operation for display purposes
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

# Route to display calculation history
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

if __name__ == "__main__":
    app.run(debug=True)