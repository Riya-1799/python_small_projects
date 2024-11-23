#Create a Dictionary which contains the Binary values mapping with numbers f
# ound in the below integer and binary and save it in binary_dict.

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
binary_dict = {}
for i in integer:
    for j in binary:
        binary_dict[i] = j


print(binary_dict)
