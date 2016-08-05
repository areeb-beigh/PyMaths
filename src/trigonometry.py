#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

white_space = "   "
decorator = "-" * 35
invalid_input = "\n{} [-] Invalid input".format(white_space)

# Available units
units = ['Radian', 'Degree']

# Available trig functions
functions = ['Sin', 'Cos', 'Tan', 'Cosec', 'Sec', 'Cot']


def main():
    print("\n")
    print("  " + decorator)
    print(white_space + " Trigonometry")
    print("  " + decorator)
    prompt_unit()


# Prompt for the unit
def prompt_unit():
    global unit
    print("\n")

    for serial, unit in enumerate(units, start=1):
        print("{0} {1}. {2}".format(white_space, serial, unit))

    print("  " + decorator)

    try:
        choice = int(input('\n{} Enter your choice: '.format(white_space)))
    except ValueError:
        print(invalid_input)
        prompt_unit()

    if choice in range(1, len(units) + 1):
        unit = units[choice - 1]
        prompt_function()
    else:
        print(invalid_input)
        prompt_unit()


# Prompt for the trig funcntion
def prompt_function():
    global function
    print("\n")

    for serial, function in enumerate(functions, start=1):
        print("{0} {1}. {2}".format(white_space, serial, function))

    print("  " + decorator)

    try:
        choice = int(input('\n{} Enter your choice: '.format(white_space)))
    except(ValueError):
        print(invalid_input)
        prompt_function()
    except KeyboardInterrupt:
        print("\n\n{} [-] Going back to unit choice...".format(white_space))
        prompt_unit()

    if choice in range(1, len(functions) + 1):
        function = functions[choice - 1]
        prompt_value()
    else:
        print(invalid_input)
        prompt_function()


# Prompt value for the angle
def prompt_value():
    # Makes sure that the input is numeric, prints error if not
    try:
        value = float(input('\n{} Angle: '.format(white_space)))
    except KeyboardInterrupt:
        print("\n\n{} [-] Going back to function choice...".format(white_space))
        prompt_function()
    except ValueError:
        print(invalid_input)
        prompt_value()

    answer = calculate(unit, function, value)

    if answer != None:
        print("{0} Answer: {1}".format(white_space, answer))
    else:
        print("[-] Unexpected error occured")

    prompt_value()


# Do the magic
def calculate(unit, function, value):
    def sin(value):
        return math.sin(value)

    def cos(value):
        return math.cos(value)

    def tan(value):
        return math.tan(value)

    def cosec(value):
        try:
            return 1 / sin(value)
        except(ZeroDivisionError):
            return "Infinity"

    def sec(value):
        return 1 / cos(value)

    def cot(value):
        try:
            return 1 / tan(value)
        except(ZeroDivisionError):
            return "Infinity"

    # For the unit testing to work we return null for non-numeric input
    try:
        value = float(value)
    except ValueError:
        return None;

    if function == 'Sin':

        # If chosen unit was Radian
        if unit == 'Radian':
            return sin(value)

        # If chosen unit was Degree
        elif unit == 'Degree':
            return sin(math.radians(value))

    elif function == 'Cos':

        if unit == 'Radian':
            return cos(value)

        elif unit == 'Degree':
            return cos(math.radians(value))

    elif function == 'Tan':

        if unit == 'Radian':
            return tan(value)

        elif unit == 'Degree':
            return tan(math.radians(value))

    elif function == 'Cosec':

        if unit == 'Radian':
            return cosec(value)

        elif unit == 'Degree':
            return cosec(math.radians(value))

    elif function == 'Sec':

        if unit == 'Radian':
            return sec(value)

        elif unit == 'Degree':
            return sec(math.radians(value))

    elif function == 'Cot':

        if unit == 'Radian':
            return cot(value)

        elif unit == 'Degree':
            return cot(math.radians(value))

    else:
        return None
