# Random means that cannot be predicted.......

#pesudo random and True Random...
#Computers work on programs, and programs are definitiva setof instructions. So, it mens there must be
# some algorithm to genrate a number as well.

from numpy import random

x = random.rand(100)
print(x)

y = random.rand()
print(y)

z = random.randint(100,size=5)
print(z)

a = random.randint(100,size=(3,5))
print(a)

b = random.rand(5)
print(b)


