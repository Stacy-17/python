# oop stands for object oriented programming
# a class is a blueprint of an object
# an object is an instance of a class
class Student:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# member function

    def display(self):
        print(f"Student Name is : {self.name}, Age is : {self.age}, Score is : {self.score}")

# instance of the class

my_object = Student("Melanie", 15, 'A' )
my_object.display()
my_object1 = Student("Amy", 17, 'B+')
my_object1.display()
my_object2 = Student("John", 20, 'C-')
my_object2.display()
my_object3 = Student("Nicolas", 18, 'A-')
my_object3.display()
my_object4 = Student("Blessing", 19, 'B-')
my_object4.display()
