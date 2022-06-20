import itertools

# infinite iterator
# for i in itertools.count(10):
#     print(i)

# infinite rotation
# for c in itertools.cycle([1, 2, 3, 4, 5]):
#     print(c)

# repeat 10 three times
for c in itertools.repeat(10, 3):
    print(c)

# # accumulates the iterated value
for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i)

# linearizes things
for i in itertools.chain.from_iterable([[1, 2, 3], [4, 5, 6]]):
    print(i)

# iterate through a bunch of combinations of values.
# repeat is the number of digits you want in the output
for i in itertools.product([0, 1], repeat = 3):
    print(i) # prints out all the binary representations

for i in itertools.permutations([1, 2, 3, 4], 2):
    print(i)

for i in itertools.combinations([1, 2, 3, 4], 2):
    print(i)

for i in itertools.combinations_with_replacement([1, 2, 3, 4], 2):
    print(i)
