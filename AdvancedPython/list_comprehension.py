mylist = [1,5,3,7,3,7,3,7,4,8,4,8,4,7,4,7,54] # some random list
anotherlist = ["dog", "cat", "ferret", "quokka", "dik-dik"]
mydict = {"shamu" : "orca", "mickey": "mouse", "Obama": "human"}

x = [item + 1000 for item in mylist] #simple comprehension
print(x)
x = {key.upper() : value for key, value in mydict.items()} #we can modify the key and value in a dictionary
print(x)
# in reality, the iterable can be lit, tuple, set, range, etc

## Now, let's more onto something more complicated
x = [item + 1000 for item in mylist if item % 2 == 0] #selects evens only
print(x)
# you can put a conditional after the iterable. this is a selection condition (i.e. if it's not satisfied, it's not in the list)
# you can also put a conditional before the iterable. This is a modification conditional
x = [item + 1000 if item % 2 == 0 else item - 1000 for item in mylist] #selects evens only
print(x)

## we can do nested
x = [[i + j for i in range(3)] for j in range(3)]
print(x)
x = [(i, j) for i in range(5) for j in range(5)] # a good way of generating coordinates!
print(x)
