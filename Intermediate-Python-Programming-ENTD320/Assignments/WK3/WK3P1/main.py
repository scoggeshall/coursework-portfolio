# Author: Sean Coggeshall
#
# RESTful web service calculator built with Flask. Exposes URL-based routes
# for basic arithmetic operations (add, sub, mult, div) and aggregate
# results via allInOneDict and allInOneList endpoints.

from flask import Flask

app = Flask(__name__)

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

calc = Use_Calculator()

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
    )

@app.route("/mycalc/add/<int:first_number>/<int:second_number>/")
def add(first_number, second_number):
    return f"{first_number} + {second_number} = {calc._Use_Calculator__add(first_number, second_number)}"

@app.route("/mycalc/sub/<int:first_number>/<int:second_number>/")
def subtract(first_number, second_number):
    return f"{first_number} - {second_number} = {calc._Use_Calculator__sub(first_number, second_number)}"

@app.route("/mycalc/mult/<int:first_number>/<int:second_number>/")
def multiply(first_number, second_number):
    return f"{first_number} * {second_number} = {calc._Use_Calculator__mul(first_number, second_number)}"

@app.route("/mycalc/div/<int:first_number>/<int:second_number>/")
def divide(first_number, second_number):
    result = calc._Use_Calculator__div(first_number, second_number)
    return f"{first_number} / {second_number} = {result}"

@app.route("/mycalc/allInOneDict/<int:first_number>/<int:second_number>/")
def all_in_one_dict(first_number, second_number):
    results = calc.allInOneDict(first_number, second_number)
    output = ""
    for op, result in results.items():
        output += f"{op}: {result}<br>"
    return output

@app.route("/mycalc/allInOneList/<int:first_number>/<int:second_number>/")
def all_in_one_list(first_number, second_number):
    results = calc.allInOneList(first_number, second_number)
    labels = ["Addition", "Subtraction", "Multiplication", "Division"]
    output = ""
    for label, result in zip(labels, results):
        output += f"{label}: {result}<br>"
    return output

if __name__ == "__main__":
    app.run(debug=True)