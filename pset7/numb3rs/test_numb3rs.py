from numb3rs import validate

def test_greater_255():
    assert validate("255.256.256.256") == False
    assert validate("255.1.1.1") == True

def test_four_sections():
    assert validate("1.1.1.1") == True
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False

def test_all_nums():
    assert validate("one.four.twenty.six") == False
    assert validate("False.True.True.True") == False
    assert validate("1.1.1.1") == True


