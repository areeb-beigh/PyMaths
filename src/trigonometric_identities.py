# Python imports
import math

# Local imports
from src.inputhandler import take_input


def get_input(preset_unit='dummy'):
    """
    Takes user input, validates it and finally prints the result
    returned by the calculate function
    """

    units = ['Degree', 'Radian']

    identities = [
        'Sin(a + b)',
        'Sin(a - b)',
        'Cos(a + b)',
        'Cos(a - b)',
        'Tan(a + b)',
        'Tan(a - b)',
    ]

    if preset_unit.title() not in units:
        unit_choice = take_input(units, len(units))
        unit = units[unit_choice - 1].lower()
    else:
        unit = preset_unit

    identity_choice = take_input(identities, len(identities))
    identity = identities[identity_choice - 1].lower()
    a = int(input("Enter value for a: "))
    b = int(input("Enter value for b: "))
    result = calculate(identity, unit, a, b)
    print("Expression:", result[0])
    print("Answer:", result[1])
    get_input(unit)


def calculate(identity, unit, a, b):
    """
    Takes the parameter identity as a string and angles a and b and
    returns a tuple containing the expression for the identity with
    the given values and the answer of the expression as well
    """

    if unit == "degree":
        a = math.radians(a)
        b = math.radians(b)

    if identity == 'sin(a + b)':
        answer = (math.sin(a) * math.cos(b)) + (math.sin(b) * math.cos(a))
        expression = 'sin({0}) * cos({1}) + sin({1}) * cos({0})'.format(a, b)

    elif identity == 'sin(a - b)':
        answer = (math.sin(a) * math.cos(b)) - (math.sin(b) * math.cos(a))
        expression = 'sin({0}) * cos({1}) - sin({1}) * cos({0})'.format(a, b)

    elif identity == 'cos(a + b)':
        answer = (math.cos(a) * math.cos(b)) - (math.sin(a) * math.sin(b))
        expression = 'cos({0}) * cos({1}) - sin({0}) * sin({1})'.format(a, b)

    elif identity == 'cos(a - b)':
        answer = (math.cos(a) * math.cos(b)) + (math.sin(b) * math.sin(a))
        expression = 'cos({0}) * cos({1}) + sin({0}) * sin({1})'.format(a, b)

    elif identity == 'tan(a + b)':
        answer = (math.tan(a) + math.tan(b)) / 1 - (math.tan(a) * math.tan(b))
        expression = 'tan({0}) + tan({1}) / 1 - (tan({0}) * tan({1}))'.format(a, b)

    elif identity == 'tan(a - b)':
        answer = (math.tan(a) - math.tan(b)) / 1 + (math.tan(a) * math.tan(b))
        expression = 'tan({0}) - tan({1}) / 1 + (tan({0}) * tan({1}))'.format(a, b)

    return expression, answer
