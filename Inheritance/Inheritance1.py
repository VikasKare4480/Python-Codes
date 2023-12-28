

class Parent:

    def __init__(self):
        print('In Parent Cons')

    def parentFunc(self):
        print('In Parents Fun')
    

class Child(Parent):

    def __init__(self):
        # call to parent constructor
        super().__init__() # 1 way
        Parent.__init__(self) # 2 way
        Parent() # 3 way not a recommended
        print('In Child Cons')
    
    def childFunc(self):
        print('In Child Fun')


obj = Child()
obj.parentFunc()
obj.childFunc()