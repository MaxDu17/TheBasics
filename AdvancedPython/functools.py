import functools

basetwo = functools.partial(int, base=2) # essentially fills out the function int(XX, base = 2) and you later go back and fill in "XX"
print(basetwo('10010'))

@functools.cache #allows for dynamic programming
def factorial(n):
    return n * factorial(n-1) if n else 1

print(factorial(3))
print(factorial(10))
