#1
print([x**2 for x in range(1,51)])

#2
s = "the length of str"
print(sum(1 for x in range(len(s))))
print(len(s))

#3
s = "the length of str"
print("".join(s[x] for x in range(len(s) -1 , -1 , -1)))

#4
def is_prime(n):
    if n<= 1:
        return False
    return True
prime_no = [no for no in range(3 , 51,2) if is_prime(no)]
print(prime_no[2])

#5
print([i for i in range(1,1001) if sum(int(digit)**3 for digit in str(i)) == 1])


#6
num = [x for x in range(11)]

l,r = 0 , len(num)- 1
tar = 9
while l<r:
    mid = (l+r)//2
    if num[mid] > tar:
        r -=1
    elif num[mid] <tar:
        l +=1
    else:
        print("the target is at idx {mid}")
        break
    print(num.index(9))

#7
for x in range(1,6):
    print("".join([str(x) for x in range(x+1 , 6)]))

