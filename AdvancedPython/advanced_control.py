a = 15
b = 2
###### IMPORTANT MESSAGE ABOUT SCOPING ######
# while, if, etc do not change the scope of a variable.
if 1 == 1:
    if 2 == 2:
        if 3 == 3:
            j = 2
            while j < 10:
                j += 2
                if 4 == 4:
                    person_name = "bob"
# this is an extreme example, but you can see how this can be powerful 
print(person_name)


##### ONE-LINERS #####
if a > b: print("hi") #shorthand if conditions
print("hey") if a < b else print("ho") # ternary operator
# you can chain longer expressions together
print("a") if a> b else print("=") if a == b else print("b")

i = 4
while i < 6:
    print(i)
    i += 1
else: #run this at the end of a while loop! Does not execute after a break
    print("I is no longer less than 6")

##### FUN WITH FOR LOOPS #####
list_1 = [1, 2, 3]
list_2 = [7, 6, 5]

for i in range(0, 10, 2): #start, stop (exclusive), hop
    print(i) #counts evens

for i in reversed(range(0, 10, 2)): #start, stop (exclusive), hop
    print(i) #counts evens backwards

for i, elem in enumerate(list_1):
    print(i, elem)

for elem_1, elem_2 in zip(list_1, list_2):
    print(elem_1, elem_2) # concurrent list

for elem in sorted(list_2):
    print(elem) #this is how you sort a list and enumerate through it

#### ASSERTIONS ####
bob = True
assert bob == True, "Bob is not true" #good for sanity checks

###### EXCEPTIONS ######
try:
    x = 1 / 0
except TypeError: # you can catch specific exceptions
    print("type error!")
except ZeroDivisionError as err:
    print("Handing error", err)
except: # fall-through
    print("oops! A problem happened!")
else: #(optional) runs if there is no problem
    print("I ran without a problem!")
finally: #(optional) runs no matter what
    print("goodbye!")


# you can raise your own exceptions, which are just classes
# raise ValueError("Whoops!")

# try:
#     x = 1 / 0
# except ZeroDivisionError:
#     print("Divide by zero!")
#     raise #re-raise error

# you can even make your own error class
class MyError(Exception): #all error classes must inherit from Exception
    def __init__(self, message):
        self.message = message

# raise MyError("ha ha!")
