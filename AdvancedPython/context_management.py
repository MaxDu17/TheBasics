# this is most commonly used for files, but it's also used for anything that has a certain "state" of being
# with open("test.txt", "r") as f:
#     content = f.read()
#     print(1 / 0) #oops! But don't worry, we still release the file.

# thsi is how to make your own context manager
class MyContext():
    def __enter__(self):
        print("yee") # guarenteed execution
    def __exit__(self, type, value, traceback):
        print("haw!") # guarenteed execution

with MyContext() as c:
    print("here")
    print(1 / 0) # another oopsie!
