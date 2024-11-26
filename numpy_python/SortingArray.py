# Sorting means putting elemnets in orderd sequence......

import numpy as n
arr = n.array([4,8,1,0,12,99,23,10,0])
arr1 = n.sort(arr)
print(arr1)


# filter Array.........
# getting some elements out of an exiting array and creating a new array out of them is called filtering.....

arr2 = n.array([41,45,7,9,10])
x = [True, True, False, False, True]
new_arr = arr2[x] # it will print elements which match the true....
print(new_arr)
