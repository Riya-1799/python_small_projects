import numpy as n

arr = n.array([1,2,3])
for x in arr:
    print(x)

arr1 = n.array([[[1,2,3],[7,6,5]],[[1,6,7],[12,14,16]]])
for x in arr1:
    for y in x:
        print(y)