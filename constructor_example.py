class Student:
    roll = ''
    gpa = ''

    def __init__(self, roll, gpa):  # Constructor (Can work without calling)
        self.roll = roll
        self.gpa = gpa

    def display(self):  # Method
        print(f'Roll: {self.roll}\nGPA: {self.gpa}')


rahim = Student(101, 3.56)
rahim.display()
print("")
karim = Student(102, 3.75)
karim.display()
