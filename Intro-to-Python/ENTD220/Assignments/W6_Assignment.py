"""
Menu-Driven Calculator - Features a menu system for selecting operations
including string-based calculations and an all-in-one mode.
Author: Sean Coggeshall
"""

import W6_Mylib as sfc

def main():
    menu = [
        "Add two numbers",
        "Multiply two numbers",
        "Divide two numbers",
        "Scalc (string calculation)",
        "All in one (Add, Subtract, Multiply, Divide)",
        "Exit"
    ]

    while True:
        # Display menu
        print("\nMenu:")
        for i, item in enumerate(menu):
            print(f"{i + 1}) {item}")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "6":
            print("Thanks for using our calculator!")
            break

        try:
            # Ask if the user wants to use range checking
            check_range = input("Do you want to check a range for the inputs? (Y/N) ---> ").strip().upper()
            lower_range, higher_range = None, None

            if check_range == 'Y':
                while True:
                    lower_range = float(input("Enter lower limit: "))
                    higher_range = float(input("Enter higher limit: "))
                    if lower_range > higher_range:
                        print("Error: Lower limit cannot be greater than higher limit.")
                    else:
                        break

            if choice == "4":
                # String calculation mode
                calc_string = input("Enter calculation string (e.g., '20,30,*'): ")
                result = sfc.scalc(calc_string)
                print(f"Result: {result}")
                continue

            # For other operations, we need two numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Check range if needed
            if check_range == 'Y' and not (sfc.IsInRange(lower_range, higher_range, num1) and sfc.IsInRange(lower_range, higher_range, num2)):
                print(f"Error: Numbers are outside the allowed range [{lower_range}, {higher_range}].")
                continue

            # Perform the selected operation
            if choice == "1":
                result = sfc.add(num1, num2)
                print(f"{num1} + {num2} = {result}")

            elif choice == "2":
                result = sfc.multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")

            elif choice == "3":
                result = sfc.divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            elif choice == "5":
                results = sfc.allInOne(num1, num2)
                print(f"{num1} + {num2} = {results['add']}")
                print(f"{num1} - {num2} = {results['sub']}")
                print(f"{num1} * {num2} = {results['mult']}")
                print(f"{num1} / {num2} = {results['div']}")

        except ValueError as ve:
            print(f"Error: Invalid input - {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
