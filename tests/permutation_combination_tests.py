from nose.tools import *
from src.permutation_combination import calculate


def test_permutation_combination():
    tests = {
        (0, 0): [1, 1],
        (5, 3): [60, 10],
        (-10, 23): [0, 0],
        (817, 92): [4.085163958479375e+265, 3.284312566323538e+123]
    }

    for input in list(tests.keys()):
        assert_equal(calculate(input[0], input[1]), tests[input])
