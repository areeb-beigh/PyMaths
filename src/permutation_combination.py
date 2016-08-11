# Python imports
import math


def get_input():
    """
    Takes user input, validates it and finally prints the result
    returned by the calculate function
    """

    n = int(input("Enter value for n: "))
    r = int(input("Enter value for r: "))

    while r > n:
        print("Value of r can't be greater than n")
        n = int(input("Enter value for n: "))
        r = int(input("Enter value for r: "))

    result = calculate(n, r)
    print("     Permutations:", result[0])
    print("     Combinations:", result[1])


def calculate(n, r):
    """
    Takes values for n and r and returns the number of permutations
    and combinations in a tuple - (permutations, combinations)
    """

    permutations = math.factorial(n) / math.factorial(n - r)
    combinations = math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

    return permutations, combinations
