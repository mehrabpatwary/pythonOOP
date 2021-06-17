class Student:
    roll = ''
    gpa = ''

    def set_value(self, roll, gpa):  # Method
        self.roll = roll
        self.gpa = gpa

    def display(self):  # Method
        print(f'Roll: {self.roll}\nGPA: {self.gpa}')


rahim = Student()
rahim.set_value(101, 3.65)
rahim.display()
print("")
karim = Student()
karim.set_value(102, 3.22)
karim.display()
