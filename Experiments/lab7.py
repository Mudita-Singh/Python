
# Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
def find_max_min(numbers):
    if not numbers:
        return None, None  

    max_num = numbers[ 0]  
    min_num = numbers[0]  

    for num in numbers[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return max_num, min_num

numbers = [3, 1, 7, 9, 2, 5]
max_num, min_num = find_max_min(numbers)
print("max no.", max_num)
print("Min no.", min_num)

# Write a Python function that takes a positive integer and returns the sum of the


def sum_of_cubes(n):
    if n <= 0:
        return 0

    sum_cubes = 0
    for i in range(1, n):
        sum_cubes += i ** 3

    return sum_cubes

num = int(input("enter a pos int "))
result = sum_of_cubes(num)
print("Sum of the cubes of pos integers smaller than", num, "is", result)



# Write a Python function to print 1 to n using recursion. ( Do not use loop)


def print_numbers_recur(n):
    if n < 1:
        return  
    else:
        print_numbers_recur(n - 1)  
        print(n)


num = int(input("enter a pos int "))
print("No. from 1 to", num, "using recur")
print_numbers_recur(num)


# Write a recursive function to print Fibonacci series upto n terms


def fibonacci(n, a=0, b=1):
    if n <= 0:
        return
    print(a, end=" ")
    if n == 1:
        return
    else:
        fibonacci(n-1, b, a+b)


terms = int(input("enter no. of terms in series "))
print("Fibonacci series up to",terms, "terms")
fibonacci(terms)



# Write a lambda function to find volume of cone


cone_volume = lambda r, h: (1/3) * 3.14159 * r**2 * h
radius = float(input("enter the radius "))
height = float(input("enter the height "))

volume = cone_volume(radius, height)
print("volume of the cone:", volume)



# Write a lambda function which gives tuple of max and min from a list.

get_max_min = lambda lst: (max(lst), min(lst))

input_list = [10, 6, 8, 90, 12, 56]
result = get_max_min(input_list)
print("Sample input:", input_list)
print("Sample output:", result)

# Write functions to explain mentior repts:

def greet(name, message):
    print(f"Hello, {name}! {message}")

greet(message="heyy?", name="sky")
greet("Bob")
greet("Alice", "How are you?")

def add(*args):
    result = 0
    for num in args:
        result += num
    return result

print(add(1, 2, 3))
print(add(4, 5))
print(add(6, 7, 8, 9))






