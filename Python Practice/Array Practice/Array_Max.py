from numpy import *

arr = array([10, 12, 21, 13, 20])

max = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]

print(max)
