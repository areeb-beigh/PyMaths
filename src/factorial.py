#!/usr/bin/python3
# -*- coding: utf-8 -*-

white_space = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input".format(white_space)


def main():
    print("\n")
    print("  " + decorator)
    print("{} Factorial".format(white_space))
    print("  " + decorator)
    prompt()


# Prompt the user to enter a whole number
def prompt():
    try:
        number = int(input('\n{} Value: '.format(white_space)))
        print("{0} Answer: {1}".format(white_space, calculate(number)))
        prompt()
    except ValueError:
        print(invalid_input)
        prompt()


def calculate(number):
    if number >= 1:
        number = int(number)
        result = 1
        for i in range(1, number + 1):
            result *= i
        return result
    elif number == 0:
        return 1
    else:
        raise ValueError
