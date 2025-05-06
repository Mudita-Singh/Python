#sum of three numbers
a,b,c=4,5,2
print(a+b+c)

#input from user
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
print(a+b+c)

#add two strings
a="hello"
b="world!"
print(a+b)

#area of rectangle
l=int(input("length: "))
b=int(input("breadth: "))
print("area=",l*b)

#area of circle
r=int(input("radius: "))
pi=3.14
print("area= ",pi*r*r)

#cube root of a number
n=int(input("number: "))
print("cube root of",n,"is",n**(1/3))

#cube root using math
import math
n=int(input("enter a number: "))
a=math.pow(n,(1/3))
print("cube root:",a)

#avg of three numbers
a=int(input("a= "))
b=int(input("b= "))
c=int(input("c= "))
print((a+b+c)/3)

#swap without temp
a=int(input("a= "))
b=int(input("b= "))
a=a+b
b=a-b
a=a-b
print(a,b)

#even odd number
a=int(input("a: "))
if(a%2==0):
    print(a,"is an even number")
else:
    print(a,"is an odd  number")

#marks
print("marks:")
a=float(input("maths:"))
b=float(input("english:"))
c=float(input("evs:"))
d=float(input("hindi:"))
e=float(input("science:"))
z=(a+b+c+d+e)/5
print("average: ",z)
if(z>=91):
    print("O")
elif (z>=81):
    print("A+")
elif (z >= 71):
    print("A")
elif (z >= 61):
    print("B+")
elif (z >= 51):
    print("B")
elif(z>=41):
    print("C+")
elif(z>=35 and z<=40):
    print("C")
else:
    print("Fail")


n = int(input("enter the no."))
for x in range(n):
    print(x**2)


n = int(input("enter no."))
seen = []
for x in range(1 , n+1) :
    seen. append(str(x))
    print("".join(seen))


n = int(input("enter no."))
num = 1
lines = 1
while n != 0:
    print(num , end = "")
    lines -= 1
    print()
    num += 2
    lines = num -1
    n -=1

n = int(input("enter the no."))
for x in range( n , 0 , -1):
    for y in range(x):
        print(x , end = "")
    print()


n = int(input("enter a no."))
for x in range( n , 0 , -1):
    print("".join([str(y) for  y in range(x , 0 , -1)]))


n = int(input("enter the no."))

for x in range(n, 0 , -1):
    print("".join("*" for y in range(x , 0 , -1)))
    
    


