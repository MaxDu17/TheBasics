class Cetacean():
    def __init__(self):
        print("Initializing Cetacean")

    def breach(self):
        print("cetacean breach")

    def make_sound(self):
        raise NotImplementedError # if you require a function (abstract class), this is how you do it

class Dolphin(Cetacean):
    def __init__(self):
        super().__init__()
        print("\tInitializing Dolphin")

    def make_sound(self): # overrides the function that would have raised a non-implementation error
        print("Dolphin noise")

x = Dolphin()
x.breach() #note how it is inherited

class PilotWhale(Cetacean):
    def __init__(self):
        super().__init__() #you need this a
        print("\tInitializing PilotWhale")

        # this one is very confusing!
        self.make_sound() # you can reference somethign that hasn't been implemented yet, in the hopes that the child will

    def breach(self):
        print("Pilot Whale Breach")
        # super().breach() #use this to call the superclass


class Bubbles(PilotWhale):
    # no init means you use the parent's init
    def make_sound(self): # we don't declare make_sound in the parent, so we do it here
        print("Hi i'm bubbles")

x = Bubbles()
x.make_sound()
