import numpy as n
arr = n.array([1,2,3,4,5,6])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)

arr1= n.array([1,2,3,4,5])
y = arr1.view()
arr1[2]=45

print(arr1)
print(y)
