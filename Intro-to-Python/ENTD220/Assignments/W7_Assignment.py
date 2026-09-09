"""
OOP Calculator - Uses a Calculator class from an imported library with
menu-based operation selection and range validation.
Author: Sean Coggeshall
"""

import W7_Mylib as sfc

def main():
    calculator = sfc.Calculator()

    while True:
        print("\nMenu:")
        print("1) Add two numbers")
        print("2) Subtract two numbers")
        print("3) Multiply two numbers")
        print("4) Divide two numbers")
        print("5) All in one (Add, Subtract, Multiply, Divide)")
        print("6) String-based calculation")
        print("7) Exit")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "7":
            print("Thanks for using the calculator!")
            break

        try:

            check_range = input("Do you want to check a range for the inputs? (Y/N) ---> ").strip().upper()
            lower_range, higher_range = None, None

            if check_range == 'Y':
                while True:
                    # Set the range limits
                    lower_range = float(input("Enter lower limit: "))
                    higher_range = float(input("Enter higher limit: "))
                    if lower_range > higher_range:
                        print("Error: Lower limit cannot be greater than higher limit.")
                    else:
                        break

            if choice == "6":
                calc_string = input("Enter calculation string (e.g., '20,30,*'): ")
                result = calculator.scalc(calc_string)
                print(f"Result: {result}")

            else:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if check_range == 'Y' and (
                    num1 < lower_range or num1 > higher_range or
                    num2 < lower_range or num2 > higher_range
                ):
                    print(f"Error: Numbers are outside the allowed range [{lower_range}, {higher_range}].")
                    continue  # Restart the menu if numbers are invalid

                if choice == "1":
                    print(f"Result: {calculator.add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {calculator.subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {calculator.multiply(num1, num2)}")
                elif choice == "4":
                    try:
                        print(f"Result: {calculator.divide(num1, num2)}")
                    except ZeroDivisionError as e:
                        print(f"Error: {e}")
                elif choice == "5":
                    # All in one calculation
                    results = calculator.allInOne(num1, num2)
                    print(f"{num1} + {num2} = {results['add']}")
                    print(f"{num1} - {num2} = {results['sub']}")
                    print(f"{num1} * {num2} = {results['mult']}")
                    print(f"{num1} / {num2} = {results['div']}")
                else:
                    print("Invalid choice. Try again.")

            continue_loop = input("Do you want to perform another calculation? (Y/N) ---> ").strip().upper()
            if continue_loop != 'Y':
                print("Thanks for using the calculator!")
                break  # Exit the main loop

        except ValueError as ve:
            print(f"Error: Invalid input - {ve}")

if __name__ == "__main__":
    main()


