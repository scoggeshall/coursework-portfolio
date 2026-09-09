"""
Range Calculator - Performs arithmetic with optional range validation and
dedicated functions for each operation.
Author: Sean Coggeshall
"""

#Range Function
def IsInRange(low_range, high_range, number):
    return low_range <= number <= high_range

#Add Function
def add(first_number, second_number):
    return first_number + second_number

#Subtraction Function
def subtract(first_number, second_number):
    return first_number - second_number

#Multiplication Function
def multiply(first_number, second_number):
    return first_number * second_number

#Division Function
def divide(first_number, second_number):
    return first_number / second_number

#Main loop
while True:
    #Check if a range is needed
    check_range = input("Do you want to check a range for the inputs? (Y/N) ---> ")

    lower_range = None
    higher_range = None

    #If the user selects Y for the range
    if check_range == 'Y':
        lower_range = float(input("Enter your Lower range ---> "))
        higher_range = float(input("Enter your Higher range ---> "))

    while True:
        first_number = float(input("Enter your First number ---> "))
        second_number = float(input("Enter your Second number ---> "))

        if check_range == 'Y':
            if not IsInRange(lower_range, higher_range, first_number) or not IsInRange(lower_range, higher_range, second_number):
                print("The input values are outside the input ranges")
                print("Please check the numbers and try again.")
                continue

        addition = first_number + second_number
        subtractionn = first_number - second_number
        multiplication = first_number * second_number
        division = first_number / second_number

        print("The result of " + str(first_number) + "+" + str(second_number) + "=" + str(addition))
        print("The result of " + str(first_number) + "-" + str(second_number) + "=" + str(subtractionn))
        print("The result of " + str(first_number) + "*" + str(second_number) + "=" + str(multiplication))
        print("The result of " + str(first_number) + "/" + str(second_number) + "=" + str(division))
        print()

        continue_loop = input("Do you want to perform another calculation? (Y/N) ---> ").strip().upper()
        if continue_loop != 'Y':
            break

print("Thanks for using our calculator!")