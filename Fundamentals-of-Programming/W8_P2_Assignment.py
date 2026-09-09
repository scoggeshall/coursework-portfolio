"""
Trip MPG Calculator - Calculates MPG for multiple trips with input validation.
Author: Sean Coggeshall
"""

def get_valid_float(prompt):
    """Prompts the user for a valid positive float."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive number.")

def calculate_trip():
    """Calculates and displays trip details."""
    while True:
        # Collect trip information
        car_name = input("Enter your car name: ").strip()
        trip_name = input("Enter your trip name: ").strip()

        gas_price = get_valid_float("Enter the price of gas per gallon: $")
        miles_driven = get_valid_float("Enter the amount of miles driven: ")
        gallons_used = get_valid_float("Enter the number of gallons used: ")

        # Calculate average miles per gallon
        avg_mpg = miles_driven / gallons_used

        # Display trip summary
        print("\n--- Trip Summary ---")
        print(f"Car Name: {car_name}")
        print(f"Trip Name: {trip_name}")
        print(f"Miles Driven: {miles_driven:.2f} miles")
        print(f"Gallons of Gas Used: {gallons_used:.2f} gallons")
        print(f"Cost per Gallon: ${gas_price:.2f}")
        print(f"Average MPG: {avg_mpg:.2f} MPG")
        print(f"Average miles per gallon for {trip_name} in {car_name}: {avg_mpg:.2f} MPG\n")

        # Ask if the user wants to calculate another trip
        choice = input("Would you like to calculate another trip? (y/n): ").strip().lower()
        if choice != 'y':
            break

    print("Thank you for using our MPG calculator! Hope you enjoyed your trip!!")
    input("Press Enter to exit...")

# Run the program
if __name__ == "__main__":
    calculate_trip()
