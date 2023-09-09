x = int(input("Enter a number: "))
prime = True
for i in range(2, int(x/2)):
    if x%i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

