from plates import is_valid

def test_is_valid_length():
    assert is_valid("heyheyhey") == False
    assert is_valid("whoa") == True

def test_is_valid_letter_start():
    assert is_valid("10") == False
    assert is_valid("aa") == True

def test_is_valid_symbols():
    assert is_valid("aa$") == False

def test_is_valid_nums():
    assert is_valid("aa0") == False
    assert is_valid("aa1") == True
    assert is_valid("aa10a") == False
    assert is_valid("aa10") == True
