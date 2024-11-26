# splitting is reverse opreation of joining...
# joining merges multiple arrays into one and spiliting breaks one array into multiple...

import numpy as n

arr = n.array([1,2,3,4,5,6])
new_arr = n.array_split(arr,3)
print(new_arr)

arr1 = n.array_split(arr,4)
print(arr1)

#spiliting 2-D Array......

arr2= n.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
arr3 = n.array_split(arr,3)
print(arr3)