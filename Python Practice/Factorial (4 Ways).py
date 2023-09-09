from math import *

def fact1(num):
    fact = factorial(num)

    return f"The factorial of {num} is {fact}."

def fact2(num):
    if num == 1:
        return 1
    else:
        return num*fact2(num-1)

def fact3(num):
    total = 1
    for i in range(1, num+1):
        total *= i

    return f"The factorial of {num} is {total}."

def fact4(num):
    total = 1
    i = 1
    while i in range(num+1):
        total *= i
        i += 1
    
    return f"The factorial of {num} is {total}"

number = int(input("Enter a number: "))

print(fact1(number))
print(f"The factorial of {number} is {fact2(number)}.")
print(fact3(number))
print(fact4(number))