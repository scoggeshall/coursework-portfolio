"""
Calculator with Exception Handling - Adds try/except error handling and
range validation to the calculator program.
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

# Division function with exception handling for division by zero
def divide(first_number, second_number):
    if second_number == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return first_number / second_number

# Main loop
while True:
    try:
        #Check if a range is needed
        check_range = input("Do you want to check a range for the inputs? (Y/N) ---> ").strip().upper()

        lower_range = None
        higher_range = None

        #If the user selects Y for the range
        if check_range == 'Y':
            while True:
                lower_range = float(input("Enter your Lower range ---> "))
                higher_range = float(input("Enter your Higher range ---> "))
                
                # Range Validation
                if lower_range > higher_range:
                    print("Error --> The lower range cannot be higher than the higher range. Please try again.")
                    continue
                break 

        while True:
            try:
                first_number = float(input("Enter your First number ---> "))
                second_number = float(input("Enter your Second number ---> "))

                if check_range == 'Y':
                    if not IsInRange(lower_range, higher_range, first_number) or not IsInRange(lower_range, higher_range, second_number):
                        print("Error --> The input values are outside the allowed range.")
                        continue

                print("The result of " + str(first_number) + " + " + str(second_number) + " = " + str(add(first_number, second_number)))
                print("The result of " + str(first_number) + " - " + str(second_number) + " = " + str(subtract(first_number, second_number)))
                print("The result of " + str(first_number) + " * " + str(second_number) + " = " + str(multiply(first_number, second_number)))
                print("The result of " + str(first_number) + " / " + str(second_number) + " = " + str(divide(first_number, second_number)))
                print()

                continue_loop = input("Do you want to perform another calculation? (Y/N) ---> ").strip().upper()
                if continue_loop != 'Y':
                    break

            except ValueError as ve:
                print(f"Error --> Invalid input: {ve}")
                continue

            except ZeroDivisionError as zde:
                print(f"Error --> {zde}")
                continue
        break

    except Exception as e:
        print(f"Error --> {e}")
        continue

print("Thanks for using our calculator!")