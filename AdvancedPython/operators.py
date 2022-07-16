a = 2
b = 3
c = 4

if a < b < c: #a legal operation!
    print("yes!")

answer = a / b # normal division
print(answer)
answer = a // b # integer division
print(answer)

exp = a**b # exponentiation

x = [1, 2, 3]
y = [1, 2, 3]
print(x is y) #this is false, because they are not the same object
print(x == y) #this is true, because they have the same value

print(1 in x) #true
print(5 not in x) # also true
