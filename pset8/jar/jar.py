class Jar:
    def __init__(self, capacity=12):
        if type(capacity) is not int or capacity < 0:
            raise ValueError("negative 🍪!?")
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        cookies = "🍪" * self._cookies
        return cookies

    def deposit(self, n):
        if n < 0:
            raise ValueError("negative 🍪!?")
        if (self._cookies + n) > self._capacity:
            raise ValueError("too many 🍪!")
        self._cookies += n


    def withdraw(self, n):
        if n < 0:
            raise ValueError("negative 🍪!?")
        if n > self._cookies:
            raise ValueError("not enough 🍪 :(")
        self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies
