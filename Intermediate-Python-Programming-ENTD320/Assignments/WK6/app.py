# Author: Sean Coggeshall
#
# Flask calculator app with SQLite database and unit testing. Includes a full
# unittest suite validating all arithmetic operations, plus RESTful routes,
# HTML form interface, and calculation history stored in a database.

from flask import Flask, render_template, request
import sqlite3
import os
import datetime
import unittest

app = Flask(__name__)

# Database setup: using the Week 6 folder structure
DB_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(DB_DIR, 'w6_sean_coggeshall.db')

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
        timestamp TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
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

##############################
# UNIT TESTS
##############################

class TestCalculator(unittest.TestCase):
    """Unit tests for Use_Calculator class methods."""

    # Tests for __add
    def test_add_pass(self):
        """Test addition: 2 + 3 = 5 (Pass)"""
        self.assertEqual(calculator._Use_Calculator__add(2, 3), 5)
        print("test_add_pass: 2 + 3 = 5 (Passed)")

    def test_add_fail(self):
        """Test addition: 2 + 3 != 6 (Pass)"""
        self.assertNotEqual(calculator._Use_Calculator__add(2, 3), 6)
        print("test_add_fail: 2 + 3 != 6 (Passed)")

    # Tests for __sub
    def test_sub_pass(self):
        """Test subtraction: 5 - 3 = 2 (Pass)"""
        self.assertEqual(calculator._Use_Calculator__sub(5, 3), 2)  
        print("test_sub_pass: 5 - 3 = 2 (Passed)")  

    def test_sub_fail(self):
        """Test subtraction: 5 - 3 != 1 (Pass)"""
        self.assertNotEqual(calculator._Use_Calculator__sub(5, 3), 1)
        print("test_sub_fail: 5 - 3 != 1 (Passed)")

    # Tests for __mul
    def test_mul_pass(self):
        """Test multiplication: 2 * 3 = 6 (Pass)"""
        self.assertEqual(calculator._Use_Calculator__mul(2, 3), 6)
        print("test_mul_pass: 2 * 3 = 6 (Passed)")

    def test_mul_fail(self):
        """Test multiplication: 2 * 3 != 5 (Pass)"""
        self.assertNotEqual(calculator._Use_Calculator__mul(2, 3), 5)
        print("test_mul_fail: 2 * 3 != 5 (Passed)")

    # Tests for __div
    def test_div_pass(self):
        """Test division: 6 / 3 = 2 (Pass)"""
        self.assertEqual(calculator._Use_Calculator__div(6, 3), 2)
        print("test_div_pass: 6 / 3 = 2 (Passed)")

    def test_div_fail(self):
        """Test division: 6 / 3 != 3 (Pass)"""
        self.assertNotEqual(calculator._Use_Calculator__div(6, 3), 3)
        print("test_div_fail: 6 / 3 != 3 (Passed)")

    def test_div_by_zero(self):
        """Test division by zero: 5 / 0 returns appropriate message (Pass)"""
        self.assertEqual(calculator._Use_Calculator__div(5, 0), "You cannot divide by Zero")
        print("test_div_by_zero: 5 / 0 = 'You cannot divide by Zero' (Passed)")

    # Tests for allInOneDict
    def test_allInOneDict_pass(self):
        """Test allInOneDict returns correct results (Pass)."""
        expected = {"add": 5, "sub": 1, "mul": 6, "div": 1.5}  
        self.assertEqual(calculator.allInOneDict(3, 2), expected)
        print("test_allInOneDict_pass: 3, 2 ->", expected, "(Passed)")

    def test_allInOneDict_fail(self):
        """Test allInOneDict does not return incorrect results (Pass)."""
        expected = {"add": 5, "sub": 1, "mul": 6, "div": 2}  
        self.assertNotEqual(calculator.allInOneDict(3, 2), expected)
        print("test_allInOneDict_fail: 3, 2 != ", expected, "(Passed)")

    # Tests for allInOneList
    def test_allInOneList_pass(self):
        """Test allInOneList returns correct results (Pass)."""
        expected = [5, 1, 6, 1.5]  
        self.assertEqual(calculator.allInOneList(3, 2), expected)
        print("test_allInOneList_pass: 3, 2 ->", expected, "(Passed)")

    def test_allInOneList_fail(self):
        """Test allInOneList does not return incorrect results (Pass)."""
        expected = [5, 1, 6, 2]  
        self.assertNotEqual(calculator.allInOneList(3, 2), expected)
        print("test_allInOneList_fail: 3, 2 != ", expected, "(Passed)")

##############################
# FLASK APPLICATION CODE BELOW
##############################

@app.route("/")
def home():
    """Default route with instructions for the database calculator."""
    return (
        "<h2>Welcome to Week 6: Database Calculator</h2>"
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
    """Render the initial calculator form."""
    return render_template('index.html', result={"fnum": "", "snum": "", "hid": ""}, retres="")

def save_calculation(first_number, second_number, operation, result):
    """Save calculation details to the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''INSERT INTO calculations (first_number, second_number, operation, result, timestamp)
                      VALUES (?, ?, ?, ?, ?)''', (first_number, second_number, operation, str(result), timestamp))
    conn.commit()
    conn.close()

@app.route("/calculate", methods=["POST"])
def calculate():
    """Handle form submission and perform calculations."""
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
                result_string = " | ".join([f"{op}: {val}" for op, val in calc_results.items()])
                calc_result = result_string
                retres = result_string
            elif operation == "allInOneList":
                labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                all_results = calculator.allInOneList(fnum, snum)
                result_string = " | ".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
                calc_result = result_string
                retres = result_string
            elif operation == "save":
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
                save_calculation(fnum, snum, last_op, calc_result)
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
    # Run unit tests first, then start the Flask app
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
    app.run(debug=True)