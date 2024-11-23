#Create a set which only contains unique sqaures from a given a integer list.
integer = [1, -1, 2, -2, 3, -3]

sq_set = set()

for i in integer:
    a = i * i
    sq_set.add(a)
print(sq_set)
