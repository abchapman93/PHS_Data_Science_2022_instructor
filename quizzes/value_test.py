class ValueTest():

    def __init__(self, expected=3, show_answer=False):
        self.expected = expected
        self.show_answer = show_answer

    def test(self, actual):
        if self.expected != actual:
            msg = "That is incorrect."
            if self.show_answer:
                msg += f" Expected {self.expected}, got {actual}"
            print(msg)
        else:
            print("That is correct!")