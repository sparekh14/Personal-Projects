from numpy import *

arr = array([10, 12, 12, 12, 14, 16, 16, 18, 20])

streak = 0

value = int(input("Enter a value: "))

for i in range(len(arr)):
    if i < 9:
        if arr[i] == value:
            streak += 1

print(streak)