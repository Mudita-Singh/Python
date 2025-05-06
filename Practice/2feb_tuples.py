'''tup=('rakesh' , 23, 6.2 , False)
print(tup[0])
print(tup[-1])
tup_num = (1,2,3,4)
tup_num[2]= 5'''


'''T1 = (1,2,3)
print(T1*2)
T2 = (4,5,6)
print(T1 +T2)'''


'''thistuple= (1,3,7,8,7,5,4,6,8,5)
x= thistuple.count(5)
print(x)
x =thistuple.index(7)
print(x)'''


'''alphabets = ('G ' ,'e' ,'e' , 'k', 's' , 'f' , 'o' , 'r' , 'G' , 'e' , 'k' , 's')
index = alphabets.index('G' , 4 , 10)'''

'''l=[]
for i in range(3):
    l.append(int(input(f"enter the {i+1} value: ")))

z=[]
for j in l:
    z.append(l.count(j))
print(z)'''

'''t=()
n=int(input("enter the no. of entries: "))
for i in range(n):
    tuple(int(input("enter a no.: ")))'''


'''set1 = {1,2, 3,4,5}
print(set1)'''

'''my_set = {1.0 , "Hello" , (1,2,3)}
my_set =set([1,2,3,2])
print(my_set)'''

thisset= {"apple" , "banana", "cherry"}
print(len(thisset))
myset = {"apple" , "banana" , "cherry"}
print(type(myset))

thisset = set(("apple" , "banana" , "cherry"))
print(thisset)

print("banana" in thisset)
thisset = {"apple" , "banana" , "cherry"}
thisset.add("orange")
print(thisset)
tropical = {"pineapple" , "mango", "papaya"}
thisset.update(tropical)
print(thisset)
thisset.remove("banana")
print(thisset)
thisset.discard("banana")
print(thisset)
thisset = {"apple", "banana" , "cherry"}
del thisset
print(thisset)



