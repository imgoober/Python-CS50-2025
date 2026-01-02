from fuel import convert
from fuel import gauge

def test_convert_errors():
    try:
        convert("cat/dog")
        assert False
    except ValueError:
        assert True

    try:
        convert("-1/2")
        assert False
    except ValueError:
        assert True

def test_convert_zero_division():
    try:
        convert("1/0")
        assert False
    except ZeroDivisionError:
        assert True

def test_convert_values():
    assert convert("1/100") == 1
    assert convert("3/4") == 75


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
