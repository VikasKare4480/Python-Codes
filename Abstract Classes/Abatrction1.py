
class Parent:

    def __init__(self):
        print('In Parent class Cons')
    
    def marry(self):
        print('in Parent Marry')

class Child(Parent):

    def __init__(self):
        print('in child cons')

    def marry(self):
        print('in child marry')


parentObj = Parent()
parentObj.marry()

childObj = Child()

childObj.marry() # Child   

print(Child.__mro__)
print(Child.mro())
    
