from nose.tools import *
from src.factorial import calculate

def test_factorial():
    tests = {
        0: 1,
        1: 1,
        1.5534: 1, # int(1.5534) = 1
        2.677: 2,
        3: 6,
        10: 3628800,
        15: 1307674368000,
    }

    for number in list(tests.keys()):
        assert_equal(calculate(number), tests[number])