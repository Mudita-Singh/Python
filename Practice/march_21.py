'''num = int(input("enter the numerator :"))
deno = int(input("enter the denominetor :"))
try:
    quo = num/deno
    print("QUOTIENT :" , quo)
except ZeroDivisionError :
    print("denominator cannot be zero")

try:
  num = int(input("enter the number"))
  print( num **2)
except(KeyboardInterrupt):
  print("you should have entered a number...program terminating ")
except(ValueError):
  print("please check before you enter... program terminating")
print("Bye")


try:
   num=int(input("entyer the number")
           print(numm **2))
except(KeyboardInterrupt , ValueError , TypeError):
   print("please check before you enter ...program terminating...")
print("bye")   


try:
   file = pen('File1.txt')
   str = f.readline()
   print(str)
except IOError:
   print("could not convert data to an integer")
except ValueError:
   print("could not convert data to an integer")
except:
   print("unexpected error...program terminating")


try:
   file = open('File1.txt')
   str = file.readline()
   print(str)
except IOError:
   print("Error occurred during input..program terminating")
else:
   print("program terminating successfully")'''


   try:
      num = 10
      print(num)
      raise ValueError
except:
print("exception occured")

   try:
   raise Exception('Hello' , 'World')
except Exception as errorobj:
print(type(errorobj))
print(errorobj.args)
print(errorobj)
arg1 ,arg2 = erroronj.args
print('Argument1 =' , arg1)
print('Argument2 =' , arg2)
