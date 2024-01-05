
class Parent1:

    def __init__(self):
        print('In Parent1 Cons')
    
    def dispData(self):
        print('In parent1 dispdata')
    
class Parent2:

    def __init__(self):
        print('Parent2 Cons')
    
    def dispData(self):
        print('In Parent2 printData')

class Child(Parent1, Parent2): # Right hand thumb rule so Parent1 having the highest Priority
    pass

obj = Child()

print(dir(obj))
print(Child.mro()) 
obj.dispData()
# obj.printData()

        