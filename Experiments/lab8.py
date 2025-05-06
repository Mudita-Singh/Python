#1
file = open("names.txt", "w")
names = ["aName1\n","Namsaaaaaaaae2\n","Name3\n"]
file.writelines(names)
file.close()
file_read = open("names.txt","r")
content = file_read.readlines()
print("Names starting with vowel :")
for x in content:
    if (x[0] in ['a','e','i','o','u']):
        print(x)

print("Name with max length : ")
max_len_name = ""
for x in content:
    if (len(x) > len(max_len_name)):
        max_len_name = x
print(max_len_name)
file_read.close()

#2
file_write = open("integers.txt","w")
numbers = ["10\n","20\n","1\n","101\n"]
file_write.writelines(numbers)
file_write.close()
file_read = open("integers.txt", "r")
content = file_read.readlines()
content_converted = [eval(i) for i in content]

print("maximum number : ", max(content_converted))
print("average : ", sum(content_converted)/len(content_converted))
count = 0
for x in content_converted:
    if x > 100:
        count +=1

print(count, "number(s) greater than 100")

#3
file_read = open("City.txt", "r")

content = file_read.readlines()

def display(x):
    print("City : ",data[0])
    print("Population : ", data[1])
    print("Area : ", data[2])

big_data = []
for x in content:
    data = x.split(" ")
    big_data.append(data)
    display(x)

for x in big_data:
    if (eval(x[1]) > 10):
        display(x)

sum_num = 0
for x in big_data:
    sum_num += eval(x[2])
print("Sum Of Areas : ", sum_num)

#4
def add(lst):
    return lst[0]+lst[1]
def sub(lst):
    return lst[0]-lst[1]
def mult(lst):
    return lst[0] * lst[1]
def divide(lst):
    try: 
        return lst[0] / lst[1]
    except ZeroDivisionError:
        return "Can not divide by zero"

N = int(input("Enter number of test cases : "))
for x in range(N):
    inp = input("Enter the numbers a and b ")
    values = inp.split(" ")
    values = [eval(i) for i in values]
    print(add(values))
    print(sub(values))
    print(mult(values))
    print(divide(values))
