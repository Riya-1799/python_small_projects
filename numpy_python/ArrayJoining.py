#joining means putting contents of two or more arrays in single array

import numpy as n

arr1 = n.array([1, 2, 3])
arr2 = n.array([4, 5, 6])
arr = n.concat((arr1, arr2))
print(arr)

#stack Function.....
#we pass a sequence of arrays that we want to join to the stack() method along with the axis.
#if axis is not expilicity passed it is taken as 0

arr3 = n.stack((arr1,arr2),axis=1)
print(arr3)

#Stacking Along Rows..
#hstack() to stack along rows...
arr4 = n.hstack((arr1,arr2))
print(arr4)

#stacking along columns..
#Vstack() to satck along columns...

arr5 = n.vstack((arr1,arr2))
print(arr5)

#stacking along with Height....
#dtack() to stack height, which is the same as depth......

arr6= n.dstack((arr1,arr2))
print(arr6)
