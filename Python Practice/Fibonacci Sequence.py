def fib1(x):
    a = 0
    b = 1
    if x == 1:
        print(a)
    elif x <= 0:
        print("You have entered an invalid value.")
    else:
        print(a)
        print(b)
        for i in range(2, x):
            c = a + b
            a, b = b, c
            print(c)

x = int(input("Enter the number of numbers you want in the fibonacci sequence: "))
fib1(x)


print("\n\n")


def fib2(y):
    i = 1
    a = 0
    b = 1
    print(a)
    print(b)
    while i > 0:
        c = a + b
        a, b = b, c
        if c <= y:
            print(c)
        else:
            break
        i += 1

y = int(input("Enter the number you want to stop at: "))
fib2(y)