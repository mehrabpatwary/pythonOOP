class Phone:
    def __init__(self):  # Can work without calling
        print("I am in phone class")

    def display(self):
        print("I can Display")


class Samsung(Phone):
    def __init__(self):  # Method Overriding
        super().__init__()  # Can call super class
        super().display()  # Can use super class Method by this super() key
        print("I am in Samsung class")


s = Samsung()
# p = Phone()
