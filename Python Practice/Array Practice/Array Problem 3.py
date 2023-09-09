from array import *

vals = array('i', [10, 11, 7, 6, 4, 1])
for i in range(0, len(vals)):
    for j in range(i, len(vals)):
        if(vals[i] > vals[j]):
            vals[i], vals[j] = vals[j], vals[i]
for i in range (0, len(vals)):
    print(vals[i], end=" ")