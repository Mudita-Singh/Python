class calculation1:
    def summation(self , a , b ):
       return a+b
class calculation2 :
    def multiplication(self , a , b):
        return a*b
class Derived(calculation1 ,  calculation2):
    def divide(self , a ,b):
        return a/b
d = Derived()
print(issubclass(Derived , calculation2))
print(issubclass(calculation1 , calculation2))

    
class Animal:
    def speak(self):
        print("speaking")
class Dog(Animal):
    def speak(self):
        print("barking")
        d = Dog()
    d.speak()

class Bank:
    def getroi(self):
        return 10 
class SBI (Bank):
    def getroi(self):
        return 7
class ICIC (Bank):
    def getroi(self):
        return 8
b1 = Bank()
b2 = SBI()
b3 = ICIC()
print("bank rate of interest" , b1.getroi())
print(" SBI rate of interest" , b2.getroi())
print("ICIC rate of interest" , b3.getroi())

