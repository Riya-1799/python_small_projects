#joining means putting contents of two or more arrays in single array

import numpy as n

arr1 = n.array([1, 2, 3])
arr2 = n.array([4, 5, 6])
arr = n.concat((arr1, arr2))
print(arr)
