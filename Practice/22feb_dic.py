'''d2= dict(name="raju",country="india")
print(d2)
d1={"k1":"01","k2":"02,","k3":[1,2,3]}
print(d1)
print(len(d1))
print(type(d1))
print(d1, get("k1"))'''
d3={10:"a",20:[1,2,3],30:"c"}
'''
d3[10]=100
d3[20][1]=12
d3[20]=110
print(d3)'''
d4={"name":"raju","age":32,"country":"india"}
'''x=d4 keys()
print(x)
y=d4 values()
print(y)
z=d4 items()
print(z)
x={"k1","k2"}
y=0
d=dict.fromkeys(x,y)
print(d)
a={"name":"raju","country":"india"}
print(a.keys())
print(a.values())
car={"brand":"ford","model":"mushtang","year":1994}
car.update({"brand":"hello"})
print(car)
student={"s1":9,"s2":1}
print(student)
suspend=student.pop("s1")
print("suspended student="+str(suspend))
print("remaining="+str(student))'''
'''nested={"dict1":{"k1":"100"},"dict2":{"k2":"200"}}
print(nested,type(nested))
print("\ndelecting dic1")
nested.pop("dict1")
print(nested)'''

#copying
dict1={10:"a",20:[1,2,3],30:"c"}
print("given dictionary:",dict1)
dict2=dict1.copy()
print("new copy:",dict2)
dict2[10]=10
dict2[20][2]=45
print("updated copy:",dict2)
dict2.clear()
print(dict2)
print(dict1.get("10"))
print(dict1.get(10))

#values method
car={"brand":"ford","model":"mustang","year":"1992"}
x=car.values()
car["year"]=2012
print(x)

#sorting lists
numbers=[3,1,5,7,2,9,10,34,2,6]
numbers.sort()
print(numbers)

#sorting tuples
tuple1=(10,22,4,7,33,1,100,9)
x=tuple(sorted(tuple1))
y=sorted(tuple1)
print(y,type(y))
print(x,type(x))

#sorting dictionary by keys
dict1={"one":1,"three":3,"two":2,"four":4}
a=dict(sorted(dict1.items()))
print(a)

#sorting by values
dict2={"one":1,"three":3,"two":2,"four":4}
z=dict(sorted(dict2.items(),key=lambda item: item[1]))
print(z)

#typecating
my_set = {1,2,3 ,4,5}
list_from_set= list(my_set)
print(list_from_set)

my_set = {1,2,3,4,5}
tuple_from_set = tuple(my_set)
print(tuple_from_set)









