
class Math:
    
    def __init__(self):
        print('This is Mats Cons')

class Demo(Math):

    def __init__(self): 
        print('In Demo Cons')
        self.x = 10;
        self._y = 20; # private variable
        self.__z = 30; # pubic variable _Demo__z

    # this is private method
    def __fun():
        print('In Demo fun')
        return 'This is private variable'
    
print(dir(Demo))

obj = Demo()

print(dir(obj))
print(Demo.mro()) # DFS (Stack) for getting the order 

print(obj._Demo__z)
print(Demo._Demo__fun())






