# If, Elif, Else Statements

x = int(input("Enter a number: "))

if (x > 0):
    print("Positive\n")
elif (x < 0):
    print("Negative\n")
else:
    print("Zero\n")

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if (a > b and a > c):
    print("%d is the greatest\n\n\n" %a)
if (b > a and b > c):
    print("%d is the greatest\n\n\n" %b)
if (c > a and c > b):
    print("%d is the greatest\n\n\n" %c)

# While Loop
x = int(input("Enter a number: "))