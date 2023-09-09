nums = [13, 18, 25, 23, 28]

for i in nums:
    if i%5 == 0:
        print(i)
        break
    if i%3 == 0:
        print(i)
else:
    print("Not Found")