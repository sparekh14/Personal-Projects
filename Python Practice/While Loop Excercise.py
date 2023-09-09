x = 1
while x <= 100:
    if (x%3 == 0 or x%5 == 0):
        print()
    else:
        print (x)
    x += 1
print("\n\n\n")

y = 1
while y <= 4:
    print("# ", end = "")
    z = 1
    while z <= 3:
        print("# ", end = "")
        z += 1
    y += 1
    print()