"""
Python Reflection - Demonstrates key Python concepts including variables,
loops, functions, classes, and file I/O.
Author: Sean Coggeshall
"""

# Open a text file to log the output
with open("reflection_output.txt", "w") as log_file:

    def log_and_print(message):
        """Helper function to print and log output."""
        print(message)
        log_file.write(message + "\n")

    # Reflection: What did you learn from the experience?
    log_and_print("Reflection 1: What did you learn from the experience?")
    log_and_print("I learned Python's key concepts, including functions, loops, OOP, and file handling.\n")

    # Reflection: How did the assignment relate to your personal or professional goals?
    log_and_print("Reflection 2: How did the assignment relate to your personal or professional goals?")
    log_and_print("They aligned with my goal of becoming an IT Systems Engineer by enhancing my problem-solving and coding skills.\n")

    # Reflection: Did the assignments challenge you?
    log_and_print("Reflection 3: Did the assignments challenge you?")
    log_and_print("Yes, especially in debugging the assignments and managing exceptions.\n")

    # 1. What is Python, and what are its key features?
    log_and_print("1. What is Python, and what are its key features?")
    log_and_print("Python is an interpreted, high-level programming language with dynamic typing and extensive libraries.\n")

    # 2. What is the difference between a local variable and a global variable in Python?
    log_and_print("2. What is the difference between a local variable and a global variable in Python?")
    log_and_print("A local variable is declared inside a function and accessible only within that function, "
                  "while a global variable is accessible throughout the entire program.\n")

    # 3. Demonstrating declaring three variables in Python using your name
    log_and_print("3. Demonstrating declaring three variables in Python using your name:")
    first_name = "Sean"
    middle_name = "F."
    last_name = "Coggeshall"
    log_and_print(f"First Name: {first_name}, Middle Name: {middle_name}, Last Name: {last_name}\n")

    # 4. Define at least three different data types available in Python
    log_and_print("4. Define at least three different data types available in Python:")
    log_and_print("- String: 'Hello World'\n- Integer: 42\n- List: [1, 2, 3]\n")

    # 5. Write a conditional statement (if-else) in Python using something that relates to you
    log_and_print("5. Write a conditional statement (if-else) in Python using something that relates to you:")
    if first_name == "Sean":
        log_and_print("Hello Sean, welcome back!")
    else:
        log_and_print("Hello, Guest!\n")

    # 6. Provide an example of lists, tuples, and dictionaries. How are they different from each other?
    log_and_print("6. Provide an example of lists, tuples, and dictionaries in Python:")
    my_list = [1, 2, 3]
    my_tuple = (4, 5, 6)
    my_dict = {"A": "Apple", "B": "Banana"}
    log_and_print(f"List: {my_list}\nTuple: {my_tuple}\nDictionary: {my_dict}\n")

    # 7. Explain the concept of function in Python and provide an example
    log_and_print("7. Explain the concept of function in Python with an example:")
    def greet(name):
        return f"Hello, {name}!"

    log_and_print(greet(first_name) + "\n")

    # 8. How do you handle exceptions (errors) in Python?
    log_and_print("8. How do you handle exceptions (errors) in Python?")
    try:
        result = 10 / 0  # Intentional ZeroDivisionError
    except ZeroDivisionError as e:
        log_and_print(f"Error handled: {e}\n")

    # 9. What is a loop in Python? Provide an example of the difference between a for loop and a while loop
    log_and_print("9. What is a loop in Python? Provide examples of a for loop and a while loop:")
    log_and_print("For Loop Example:")
    for i in range(3):
        log_and_print(f"Iteration {i}: Hello {first_name}")

    log_and_print("While Loop Example:")
    counter = 0
    while counter < 3:
        log_and_print(f"While Loop {counter}: Hi {first_name}")
        counter += 1
    log_and_print("")

    # 10. What is the purpose of the "range()" function in Python?
    log_and_print("10. What is the purpose of the 'range()' function in Python?")
    log_and_print("The 'range()' function generates a sequence of numbers, often used to control loop iterations.\n")

    # 11. How do you read data from a file in Python?
    log_and_print("11. How do you read data from a file in Python?")
    log_and_print("In Python, you use the built-in `open()` function to open files. "
                  "Using a 'with' block ensures the file is properly closed after use. "
                  "You can read the entire content with `file.read()` or read line by line using a loop. "
                  "It’s important to handle exceptions like FileNotFoundError for missing files.")
    try:
        with open("sample.txt", "r") as file:
            content = file.read()
            log_and_print("File Content:\n" + content)
    except FileNotFoundError:
        log_and_print("The file 'sample.txt' was not found.\n")

    # 12. How do you comment your code in Python? Why is it important to write comments?
    log_and_print("12. How do you comment your code in Python? Why is it important to write comments?")
    log_and_print("# This is a single-line comment\n'''This is a multi-line comment'''")
    log_and_print("Comments improve code readability and help others understand your code.\n")

    # 13. Describe the concept of OOP in Python. What are classes and objects?
    log_and_print("13. Describe the concept of OOP in Python. What are classes and objects?")
    log_and_print("Object-Oriented Programming (OOP) in Python organizes code into reusable, modular 'classes' "
                  "as blueprints for attributes and methods. 'Objects' are instances of classes, holding actual data "
                  "and using class methods. OOP promotes code reuse and real-world modeling.")


