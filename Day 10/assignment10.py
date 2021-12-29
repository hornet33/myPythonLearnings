# Python program to implement a calculator
from calculator_art import logo
from helpers.utilities import screen_clear


# Addition
def add(n1, n2):
    """Function to add two numbers and return the output"""  # Doc String
    return n1 + n2


# Subtraction
def subtract(n1, n2):
    """Function to subtract n2 from n1 and return the output"""
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    """Function to multiply two numbers and return the output"""
    return n1 * n2


# Division
def divide(n1, n2):
    """Function to divide n1 by n2 and return the output"""
    return n1 / n2


# Storing the calculator operations as a dictionary
calc_ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    screen_clear()
    print(logo)
    continue_calculation = True
    num1 = float(input("Enter the first number: "))

    while continue_calculation:
        print("Following are the choice of operations: ")
        for operation in calc_ops:
            print(operation)
        choice = input("Enter the operation to perform: ")
        num2 = float(input("Enter the next number: "))

        # Call the function to perform
        func = calc_ops[choice]  # From the calculator operations dictionary, get the function name to call
        result = func(num1, num2)  # Python replaces 'func' with name of the function and calls that function
        # Example, func = add so for Python it is "add()"

        print(f"{num1} {choice} {num2} = {result}")
        user_choice = input(
            f"Type 'y' to continue calculation with {result}, type 'n' to start a new calculation: ").lower()
        if user_choice == 'y':
            num1 = result  # Reassign num1 to last result to continue calculation with it
        else:
            continue_calculation = False
            calculator()  # Recursive call to calculator() for a new calculation


# Calling calculator()
calculator()
