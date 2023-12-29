
class Parent:

    z = 234
    def __init__(self):
        print('In Parents Cons')
        self.x = 10
        self.y = 20

    @classmethod
    def dispParent(self):
        print(Parent.z)

    def __del__(self):
        print('In Parents del')

# class Child(Parent):

#     def __init__(self):
#         print('In Child Cons')
#         # Parent.__init__(self)
#         super().__init__()

#     def __del__(self):
#         print('In childs del')
    
obj = Parent()
obj.dispParent()

