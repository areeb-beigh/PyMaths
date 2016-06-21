from nose.tools import *
from src.trigonometric_identities import calculate
import math

def assert_equality(answersDict, identity):
    for angleList in list(answersDict.keys()):
        result = calculate(identity, angleList[0], angleList[1])[0]
        expected = answersDict[angleList]
        assert_equal(round(result,2), expected)

def test_sin_addition():
    tests = {
        (math.radians(45), math.radians(45)): 1.00,
        (522, 98): -0.89,
        (56,56): -0.89,
    }

    assert_equality(tests, "sin(a + b)")

def test_sin_subtraction():
    tests = {
        (math.radians(45), math.radians(45)):0.00,
        (522, 98): 0.11,
        (56,56): 0.00,
    }

    assert_equality(tests, "sin(a - b)")


def test_cos_addition():
    tests = {
        (math.radians(45), math.radians(45)): 0.00,
        (522, 98): -0.45,
        (56,56): 0.46,
    }

    assert_equality(tests, "cos(a + b)")


def test_cos_subtraction():
    tests = {
        (math.radians(45), math.radians(45)): 1.00,
        (522, 98): -0.99,
        (56,56): 1.00,
    }

    assert_equality(tests, "cos(a - b)")


def test_tan_addition():
    tests = {
        (math.radians(45), math.radians(45)): 1.00,
        (522, 98): 0.86,
        (56,56): -1.60,
    }

    assert_equality(tests, "tan(a + b)")


def test_tan_subtraction():
    tests = {
        (math.radians(45), math.radians(45)): 1.00,
        (522, 98): 0.22,
        (56,56): 0.37,
    }

    assert_equality(tests, "tan(a - b)")