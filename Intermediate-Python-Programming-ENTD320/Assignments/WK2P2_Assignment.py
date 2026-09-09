# Author: Sean Coggeshall
#
# Calculator class with range-validated input and division-by-zero handling.
# Prompts the user for a numeric range, then performs arithmetic operations
# only on values within that range.

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


# Driver code to test the Use_Calculator class with input range and division by zero checks
def main():
    calc = Use_Calculator()  # Create class instance

    # Loop to get a valid user-defined range
    while True:
        try:
            lower_range = float(input("Enter your Lower range ---> "))
            upper_range = float(input("Enter your Higher range ---> "))

            if lower_range < upper_range:
                break  # Exit loop if valid
            else:
                print("Lower range must be less than Higher range. Please try again.")
        except ValueError:
            print("Please enter numeric values for the range.")

    # Main calculation loop
    while True:
        try:
            first_number = float(input("Enter your First number ---> "))
            second_number = float(input("Enter your Second number ---> "))

            # Check if the inputs are within the user-defined range
            if not (lower_range <= first_number <= upper_range and lower_range <= second_number <= upper_range):
                print("The input values are out side the input ranges")
                print("Please check the numbers and try again")
                print("Thanks for using our calculator!")
                return  # Exit immediately

            # Calculate and display results
            results = calc.allInOneDict(first_number, second_number)
            print(f"The Result of {first_number}+{second_number}={results['add']}")
            print(f"The Result of {first_number}-{second_number}={results['sub']}")
            print(f"The Result of {first_number}*{second_number}={results['mul']}")
            
            # Special handling for division
            if isinstance(results['div'], str):
                print(f"The Result of {first_number}/{second_number}={results['div']}")
            else:
                print(f"The Result of {first_number}/{second_number}={results['div']}")

            # Ask if user wants to perform more calculations
            choice = input("Do you want more calculations (Y/N) ---> ").strip().upper()
            if choice != 'Y':
                break

        except ValueError:
            print("Please enter valid numeric values.")

    print("Thanks for using our calculator!")


if __name__ == "__main__":
    main()
