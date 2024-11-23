
def next_square():
    i = 1
    while True:
        yield i * i
        i = i + 1


number = int(input("enter the number: "))

for n in next_square():
    if n> number:
        break
    print(n)


