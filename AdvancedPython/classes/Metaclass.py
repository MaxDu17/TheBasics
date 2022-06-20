# meta-classes create classes.
# all classes, unless said otherwise, are from metaclass type()

# now, type() can create a class directly for you, just like how classes
# can make objects directly:
Whale = type("Whale", (), dict(environment="water", weight = "heavy"))
x = Whale()
print(x.environment) #so we just generated a new class from the metaclass

# now, let's make our own type()-style meta-class!
class MyMeta(type):
    # bases is the inherited classes
    def __new__(cls, clsname, bases, clsdict):
        print("Custom metaclass!")
        class_instance = super().__new__(cls, clsname, bases, clsdict)
        print("doing something here, perhaps")
        return class_instance

# in defining this, we will print "Custom metaclass!"
class Whale(metaclass=MyMeta):
    pass

class Dolphin(Whale): #same thing!
    pass

