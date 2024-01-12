
class Parent:

    def property(self):
        print('Gold Car Banglow')

    def carreer(self):
        print('Engineering')

class Child(Parent):

    def carreer(self):
        Parent.carreer(self)
        print('Business Person')


obj1 = Child()
obj1.property()
obj1.carreer()

        

    
