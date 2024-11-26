# you can search and Array for a certain value and return the index that get match , where() method

import numpy as n
arr = n.array([1,2,3,4,5,6,7,8,9,10,134567,789])
x = n.where(arr==2)
y = n.where(arr==12)
print(x)
print(y)

z = n.where(arr%2 == 0)
print(z)

# Search sorted
# perfroms a binary search in the Array, and returns index where the specified value would be insterted to maintain the search order.

arr1 = n.array([1,5,7,8,9,0])
xx = n.searchsorted(arr1,7)
print(xx)
#search from right side....
xy = n.searchsorted(arr1,7,side='right')
print(xy)

