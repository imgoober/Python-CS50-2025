import pytest
from jar import Jar

def test_init():
    jar_A = Jar()
    assert jar_A.capacity == 12
    assert jar_A.size == 0
    jar_B = Jar(5)
    assert jar_B.capacity == 5
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("a")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar(4)
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(1)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(1)
    with pytest.raises(ValueError):
        jar.deposit(-5)

def test_withdraw():
    jar = Jar(6)
    jar.deposit(4)
    jar.withdraw(2)
    assert jar.size == 2
    jar.withdraw(2)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    with pytest.raises(ValueError):
        jar.withdraw(-3)

