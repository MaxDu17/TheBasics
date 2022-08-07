# python decorator is just basically a wrapper function
# inspired by https://realpython.com/primer-on-python-decorators/

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# a decorator just wraps the function in something else
# this allows you to modify a function's behavior drastically
@my_decorator
def say_whee():
    print("Whee!")

@my_decorator
def say_squeak():
    print("Squeak!")

say_squeak()
say_whee()

# decorators that use parameters
def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper

@do_twice
def greet_person(name):
    print(name)

greet_person("bob")
