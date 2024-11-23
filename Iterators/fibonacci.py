#Create an iterator for fibonacci series in such a way that each next returns the next element from fibonacci series.

class fibonacci:
    def __init__(self,limit):
        self.previous = 0 # last to second
        self.current = 1  # last one
        self.n = 0 # how many number already done
        self.limit = limit # up to what you want to generate take from user( user input)

    def __iter__(self):
        return  self   # it makes class iterable like java we are extending itreable class

    def __next__(self):
        if self.n >= self.limit:
            raise StopIteration
        if self.n == 0:  # Return the first Fibonacci number (0)
            self.n += 1
            return self.previous
        elif self.n == 1:  # Return the second Fibonacci number (1)
            self.n += 1
            return self.current
        else:
            result = self.previous + self.current
            self.previous=self.current
            self.current=result
            self.n = self.n + 1
            return result

number = int(input("untill which number you want to print Fibonacci series : "))

fib_iterator = iter(fibonacci(number))
while True:
    try:
        print(next(fib_iterator))
    except StopIteration:
        break

