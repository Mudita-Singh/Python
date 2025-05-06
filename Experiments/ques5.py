def mul_vector(vector1, vector2):
    mul_vector = tuple([x * y for x, y in zip(vector1, vector2)])
    print(mul_vector)

vector1 = []
vector2 = []
for x in range(5):
    a = int(input("Enter the element to be inserted : "))
    vector1.append(a)
for x in range(5):
    a = int(input("Enter the element to be inserted : "))
    vector2.append(a)
vector1 = tuple(vector1)
vector2 = tuple(vector2)

mul_vector(vector1,vector2)