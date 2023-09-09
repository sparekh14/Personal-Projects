from numpy import *
from array import *

arr = array('i', [10, 12, 14, 16, 18, 20])

print(arr.buffer_info())
print(len(arr.buffer_info()))
print(bytes(len(arr.buffer_info())))
print(bytes(8))