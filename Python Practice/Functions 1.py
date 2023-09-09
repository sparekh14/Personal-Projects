from numpy import *

def sum(x, y):
    z = x + y
    print(z)

a = array([1, 3])
sum(*a)