x = int(input("Enter the number of candies: "))
av = 5
y = 1
while y <= x:

    if y > av:
        break

    print("Candy")
    y += 1
print("\n\n\n")

for i in range (1,101):
    if i%3 == 0 or i%5 == 0:
        continue
    print(i)
print("\n\n\n")

for i in range (1, 101):
    if (i%2 != 0):
        pass
    else:
        print(i)

for i in range (1,11):
    print(i)