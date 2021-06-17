# Multiple_Inheritance

class A:
    def display(self):
        print('I am in A class')


class B:
    def display(self):
        print('I am in B class')


class C(B, A):  # Multiple_Inheritance
    # def display(self):
    # print('I am in C class')
    pass


ob1 = C()
ob1.display()
