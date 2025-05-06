
#ques
'''l=[1,2,3,4,5,6]
print(l[0])
print()
for i in l:
    print(i)
t=len(l)
print()
for j in range(t):
    print(l[j])
print()
print(l[1:4])'''

#ques2:
'''l=[1,2,3,4,5,6]
print([h for h in l])
print()
t=[]
t.extend(l)
print(t)
l2=copy.deepcopy(l)
l[4]=100
print(l2)
print()
l3=copy.copy(l)
print(l3)'''

#ques
'''
l=[11,2,3,4,5,6,14]
p=[11,12,13,14,6]
l.insert(0,10)
print(l)
l.extend(p)
print(l)
l.append(p)
print(l)
x=p.count(14)
print(x)
print(max(p))
print(min(p))
print(p.index(13))
p.sort
print(p)
l.remove(4)
print(l)
'''

#ques

l=[11,2,3,4,5,6,14]
p=[11,12,13,14,6]
z=len(p)
for i in range(0,z):
    if l[i]==p[i]:
        print(l[i])
print()


#ques
l=[11,2,3,4,5,6,14]
p=[11,12,13,14,6]
l[0]=199
print(l)
l.extend(p)
print()
l.append(p)
print(l)
l.insert(3,600)
print(l)
