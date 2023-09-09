from array import *

arr = array('i', [])

x = int(input("Enter the number of values you want to append: "))


for i in range (x):
    y = int(input("Enter the value to append: "))
    arr.append(y)

print(arr)