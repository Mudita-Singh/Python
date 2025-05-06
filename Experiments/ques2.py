def repeat_letters(name):
    len=len(name)
    while(len!=0):
        print(name,end="")
        len-=1
name=input("Enter the string:")
repeat_letters(name)
