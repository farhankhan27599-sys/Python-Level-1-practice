# PROGRAM TO FIND THE PRIME NUMBER

'''
num = int(input("Enter a number: "))

if num > 1:

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number")

else:
    print("Not a Prime Number")
'''

# PROGRAM TO FIND FACTORIAL OF A NUMBER
'''
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("Factorial does not exist for negative numbers")

elif num == 0:
    print("Factorial of 0 is 1")

else:
    for i in range(1, num + 1):
        factorial *= i

    print("Factorial is:", factorial)

'''

#program to check if the string is palendrom
'''
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

'''
#PROGRAM TO FIND FIBONNOCCI SERIES
'''
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter number of terms: "))

for i in range(n):
    print(fibonacci(i), end=" ")

'''

#PROGRAM TO FIND SUM OF DIGITS
'''
num = int(input("Enter a number: "))

sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum of digits is:", sum)

'''