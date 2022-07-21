class FunctionTest:
    def __init__(self, args, expected):
        self.args = args
        self.expected = expected

    def test(self, func):
        actual = func(*self.args)
        try:
            assert actual == self.expected
            print("Correct!")
        except AssertionError:
            print("Wrong!")
        except IndexError as e:
            print("Error raised during test.")
            raise e
