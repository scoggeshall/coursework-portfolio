"""
Simple Calculator - Performs basic arithmetic on two user-provided numbers.
Author: Sean Coggeshall
"""

print('This is my first programming assignment')
first_number = input("Enter your Fist number ---> ")
second_number = input("Enter your Second number ---> ")

firstVar = float(first_number)
secondVar = float(second_number)

addition = firstVar + secondVar
subtractionn = firstVar - secondVar
multiplication = firstVar * secondVar
division = firstVar / secondVar

print("The result of " + str(first_number) + "+" + str(second_number) + "=" + str(addition))
print("The result of " + str(first_number) + "-" + str(second_number) + "=" + str(subtractionn))
print("The result of " + str(first_number) + "*" + str(second_number) + "=" + str(multiplication))
print("The result of " + str(first_number) + "/" + str(second_number) + "=" + str(division))
print()
print("Thanks for using our calculator!")