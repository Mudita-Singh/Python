
#ques1:
'''print("enter a no.:")
a= int(input())
if(a%2==0):
    print(a ,"is an even no.")
else:
    print(a,"is an odd no")'''

#ques1 b:
'''a=int(input("enter no."))
if a==1:
    print(a,"is not a prime no.")

elif a>1:
    for i in range(2,a-1):
        if(a%i==0):
            print("not a prime no.")
            break
        else:
            print("prime no.")'''

#ques2:
'''str=input("enter")
l=len(str)
for i in str:
    print(i)
for i in  range(l-1,-1,-1):
    print(str[i])'''

#ques3:
'''print("enter a str:")
a=input()
print("enter a substr:")
b=input()
if(b in a):
    print("hello")'''

#ques4:
'''s=" hello my name is aman "
l=s.split()
print(l)
print(len(l))
new=""
for i in range(len(l)-1):
    s=l[i]
    new+=(s[0].upper() + ".")
new+=l[-1].title()
print(new)'''

#ques5:
s='Hello World'
s.upper()
for i in s:
    print(i,"=", s.count(i))