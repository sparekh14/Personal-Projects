def fact(x):
    a = 1
    for i in range(1, x+1):
        a = a*i
    return a


x = int(input("Enter a value for a factorial: "))
factorial = fact(x)
print(factorial)