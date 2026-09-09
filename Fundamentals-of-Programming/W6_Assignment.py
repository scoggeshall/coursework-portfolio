"""
MPG Calculator - Calculates average miles per gallon with a looping menu.
Author: Sean Coggeshall
"""

def mpg_calculator():
    while True:
        # Collect user input
        car_name = input("Enter your car name: ").strip()
        trip_name = input("Enter your trip name: ").strip()

        # Get gas price with validation
        while True:
            try:
                gas_price = float(input("Enter the price of gas per gallon: $").strip())
                if gas_price <= 0:
                    raise ValueError("Gas price must be positive.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid positive number.")

        # Get miles driven with validation
        while True:
            try:
                miles_driven = float(input("Enter the amount of miles driven: ").strip())
                if miles_driven < 0:
                    raise ValueError("Miles driven cannot be negative.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid number.")

        # Get gallons used with validation
        while True:
            try:
                gallons_used = float(input("Enter the number of gallons used: ").strip())
                if gallons_used <= 0:
                    raise ValueError("Gallons used must be positive.")
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please enter a valid positive number.")

        # Calculate average miles per gallon
        avg_mpg = miles_driven / gallons_used

        # Display trip summary
        print("\n--- Trip Summary ---")
        print(f"Car Name: {car_name}")
        print(f"Trip Name: {trip_name}")
        print(f"Miles Driven: {miles_driven:.2f} miles")
        print(f"Gallons of Gas Used: {gallons_used:.2f} gallons")
        print(f"Cost per Gallon: ${gas_price:.2f}")
        print(f"Average Miles per Gallon: {avg_mpg:.2f} MPG")

        # Ask if the user wants to calculate another trip
        choice = input("\nWould you like to calculate another trip? (y/n): ").strip().lower()
        if choice != 'y':
            break

    print("\nThank you for using our MPG calculator! Hope you enjoyed your trip!!")
    input("Press Enter to exit...")

# Run the MPG calculator
mpg_calculator()
