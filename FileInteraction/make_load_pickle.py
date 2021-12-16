import pickle

class TestClass():
    def __init__(self):
        self.test = 1
        self.testanother = "b"


k = TestClass()
with open("samples/testpkl.pkl", "wb") as f:
    pickle.dump(k, f)
    print("done saving!")


with open("samples/testpkl.pkl", "rb") as f:
    k = pickle.load(f)
    print(k.test)
    print(k.testanother)
    print("done loading!")