from collections import deque

# deque (ring buffer)
queue = deque(['name', 'age', 'DOB']) #normal deque (better complexity)
ring_buffer = deque([], maxlen=10) #ring buffer!
print(queue)

# lists
structure = [1, 65, 3, 6, 3]
if 1 in structure:
    print("yes!")
print(structure.count(1)) #number of elements with this number
print(structure.index(65, 0, 2)) #find an item between indexes [0, 2]

structure[0:3] = [12542] #replaces 0, 1, 2 elements with a singular 12542
print(structure)

structure.pop() #removes the last element
print(structure)

structure.reverse() #reverse the list
structure.sort() #sort the list

# dictionaries
b = {"one" : 1, "two" : 2}
print(b["one"]) #square bracket if you are sure that it exists
b.get("three") #returns none, intstead of throwing an error
for val in b.values():
    pass # 1, 2

for key in b.keys():
    pass #one, two

for key, value in b.items():
    print(key, value) #one 1  two 2

del b["one"] #removes this
print(b)

