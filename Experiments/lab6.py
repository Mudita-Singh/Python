#1
'''from collections import Counter
arr =[]
for x in range(3):
    arr.append(int(input("Enter the number")))
    print(Counter(arr))

'''
#2
'''nums = int(input("number of terms"))
summ = 0
for x in range (nums):
      summ += int (input("number to add"))
print(summ/nums)'''

#3
'''N=(10 , 12 , 13, 888  , 74)
def runner_up(x):
        x = sorted(x)
        return x [-2]
print(runner_up(N))'''

#4
n_p = { "anuj" : "india",
       "mud" : " china",
       "dhak" : "korea",
       "ani" : " japan"}

seen = []
for x in n_p:
   stu = 1
   if n_p[x] in seen :
    stu +=1
    seen.append([n_p[x], stu])
    print(n_p.keys())
    print(n_p.values())
    print(n_p.items())
    print(seen)

