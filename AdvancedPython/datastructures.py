from collections import deque
import queue

##### COPYING ######
# remember that all python non-primitives are passed by reference
x = list()
y = x
y.append(1)
x.append(2)
# these print the same thing
print(x)
print(y)

# to prevent this, just use a copy!
x = list()
y = x.copy()
y.append(1)
x.append(2)
print(x)
print(y)
########### QUEUE ##############
# you can just use .append() and .pop(), but for multithreading, you should use the actual queue module
structure = queue.Queue()
structure.put(1)
print(structure.qsize()) # size of the queue
print(structure.get()) # removes that element
# there is no way of peeking into the queue, due to race condition problems

############### LISTS ######################
structure = [1, 65, 3, 6, 3]
if 1 in structure: # searching for elements
    print("yes!")
print(structure.count(1)) #number of elements with this number
print(structure.index(65, 0, 2)) #find an item between indexes [0, 2]

structure[0:3] = [12542] #replaces 0, 1, 2 elements with a singular 12542
print(structure)

structure.pop() #removes the last element
print(structure)

structure.reverse() #reverse the list
structure.sort() #sort the list

######### DICTIONARIES ###########
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

############## SETS #################
b = {1, 6, 4, 8, 8} # creates {8, 1, 4, 6} set
a = {1, 4, 21}

c = b - a # difference
c = a | b # union
a.update(b) #in-place union
c = a & b # intersection
c = a ^ b # symmetric difference

############## TUPLES #################
# immutable, but if they refer to objects, these objects can be modififed
b = ("test", ) # the extra comma indicates that it's a tuple
b = ("test", "rat", "mouse",)
t, r, m = b # tuple unpacking
b = (t, r, m) #tuple packing

x = 2
y = 3
x, y = y, x # quick value swap using implicit tuple packing!

############ DEQUE #############
q = deque(['name', 'age', 'DOB']) #normal deque (better complexity)
ring_buffer = deque([], maxlen=10) #ring buffer!
print(q)
