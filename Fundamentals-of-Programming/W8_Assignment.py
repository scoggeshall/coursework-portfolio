"""
Payroll Calculator - Computes payroll for multiple employees in a loop.
Author: Sean Coggeshall
"""

def get_valid_float(prompt):
    """Prompts the user for a valid positive float."""
    while True:
        try:
            value = float(input(prompt).strip())
            if value < 0:
                raise ValueError("Value cannot be negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid positive number.")

def calculate_payroll():
    """Calculates payroll for multiple employees."""
    while True:
        # Collect employee information
        employee_name = input("Enter the employee's name: ").strip()

        # Collect hours worked and hourly rate with validation
        hours_worked = get_valid_float("Enter hours worked: ")
        hourly_rate = get_valid_float("Enter hourly rate: ")

        # Calculate payroll
        payroll = hours_worked * hourly_rate

        # Display payroll summary
        print("\n--- Payroll Summary ---")
        print(f"Employee Name: {employee_name}")
        print(f"Hours Worked: {hours_worked:.2f} hours")
        print(f"Hourly Rate: ${hourly_rate:.2f} per hour")
        print(f"Total Payroll: ${payroll:.2f}")
        print(f"Calculation: {hours_worked:.2f} * {hourly_rate:.2f} = ${payroll:.2f}\n")

        # Ask if the user wants to calculate another payroll
        choice = input("Would you like to calculate another payroll? (y/n): ").strip().lower()
        if choice != 'y':
            break

    print("Thank you for using our payroll calculator!")
    input("Press Enter to exit...")

# Run the payroll calculator
if __name__ == "__main__":
    calculate_payroll()
