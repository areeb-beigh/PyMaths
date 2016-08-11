# Python imports
import math

# Local imports
from src.inputhandler import take_input


def get_input(preset_unit="dummy"):
    """
    Takes user input, validates it and finally prints the result
    returned by the calculate function

    Parameters:
        preset_unit:
            If this is given and it is in the list of valid units
            then the units selection will be skipped (used in recursion)
    """

    units = ['Degree', 'Radian']

    functions = [
        'Sine',
        'Cosine',
        'Tangent',
        'Arc Sine',
        'Arc Cosine',
        'Arc Tangent',
        'Hyperbolic Sine',
        'Hyperbolic Cosine',
        'Hyperbolic Tangent',
        'Go Back',
    ]

    function_values = [
        'sin',
        'cos',
        'tan',
        'asin',
        'acos',
        'atan',
        'sinh',
        'cosh',
        'tanh',
    ]

    if preset_unit.title() not in units:
        unit_choice = take_input(units, max_value=len(units))
        unit = units[unit_choice - 1].lower()
    else:
        unit = preset_unit

    print("     Unit:", unit)
    function_choice = take_input(functions, max_value=len(functions))
    # Index error would occur if the user selected the Go Back option
    # In that case he is taken back to the main menu
    try:
        function = function_values[function_choice - 1]
    except IndexError:
        return
    angle = int(input("Enter angle in {}s: ".format(unit)))
    result = calculate(function, angle, unit)
    print("     Answer:", result)
    # Go back with the selected unit
    get_input(unit)


def calculate(function, angle, units):
    """
    Returns the calculated result of the given angle
    """

    if units == "degree":
        angle = math.radians(angle)

    method_call = "math.{0}({1})".format(function, angle)
    return eval(method_call)
