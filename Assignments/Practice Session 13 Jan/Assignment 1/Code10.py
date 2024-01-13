
class Prashant:

    def __new__(self):
        print("Memory allocated")
        
        # return object.__new__(self)

    def __init__(self):
        print("Const ")


obj = Prashant()

print("End of Program")
        