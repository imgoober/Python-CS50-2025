from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten('hello') == "hll"
    assert shorten('HELLO') == "HLL"
    assert shorten('400ap') == "400p"
    assert shorten('.') == "."



if __name__ == "__main__":
    main()
