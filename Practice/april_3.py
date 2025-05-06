'''
class Bike:
    name = ""
    gear = 0

bike1 = Bike
bike1.gear = 11
bike1.name = "Mountain bike"
print(f"Name: {bike1.name} , Gears:{bike1.gear}")


class Employee :
    employee_id = 0
employee1 = Employee()
employee2 = Employee()
employee1.employee_id = 1001
print(f"Employee ID : {employee1.employee_id}")
employee2.employee_id = 1002
print(f"Employee ID : { employee2.employee_id}")'''

'''
class Room:
    length = 0.0
    breadth = 0.0
    def calculate_area(self):
        print("Area of Room =" , self.length*self.breadth)
study_room = Room()
study_room.length = 42.5
study_room.breadth = 30.8
study_room.calculate_area()


class ABC():
    var = 10
    def display(self):
        print("in class method..")
obj = ABC()
print(obj.var)
obj.display'''

'''
class Animal:
  def eat(self):
        print("i can eat")
  def sleep(self):
        print("i can sleep")

class Dog(Animal):
    def bark(self):
        print("i can bark woof woof")


dog1 = Dog()
dog1.eat()
dog1.sleep()    
dog1.bark()
'''

#area using inheritance
class Shapes:
    length = breadth = height = 0

class Square(Shapes):
    def calc_area(self):
        print("Area of the square is : ",self.length*self.length)
class Rectangle(Shapes):
    def calc_area(self):
        print("Area of the rectangle is : ",self.length*self.breadth)
class Cube(Shapes):
    def calc_area(self):
        print("Area of the cube is : ",self.length*self.length*self.length)
class Triangle(Shapes):
    def calc_area(self):
        print("Area of the triangle is : ",(self.breadth*self.height)/2)

square1 = Square()
square1.length = 10
square1.calc_area()

rect1 = Rectangle()
rect1.length = 10
rect1.breadth = 20
rect1.calc_area()

cube1 = Cube()
cube1.length = 10
cube1.calc_area()

triangle1 = Triangle()
triangle1.breadth = 10
triangle1.height = 20
triangle1.calc_area()



    







