def add_comp(Comp1, Comp2):
    print(f"{Comp1[0]+Comp2[0]} +- i({Comp1[1]+Comp2[1]})")

def sub_comp(Comp1, Comp2):
    print(f"{Comp1[0]-Comp2[0]} +- i({Comp1[1]-Comp2[1]})")

def mult_comp(Comp1, Comp2):
    print(f"{Comp1[0]*Comp2[0]} +- -({Comp1[1]*Comp2[1]})")

def divide_comp(Comp1, Comp2):
    print(f"{Comp1[0]/Comp2[0]} +- ({Comp1[1]/Comp2[1]})")


a = int(input("Enter Real part of first complex number : "))
b = int(input("Enter Imaginary part of first complex number : "))
Comp1 = (a,b)
print(f"{Comp1[0]} +- i({Comp1[1]})")
a = int(input("Enter Real part of Second complex number : "))
b = int(input("Enter Imaginary part of Second complex number : "))
Comp2 = (a,b)
print(f"{Comp2[0]} +- i({Comp2[1]})")

add_comp(Comp1,Comp2)
sub_comp(Comp1,Comp2)
mult_comp(Comp1,Comp2)
divide_comp(Comp1,Comp2)
