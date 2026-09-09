# Author: Sean Coggeshall
#
# Calculator class with encapsulated arithmetic operations (add, sub, mul, div)
# that returns results as a dictionary or list, with an interactive CLI driver.

# Define the class with arithmetic operations
class Use_Calculator:
    
    # Private method for addition
    def __add(self, first_number, second_number):
        return first_number + second_number
    
    # Private method for subtraction
    def __sub(self, first_number, second_number):
        return first_number - second_number
    
    # Private method for multiplication
    def __mul(self, first_number, second_number):
        return first_number * second_number
    
    # Private method for division
    def __div(self, first_number, second_number):
        return first_number / second_number

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

# Driver code to test the Use_Calculator class
def main():
    #Driver to get user input and display  results
    calc = Use_Calculator()  # Create class instance
    
    while True:
        try:
            # Get two numbers from user
            first_number = float(input("Enter your First number ---> "))
            second_number = float(input("Enter your Second number ---> "))
            
            # Get results from dictionary method
            results = calc.allInOneDict(first_number, second_number)
            
            # Print results in required format
            print(f"\nThe Result of {first_number}+{second_number}={results['add']}")
            print(f"The Result of {first_number}-{second_number}={results['sub']}")
            print(f"The Result of {first_number}*{second_number}={results['mul']}")
            print(f"The Result of {first_number}/{second_number}={results['div']:.11f}")
            
            # Ask to continue
            if input("\nDo you want more calculations (Y/N) ---> ").strip().lower() != 'y':
                print("Thanks for using our calculator!")
                break
        
        except ValueError:
            print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()

