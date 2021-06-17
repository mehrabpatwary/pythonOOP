class Phone:  # Parent class, Super class, Base class
    def call(self):
        print("You can call")

    def message(self):
        print("You can message")


class Samsung(Phone):  # Inherit (Child class, Sub class, Derived class)
    def photo(self):
        print("You can take photo")


p = Samsung()
p.call()
p.message()
p.photo()

print(issubclass(Samsung, Phone))


