"""
Trip MPG Calculator - Calculates average miles per gallon for a car trip.
Author: Sean Coggeshall
"""

# Collect user input
car_name = input("Enter your car name: ").strip()
trip_name = input("Enter your trip name: ").strip()

# Ensure the gas price input is valid
while True:
    try:
        gas_price = float(input("Enter the price of gas per gallon: $").strip())
        if gas_price <= 0:
            raise ValueError("Gas price must be positive.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive number.")

# Get miles driven with error handling
while True:
    try:
        miles_driven = float(input("Enter the total miles driven: ").strip())
        if miles_driven < 0:
            raise ValueError("Miles driven cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")

# Get gallons used with error handling
while True:
    try:
        gallons_used = float(input("Enter the number of gallons used: ").strip())
        if gallons_used <= 0:
            raise ValueError("Gallons used must be positive.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive number.")

# Calculate average miles per gallon
average_mpg = miles_driven / gallons_used

# Display results
print("\n--- Trip Summary ---")
print(f"Car Name: {car_name}")
print(f"Trip Name: {trip_name}")
print(f"Miles Driven: {miles_driven:.2f} miles")
print(f"Gallons of Gas Used: {gallons_used:.2f} gallons")
print(f"Cost per Gallon: ${gas_price:.2f}")
print(f"Average Miles per Gallon: {average_mpg:.2f} MPG")
print(f"Average MPG for {trip_name} in {car_name} is: {average_mpg:.2f}")

input("\nPress Enter to exit...")
