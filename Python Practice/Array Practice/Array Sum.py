from numpy import *
import array as a

arr1 = array([10, 5, 12])
arr2 = array([13, 15, 16])
arr3 = array([])

for i in range(len(arr1)):
    arr3 = append(arr3, arr1[i]+arr2[i])

print(arr3)