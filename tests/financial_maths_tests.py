from nose.tools import *
from src.financial_maths import compound_interest
from src.financial_maths import simple_interest


def test_compound_interest():
    assert_equal(compound_interest(100, 23, 553, 2), 158.39)
    assert_equal(compound_interest(18947, 239, 328, 3), 23996167.4)
    assert_equal(compound_interest(342, 43, 32, 2), 803.59)
    assert_equal(compound_interest(0, 0, 0, 0), None)


def test_simple_interest():
    assert_equal(simple_interest(1, 20, 30), 6.0)
    assert_equal(simple_interest(500, 10, 20), 1000.0)
    assert_equal(simple_interest(0, 0, 0), 0.0)
