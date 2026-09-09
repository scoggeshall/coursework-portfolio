# Author: Sean Coggeshall
#
# Flask calculator app using Jinja2 template programming. Provides RESTful URL
# routes and an HTML form for performing arithmetic operations, with results
# rendered back into the template.

from flask import Flask, render_template, request

app = Flask(__name__)

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
        "<h2>Welcome to Week 4: Template Programming Calculator</h2>"
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
                retres = f"add res = {calc_results['add']}"
            elif operation == "sub":
                retres = f"sub res = {calc_results['sub']}"
            elif operation == "mult":
                retres = f"mult res = {calc_results['mul']}"
            elif operation == "div":
                retres = f"div res = {calc_results['div']}"
            elif operation == "allInOneDict":
                retres = "<br>".join([f"{op}: {val}" for op, val in calc_results.items()])
            elif operation == "allInOneList":
                labels = ["Addition", "Subtraction", "Multiplication", "Division"]
                all_results = calculator.allInOneList(fnum, snum)
                retres = "<br>".join([f"{label}: {val}" for label, val in zip(labels, all_results)])
            else:
                retres = "Invalid operation"

            return render_template('index.html', result=result, retres=retres)
        except ValueError:
            return render_template('index.html', result=result, retres="Error: Please enter valid numbers")

if __name__ == "__main__":
    app.run(debug=True)