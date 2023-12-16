

class Empleyee:

    def __new__(self):
        print("in the new method")
        return super().__new__(self)

    def __init__(self):
        print("in the init")
        self.name = "Google";
        self.emplyeeCount = 500

    def display(self):
        print("in the display")
        print(self.name)
        print(self.emplyeeCount)


empObj = Empleyee();

# print(id(empObj))?
print(type(empObj.display))
empObj.display()



