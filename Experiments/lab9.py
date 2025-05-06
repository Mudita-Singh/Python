#`1
class Student:
    name = ""
    sap_id = 0
    marks_math = 0
    marks_chemistry = 0
    marks_physics = 0

stu = [Student(), Student(), Student()]

for x in range(3):
    name = input("Enter name : ")
    sap_id = int(input("Enter sap_id : "))
    marks_math = int(input("Enter marks in math : "))
    marks_physics = int(input("Enter marks in physics : "))
    marks_chemistry = int(input("Enter marks in Chemistry : "))

    stu[x].name = name
    stu[x].sap_id = sap_id
    stu[x].marks_physics = marks_physics
    stu[x].marks_math = marks_math
    stu[x].marks_chemistry = marks_chemistry

for x in range(3):
    print("Name :",stu[x].name)
    print("Sap : ",stu[x].sap_id)
    print("Marks phy : ", stu[x].marks_physics)
    print("Marks math : ",stu[x].marks_math)
    print("Marks chemistry : ",stu[x].marks_chemistry)

#2
class Student:
    def __init__(self, name, sap_id, marks_math, marks_chemistry, marks_physics):
        self.name = name
        self.sap_id = sap_id
        self.marks_math = marks_math
        self.marks_chemistry = marks_chemistry
        self.marks_physics = marks_physics
    def display_details(self):
        print(self.name)
        print(self.sap_id)
        print(self.marks_math)
        print(self.marks_chemistry)
        print(self.marks_physics)

    def marks_percentage(self):
        print(((self.marks_math+self.marks_physics+self.marks_chemistry)/300)*100)
    
    def result(self):
        if (self.marks_math > 40 and self.marks_physics > 40 and self.marks_chemistry > 40 ):
            print("pass")
        else:
            print("Fail")
students = []

for x in range(3):
    name = input("Enter name : ")
    sap_id = int(input("Enter sap_id : "))
    marks_math = int(input("Enter marks in math : "))
    marks_physics = int(input("Enter marks in physics : "))
    marks_chemistry = int(input("Enter marks in Chemistry : "))

    students.append(Student(name, sap_id, marks_math, marks_physics, marks_chemistry))

for stu in students:
    stu.display_details()

#3
#Single Inheritance

class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child(Parent):
    def func2(self):
        print("This function is in child class.")
object = Child()
object.func1()
object.func2()

#Multiple Inheritance
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()
#Multilevel Inheritance
class SuperHead:
    superheadname = ""

class Head(SuperHead):
    headname = ""
class Person(Head):
    name = ""
    def __init__(self, name):
        self.name  = name
    def print_heads(self):
        print(self.headname)
        print(self.superheadname)

p = Person("Mudita")
p.headname = "Anirvan"
p.superheadname = "Dhakshinesh"
p.print_heads()

# Hierarchical inheritance
class Parent:
    def func1(self):
        print("This function is in parent class.")
class Child1(Parent):
    def func2(self):
        print("This function is in child 1.")
class Child2(Parent):
    def func3(self):
        print("This function is in child 2.")
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()

#4
class Parent:
    def func(self):
        print("Parent Class")

class Child(Parent):
    def func(self):
        print("Child class")

obj1 = Parent()
obj2 = Child()

obj1.func()
obj2.func()

#5
class number:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(first, second):
        return (first.x + second.x, first.y + second.y)

p1 = number(1,3)
p2 = number(2,10)
p3 = p1 + p2
print(p3)
	
