from nose.tools import *
from src.trigonometry import calculate
import math


invalidInputs = {
    "iuedh": None,
    "uihfiohyh": None,
    "": None,
    }

'''
To avoid a ton of repetition this function makes the result supplied from calculate()
and the expected result global variables to test equality
'''
def get_result_expected_pair(answersDict, unit, function, angle):
    global result, expected
    result = calculate(unit, function, angle)
    expected = answersDict[angle]

'''
This function takes in the answers dictionary, units of the angle, the function and
iterates over each supplied value to test and uses assert_equal() to check if the result
returned by calculate() is equal to the expected value.

The parameter isInvalid is a boolean that is True if the supplied input is an invalid input
i.e a string of non-numeric characters.
'''
def assert_equality(answersDict, unit, function, isInvalid=False):
    for angle in list(answersDict.keys()):
        get_result_expected_pair(answersDict, unit, function, angle)

        if(not(isInvalid)):
            if(result != "Infinity"):
                assert_equal(round(result,2), expected)
            else:
                assert_equal(result, expected)
        else:
            assert_equal(result, expected)

# Tests the Sin function
def test_sin():
    function = "Sin"

    degreeAngles = {
        90: 1.0,
        60: 0.87,
        45: 0.71,
        30: 0.50,
        0: 0.0,
        99999: -0.99,
    }
    
    radianAngles = {
        math.radians(90): 1.0,
        math.radians(60): 0.87,
        math.radians(45): 0.71,
        math.radians(30): 0.50,
        math.radians(0): 0.0,
        math.radians(99999): -0.99,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)

# Tests the Cos function
def test_cos():
    function = "Cos"

    degreeAngles = {
        90: 0.0,
        60: 0.5,
        45: 0.71,
        30: 0.87,
        0: 1.0,
        99999: 0.16,
    }
    
    radianAngles = {
        math.radians(90): 0.0,
        math.radians(60): 0.5,
        math.radians(45): 0.71,
        math.radians(30): 0.87,
        math.radians(0): 1.0,
        math.radians(99999): 0.16,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)

# Tests the Tan function
def test_tan():
    function = "Tan"

    degreeAngles = {
        90: 1.633123935319537e+16,
        60: 1.73,
        45: 1.00,
        30: 0.58,
        0: 0.00,
        99999: -6.31,
    }
    
    radianAngles = {
        math.radians(90): 1.633123935319537e+16,
        math.radians(60): 1.73,
        math.radians(45): 1.00,
        math.radians(30): 0.58,
        math.radians(0): 0.00,
        math.radians(99999): -6.31,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)

# Tests the Cosec function
def test_cosec():
    function = "Cosec"

    degreeAngles = {
        90: 1.0,
        60: 1.15,
        45: 1.41,
        30: 2.00,
        0: "Infinity",
        99999: -1.01,
    }
    
    radianAngles = {
        math.radians(90): 1.0,
        math.radians(60): 1.15,
        math.radians(45): 1.41,
        math.radians(30): 2.00,
        math.radians(0): "Infinity",
        math.radians(99999): -1.01,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)

# Tests the Sec function
def test_sec():
    function = "Sec"

    degreeAngles = {
        90: 1.633123935319537e+16,
        60: 2.00,
        45: 1.41,
        30: 1.15,
        0: 1.00,
        99999: 6.39,
    }
    
    radianAngles = {
        math.radians(90): 1.633123935319537e+16,
        math.radians(60): 2.00,
        math.radians(45): 1.41,
        math.radians(30): 1.15,
        math.radians(0): 1.0,
        math.radians(99999): 6.39,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)

# Tests the Cot function
def test_cot():
    function = "Cot"

    degreeAngles = {
        90: 0.00,
        60: 0.58,
        45: 1.00,
        30: 1.73,
        0: "Infinity",
        99999: -0.16,
    }
    
    radianAngles = {
        math.radians(90): 0.00,
        math.radians(60): 0.58,
        math.radians(45): 1.00,
        math.radians(30): 1.73,
        math.radians(0): "Infinity",
        math.radians(99999): -0.16,
    }

    assert_equality(degreeAngles, "Degree", function)
    assert_equality(radianAngles, "Radian", function)
    assert_equality(invalidInputs, "Degree", function, True)
    assert_equality(invalidInputs, "Radian", function, True)