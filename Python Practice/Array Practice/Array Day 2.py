from array import *

arr = array('i', [])

size = int(input("Enter the length of the array: "))

for i in range(size):
    x = int(input("Enter your value: "))
    arr.append(x)

val = int(input("Enter the desired value to search: "))

k = 0
for j in arr:
    if j == val:
        print(k)
        break
    else:
        print("Not in the array")
        break
    k+=1