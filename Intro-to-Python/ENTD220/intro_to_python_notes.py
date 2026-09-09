"""
Introduction to Python Programming - Covers fundamental Python concepts including
comments, variables, functions, control structures, loops, error handling, and OOP.
Author: Sean Coggeshall
"""

# Section: User Greeting
myname = input("Enter your name: ")
print("Hello, my name is", myname)

"""
Section: Comments
1) Block Comments: Enclosed in triple quotes.
2) Line Comments: Start with the '#' symbol.
"""

# Section: Variables and Printing
fnum = float(input("Enter first number -> "))
snum = float(input("Enter second number -> "))
sum_result = fnum + snum
print(f"{fnum} + {snum} = {sum_result}")

# Section: Functions and Error Handling
def add_numbers(num1, num2):
    if num1 < 0 or num2 < 0:
        raise ValueError("Negative numbers are not allowed")
    return num1 + num2

try:
    result = add_numbers(5, -3)
    total = result + 10
except ValueError as e:
    print(f"Error: {e}")

def div(n1, n2):
    return n1 / n2

while True:
    try:
        fnum = float(input("Enter first number -> "))
        snum = float(input("Enter second number -> "))
        print(f"The division result = {div(fnum, snum)}")
        break
    except Exception as e:
        print(f"Error: {e}")
        continue

# Section: Dictionaries
def myfruits():
    return {"A": "Apple", "B": "Banana", "C": "Coconut"}

print(f"My favorite fruit: {myfruits()['A']}")

# Section: Classes and Objects
class DCalc:
    def add(self, fn, sn):
        return fn + sn

    def multiply(self, fn, sn):
        return fn * sn

calc = DCalc()
print(f"2 + 3 = {calc.add(2, 3)}")
print(f"2 * 3 = {calc.multiply(2, 3)}")

# Section: Static vs Dynamic Classes
class StaticCalc:
    def add(fn, sn):
        return fn + sn

print(StaticCalc.add(5, 7))

class DynamicCalc:
    def add(self, fn, sn):
        return fn + sn

obj1 = DynamicCalc()
print(obj1.add(4, 5))

# Section: Library Usage Example
def pay(hours, rate):
    return hours * rate

def overtime_pay(base_pay, ot_rate):
    return base_pay * ot_rate

base = pay(4, 20)
total_pay = overtime_pay(base, 1.5)
print(f"The base pay = {base}")
print(f"The total pay = {total_pay}")

# Section: Trapping Errors
def checknum(lb, num, ub):
    return lb < num < ub

while True:
    try:
        fnum = float(input("Enter first number -> "))
        snum = float(input("Enter second number -> "))
        if checknum(0, fnum, 100) and checknum(0, snum, 100):
            print(f"{fnum} + {snum} = {fnum + snum}")
            break
        else:
            print("Number out of range, try again.")
    except Exception as e:
        print(f"Error: {e}")
        continue

# Section: File Handling with Read/Write Methods
class Calc:
    def sadd(self, fn, sn):
        return fn + sn

    def wres(self, file, message):
        with open(file, "a") as f:
            f.write(message)

    def rres(self, file):
        with open(file, "r") as f:
            return f.read()

calc = Calc()
while True:
    a = float(input("Enter first number -> "))
    b = float(input("Enter second number -> "))
    result = f"{a} + {b} = {calc.sadd(a, b)}\n"
    save = input("Save result? (y/n) ")
    if save.lower() == 'y':
        calc.wres("results.txt", result)
    cont = input("Continue? (y/n) ")
    if cont.lower() != 'y':
        break

print("Results:\n", calc.rres("results.txt"))
