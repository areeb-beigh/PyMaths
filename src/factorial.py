# Python imports
import math


def get_input():
    """
    Takes user input, validates and prints it's factorial
    """

    try:
        number = int(input("Enter an natural number (q to go back): "))
    except ValueError:
        return
    print("Answer:", math.factorial(number))
    get_input()