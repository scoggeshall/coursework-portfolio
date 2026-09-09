"""
Car Trip Report Generator - Manages a list of cars, collects trip data, and
prints a summary report with MPG calculations.
Author: Sean Coggeshall
"""

def display_car_list(car_list):
    """Displays the list of cars."""
    print("\n--- List of Cars ---")
    for car in car_list:
        print(f"- {car}")
    print()

def collect_car_info(car_list):
    """Collects trip data and calculates MPG for each car."""
    car_info = {}
    while True:
        car_name = input("Select a car from the list: ").strip()
        if car_name not in car_list:
            print("Invalid car name. Please select a valid car.")
            continue

        trip_name = input("Enter your trip name: ").strip()

        # Get miles driven with validation
        miles_driven = get_valid_float(f"Miles driven for {trip_name}: ")

        # Get gas price with validation
        gas_price = get_valid_float(f"Cost for {miles_driven} miles: $")

        # Get gallons used with validation
        gallons_used = get_valid_float(f"Gallons of gas used on {trip_name}: ")

        # Calculate average MPG
        avg_mpg = miles_driven / gallons_used

        # Store the trip information
        car_info[car_name] = {
            "Trip Name": trip_name,
            "Miles Driven": miles_driven,
            "Gas Price": gas_price,
            "Gallons Used": gallons_used,
            "Average MPG": avg_mpg
        }

        # Check if the user wants to add more trips
        ans = input("More calculations? (y/n): ").strip().lower()
        if ans != 'y':
            break

    return car_info

def get_valid_float(prompt):
    """Prompts for a valid float input with error handling."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value <= 0:
                raise ValueError("Value must be positive.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid number.")

def print_report(car_list, car_info):
    """Prints the summary report for all cars."""
    print("\n--- Trip Report ---")
    for car in car_list:
        if car in car_info:
            info = car_info[car]
            print(f"Car: {car}")
            print(f"  Trip Name: {info['Trip Name']}")
            print(f"  Miles Driven: {info['Miles Driven']:.2f} miles")
            print(f"  Gallons Used: {info['Gallons Used']:.2f} gallons")
            print(f"  Cost per Mile: ${info['Gas Price']:.2f}")
            print(f"  Average MPG: {info['Average MPG']:.2f} MPG")
            print()
        else:
            print(f"No trip data for {car}.\n")

def main():
    """Main function to drive the program."""
    car_list = []

    # Collect car names
    while True:
        car_name = input("Enter your car name: ").strip()
        car_list.append(car_name)

        ans = input("Add more cars? (y/n): ").strip().lower()
        if ans != 'y':
            display_car_list(car_list)
            break

    # Collect trip information
    car_info = collect_car_info(car_list)

    # Print the report
    print_report(car_list, car_info)

    print("Thank you for using our MPG calculator! Hope you enjoyed your trip!!")
    input("Press Enter to exit...")

# Run the program
if __name__ == "__main__":
    main()
