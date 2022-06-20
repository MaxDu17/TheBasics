# this file demonstrates how to use lambdas and maps

f = lambda x: -x
print(f(2)) # we just made a function!

y = [3, 2, 5, 3, 3]
y_sorted = sorted(y, key = f) # will sort in reverse order
y_mapped = list(map(f, y))

print(y)
print(y_sorted)
print(y_mapped)
