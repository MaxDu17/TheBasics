#this will read to a file
with open("samples/sample.txt", "r") as f: #we are not in binary mode so there is no 'b'
    raw_text = f.read() #this reads the whole thing
    print(raw_text)
    #let's play around with file pointers
    print("now some fun seeking")
    print(f.tell()) #how many characters we have consumed
    f.seek(0) #brings us back to the beginning (shorthand)
    #second argument: 0 means from beginning, 1 means from current position, and 2 means end

    #negative indexing is only supported in binary mode
    f.seek(0, 2) #moves to the end
    f.seek(0, 1) #stays where we are
    f.seek(0, 0) #moves to the beginning

    #now, let's say we wanted to get line by line
    lines = f.readlines()
    print(lines)
    f.seek(0)

    chunk = f.read(10)
    print(chunk)

#alternatively, you can use the open() and f.close() without using the "with" syntax, though what we have here is more reliable

# now, writing!

#this will write to a file
text = '''I remember when rock was young
Me and Susie had so much fun
Holding hands and skimming stones
Had an old gold Chevy, and a place of my own
But the biggest kick I ever got
Was doing a thing called the Crocodile Rock
While the other kids were rocking 'round the clock
We were hopping and bopping to the Crocodile Rock, well'''

lines = ["this", "is", "a", "test"]

with open("samples/sample_written.txt", "w") as f: #use "a" to append to a file
    f.write(text)
    f.writelines("\n".join(lines)) #this adds an endline between each element of the list

with open("samples/sample.txt", "r") as f:
    for line in f: #another way of iterating through a file
        print(line)
