
class Demo:

    def fun(self):
        print('In Demo Fun')
    
class Memo:

    def fun(self):
        print('In Memo fun')


def callerFun(obj): 
    obj.fun()
    
obj1 = Demo()
obj2 = Memo()

callerFun(obj2) # In Memo function
callerFun(obj1) # In Demo function


