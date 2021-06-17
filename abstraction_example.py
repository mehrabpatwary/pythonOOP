from abc import ABC, abstractmethod


class Shape(ABC):  # Abstract Class
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod
    def area(self):  # We can call it polymorphism
        pass


class Triangle(Shape):
    def area(self):  # Must Use this Method *** We can call it polymorphism also
        print("Area of Triangle: ", 0.5 * self.dim1 * self.dim2)


class Rectangle(Shape):
    def area(self):  # Must Use this Method *** We can call it polymorphism also
        print("Area of Rectangle: ", self.dim1 * self.dim2)


triangle = Triangle(10, 20)
triangle.area()

rectangle = Rectangle(20, 30)
rectangle.area()
