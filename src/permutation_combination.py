#!/usr/bin/python3
# -*- coding: utf-8 -*-
from src.factorial import calculate as factorial

white_space = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input".format(white_space)


def main():
    print("\n")
    print("  " + decorator)
    print("{} Permutations & Combinations".format(white_space))
    print("  " + decorator)
    prompt()


# Prompt for values for n and r
def prompt():
    try:
        n = int(input('\n{} Value of n: '.format(white_space)))
        r = int(input('{} Value for r: '.format(white_space)))
    except ValueError:
        print(invalid_input)
        prompt()

    result = calculate(n, r)
    print("\n")
    print("{0} Permutations: {1}".format(white_space, result[0]))
    print("{0} Combinations: {1}".format(white_space, result[1]))
    prompt()


# Do the calculations
def calculate(n, r):
    try:
        permutation = factorial(n) / factorial(n - r)
        combination = factorial(n) / (factorial(r) * factorial(n - r))
    # This error is rasied by factioral() for invalid inputs
    except ValueError:
        permutation = 0
        combination = 0

    # Return the number of permutations and combinations in a list
    return [permutation, combination]
