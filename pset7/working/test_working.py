from working import convert
import pytest

def test_full_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_hours_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"
    assert convert("12:01 AM to 1:05 PM") == "00:01 to 13:05"
    assert convert("11:59 PM to 12:01 AM") == "23:59 to 00:01"

def test_broken_times():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")




