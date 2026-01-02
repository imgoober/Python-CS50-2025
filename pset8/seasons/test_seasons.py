import pytest
from datetime import date
from seasons import find_date
from seasons import find_num_mins
from seasons import int_to_words
from datetime import timedelta

def test_find_date():
    assert find_date("2000-01-01") == date(2000, 1, 1)
    assert find_date("1999-10-25") == date(1999, 10, 25)
    with pytest.raises(ValueError):
        find_date("blah-blah-blah")
    with pytest.raises(ValueError):
        find_date("2000/01/01")
    with pytest.raises(ValueError):
        find_date("2000-00-01")
    with pytest.raises(ValueError):
        find_date("2000-13-01")
    with pytest.raises(ValueError):
        find_date("2000-01-35")

def test_find_num_mins():
    today = date.today()
    yesterday = today - timedelta(days=1)
    assert find_num_mins(yesterday) == 24*60
    yester_yesterday = today - timedelta(days=2)
    assert find_num_mins(yester_yesterday) == 24*60*2


def test_int_to_words():
    assert int_to_words(1440) == "One thousand, four hundred forty"
    assert int_to_words(1) == "One"
    assert int_to_words(23) == "Twenty-three"
