# variables are dynamically created upon assignments. If you must "initialize" something, use
this_var = None
print(id(this_var)) # even though it is none, the variable already has a tracker

x, y, z = 1, 2, 3 #tuple unpacking assignments
x = y = z = 1 # chain of equality assignment
w = float(x) #how you cast

####### tricks with objects ######
x = [1, 2, 3, 4]
y = [8, 9, 10]
print(isinstance(x, list)) #check if something is an instance of something else. Works for all parents of the object too
print(x.__sizeof__()) #size in bytes

#### MORE ABOUT SCOPES ####
global_var = "steve"

def my_funct():
    global global_var #connects directly to the global variable
    print(global_var)

my_funct()

#### TRUTH VALUE OF THINGS #####
# most values are true
bool([1, 2, 3]) # true
print(bool(3)) # true; all non-zero numbers are true, inclluding negatives
print(bool([False])) #true; all non-empty datastructures are true
print(bool([[]])) # true; it's also not empty
print(bool([])) #false
print(bool(0)) #false
