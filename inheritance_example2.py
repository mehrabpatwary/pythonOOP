class Shape:
    def __init__(self, dim1, dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print('Í am area method of shape class ')


class Triangle(Shape):
    def area(self):
        print("Area of Triangle: ", 0.5 * self.dim1 * self.dim2)


class Rectangle(Shape):
    def area(self):
        print("Area of Rectangle: ", self.dim1 * self.dim2)


triangle = Triangle(10, 20)
triangle.area()

rectangle = Rectangle(20, 30)
rectangle.area()
