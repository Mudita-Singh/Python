def binaryToDecimal(binary):
    decimal = 0
    i = 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    print(decimal)
x = int(input("Enter the binary number : "))

binaryToDecimal(x)