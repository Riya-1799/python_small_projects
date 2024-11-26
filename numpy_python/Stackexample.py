import numpy as n

# we pass a sequence of arrays that we want to join to the stack method along withe the axis.....
# if axis is not explicity passed it is taken as 0


arr1= n.array([1,2,3])
arr2= n.array([3,4,5])
arr = n.stack((arr1,arr2),axis=1)
print(arr)