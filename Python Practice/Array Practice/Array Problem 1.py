from array import *

size = int(input("Enter the size of the array: "))

arr = array('i', [])

for i in range(size):
    val = int(input("Enter your value: "))
    arr.append(val)

value = int(input("Enter the index for your search: "))

for j in range(size):
    if arr[j] == value:
        print(j)
        break