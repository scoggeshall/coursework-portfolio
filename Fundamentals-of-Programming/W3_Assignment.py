"""
Car Trip Tracker - Collects car names and trip data, then generates a report.
Author: Sean Coggeshall
"""

# Initialize lists and dictionaries
car_list = []  # List of car names
car_info = {}  # Dictionary to store car information

# Function to display the list of valid cars
def display_car_list():
    print("\nList of Valid Cars:")
    for car in car_list:
        print(f"- {car}")
    print()

# Collect car names from the user
while True:
    car_name = input("Enter a valid car name: ").strip()
    if car_name:
        car_list.append(car_name)
    else:
        print("Car name cannot be empty. Please try again.")
        continue

    ans = input("Add more cars? (y/n): ").strip().lower()
    if ans != 'y':
        display_car_list()
        break

# Collect trip information for selected cars
while True:
    car_name = input("Select a car from the list: ").strip()
    if car_name not in car_list:
        print("Invalid car name. Please select again.")
        continue

    trip_name = input(f"Enter trip name for {car_name}: ").strip()
    try:
        miles_driven = float(input(f"Enter miles driven for {trip_name}: "))
        trip_cost = float(input(f"Enter the cost for {miles_driven} miles: "))
    except ValueError:
        print("Invalid input! Miles and cost should be numeric.")
        continue

    # Store trip information in the dictionary
    car_info[car_name] = {
        "Trip Name": trip_name,
        "Miles Driven": miles_driven,
        "Trip Cost": trip_cost
    }

    ans = input("Do you want to add more trips? (y/n): ").strip().lower()
    if ans != 'y':
        # Print final report
        print("\n--- Car Trip Report ---")
        for car, info in car_info.items():
            print(f"Car: {car}")
            print(f"  Trip Name: {info['Trip Name']}")
            print(f"  Miles Driven: {info['Miles Driven']} miles")
            print(f"  Trip Cost: ${info['Trip Cost']:.2f}")
        print()
        break
