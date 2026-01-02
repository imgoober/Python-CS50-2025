from um import count

def test_case_sensitivity():
    assert count("um") == 1
    assert count("uM") == 1
    assert count("UM") == 1
    assert count("Um") == 1

def test_punctuation():
    assert count("um, um. um! um; um?") == 5

def test_within_word():
    assert count("yum") == 0


def test_many_spaces():
    assert count("um      um") == 2


