from math_series import __version__
from math_series.series import fibonacci, lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'

def test_fibTest():
    actual = fibonacci(9)
    value = 21
    assert actual == value

def test_lucTest():
    actual = lucas(9)
    value = 76
    assert actual == value

def test_sumFibTest():
    actual = sum_series(1)
    value = 0
    assert actual == value

def test_sumLucTest():
    actual = sum_series(6, 2, 1)
    value = 11
    assert actual == value
