"""
OOP Math Library - Defines math operations using classes with inheritance.
MathBase provides add/subtract, AdvancedMath adds multiply/divide, and
Calculator includes string-based and all-in-one calculation methods.
Author: Sean Coggeshall
"""

# Standalone function to check if a number is within the range
def IsInRange(low_range, high_range, number):
    """Check if a number is within the given range."""
    return low_range <= number <= high_range

# Option 1: Class that contains add and subtract methods
class MathBase:
        
    #Add Function
    def add(self, first_number, second_number):
        return first_number + second_number

    #Subtraction Function
    def subtract(self, first_number, second_number):
        return first_number - second_number

# Option 1: Sub-class using inheritance to add multiply and divide methods
class AdvancedMath(MathBase):
    
    #Multiplication Function
    def multiply(self, first_number, second_number):
        return first_number * second_number

    # Division function with exception handling for division by zero
    def divide(self, first_number, second_number):
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return first_number / second_number
    
# Class that contains prior functions converted to methods of that class
class Calculator(AdvancedMath):
    
    # Scalc 
    def scalc(self, calc_string):

        num1, num2, operator = map(str.strip, calc_string.split(","))
        num1, num2 = float(num1), float(num2)

        if operator == "*":
            return self.multiply(num1, num2)
        elif operator == "+":
            return self.add(num1, num2)
        elif operator == "-":
            return self.subtract(num1, num2)
        elif operator == "/":
            return self.divide(num1, num2)
        else:
            raise ValueError("Invalid operator.")
    
    # All in One
    def allInOne(self, num1, num2):
        return {
            "add": self.add(num1, num2),
            "sub": self.subtract(num1, num2),
            "mult": self.multiply(num1, num2),
            "div": self.divide(num1, num2) if num2 != 0 else None
        }
    