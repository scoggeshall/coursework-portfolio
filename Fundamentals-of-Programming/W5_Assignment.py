"""
Payroll Calculator - Computes employee pay based on hours worked and hourly rate.
Author: Sean Coggeshall
"""

# Collect user input for employee name
employee_name = input("Enter employee's name: ").strip()

# Get hours worked with validation
while True:
    try:
        hours_worked = float(input("Enter the number of hours worked: ").strip())
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid number.")

# Get hourly rate with validation
while True:
    try:
        hourly_rate = float(input("Enter the hourly rate: ").strip())
        if hourly_rate <= 0:
            raise ValueError("Hourly rate must be positive.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive number.")

# Calculate payroll (with a $70 base pay bonus)
base_pay = 70.00
payroll = base_pay + (hours_worked * hourly_rate)

# Display results
print("\n--- Payroll Summary ---")
print(f"Employee Name: {employee_name}")
print(f"Hours Worked: {hours_worked:.2f} hours")
print(f"Hourly Rate: ${hourly_rate:.2f} per hour")
print(f"Base Pay: ${base_pay:.2f}")
print(f"Total Payroll: ${payroll:.2f}")

input("\nPress Enter to exit...")
