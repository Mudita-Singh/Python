#Printing Odd number between a and b

def odd_number(a,b):
    for i in range(a,b+1):
        if a%2!=0:
            print(a)
        a+=1

a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
if(a<b):
    odd_number(a,b)
else:
    print("Enter the number such that a<b")