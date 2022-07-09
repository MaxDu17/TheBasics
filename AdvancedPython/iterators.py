# you've used iterators a lot
# for i in range(10): #this "range" is an iterator
#     print(i)

# you can make a custom iterator
class IterClass():
    def __iter__(self): #returns the iterator, which can be yourself
        self.index = 0
        self.values = [1, 2, 3, 4, 5]
        return self

    def __next__(self):
        if self.index < len(self.values):
            x = self.values[self.index]
            self.index += 1
            return x
        else:
            raise StopIteration # when you're done

    def __len__(self):
        return len(self.values)

my_class = IterClass()
my_iter = iter(my_class) # constructs the iterable
for x in my_iter:
    print(x)

# alternatively you can use next(my_iter)

# you can also make a "generator", which creates iterators
def printdata():
    for i in range(10):
        yield i * 2 # pauses at each iteration

for num in printdata():
    print(num)
