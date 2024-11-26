import numpy as n

# The function  nditer() is a helping function that can be used from very basic to very advanced iterations....

arr = n.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in n.nditer(arr):
    print(x)