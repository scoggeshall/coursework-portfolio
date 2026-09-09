# Author: Sean Coggeshall
#
# Flask calculator app with both RESTful URL routes and an HTML form interface.
# Supports add, sub, mult, div operations plus allInOneDict and allInOneList
# aggregate results, rendered via a Jinja2 template.

from flask import Flask, render_template, request

app = Flask(__name__)

# Define the class with encapsulated arithmetic operations
class Use_Calculator:
    """Class for basic arithmetic operations with private methods."""

    # Private method for addition
    def __add(self, first_number, second_number):
        return first_number + second_number

    # Private method for subtraction
    def __sub(self, first_number, second_number):
        return first_number - second_number

    # Private method for multiplication
    def __mul(self, first_number, second_number):
        return first_number * second_number

    # Private method for division with zero handling
    def __div(self, first_number, second_number):
        return "You cannot divide by Zero" if second_number == 0 else first_number / second_number

    # Public method returning results in a dictionary
    def allInOneDict(self, first_number, second_number):
        return {
            "add": self.__add(first_number, second_number),
            "sub": self.__sub(first_number, second_number),
            "mul": self.__mul(first_number, second_number),
            "div": self.__div(first_number, second_number)
        }

    # Public method returning results in a list
    def allInOneList(self, first_number, second_number):
        return [
            self.__add(first_number, second_number),
            self.__sub(first_number, second_number),
            self.__mul(first_number, second_number),
            self.__div(first_number, second_number)
        ]

# Create an instance of the calculator class
calculator = Use_Calculator()

@app.route("/")
def home():
    return (
        "<h2>Hello ENTD320, Welcome to my Restful webservices calculator</h2>"
        "<p>Examples:</p>"
        "<p>To add two numbers: <code>/mycalc/add/7/5/</code></p>"
        "<p>To subtract two numbers: <code>/mycalc/sub/14/7/</code></p>"
        "<p>To multiply two numbers: <code>/mycalc/mult/6/3/</code></p>"
        "<p>To divide two numbers: <code>/mycalc/div/10/2/</code></p>"
        "<p>To get all operations as dictionary: <code>/mycalc/allInOneDict/8/4/</code></p>"
        "<p>To get all operations as list: <code>/mycalc/allInOneList/8/4/</code></p>"
        "<p>To access the form: <code>/form</code></p>"
    )

# RESTful Routes
@app.route("/mycalc/add/<int:first_number>/<int:second_number>/")
def calc_add(first_number, second_number):
    return f"{first_number} + {second_number} = {calculator.allInOneDict(first_number, second_number)['add']}"

@app.route("/mycalc/sub/<int:first_number>/<int:second_number>/")
def calc_sub(first_number, second_number):
    return f"{first_number} - {second_number} = {calculator.allInOneDict(first_number, second_number)['sub']}"

@app.route("/mycalc/mult/<int:first_number>/<int:second_number>/")
def calc_mult(first_number, second_number):
    return f"{first_number} * {second_number} = {calculator.allInOneDict(first_number, second_number)['mul']}"

@app.route("/mycalc/div/<int:first_number>/<int:second_number>/")
def calc_div(first_number, second_number):
    return f"{first_number} / {second_number} = {calculator.allInOneDict(first_number, second_number)['div']}"

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
    return render_template("index.html")

# Route to handle form submission
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        first_number = float(request.form["first_number"])
        second_number = float(request.form["second_number"])
        operation = request.form["operation"]

        if operation == "add":
            result = f"{first_number} + {second_number} = {calculator.allInOneDict(first_number, second_number)['add']}"
        elif operation == "sub":
            result = f"{first_number} - {second_number} = {calculator.allInOneDict(first_number, second_number)['sub']}"
        elif operation == "mult":
            result = f"{first_number} * {second_number} = {calculator.allInOneDict(first_number, second_number)['mul']}"
        elif operation == "div":
            result = f"{first_number} / {second_number} = {calculator.allInOneDict(first_number, second_number)['div']}"
        elif operation == "allInOneDict":
            result = calculator.allInOneDict(first_number, second_number)  # Keep as dict
        elif operation == "allInOneList":
            result = calculator.allInOneList(first_number, second_number)  # Keep as list
        else:
            result = "Invalid operation."
    except ValueError:
        result = "Invalid input. Please enter valid numbers."

    return render_template("index.html", result=result, operation=operation)

if __name__ == "__main__":
    app.run(debug=True)
