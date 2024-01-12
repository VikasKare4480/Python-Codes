
class Demo:

    def fun(self):
        print("In Demo fun")
    
class Memo:

    def gun(self):
        print('In Memo gun')

def callerFun(obj):

    if(type(obj) == type(fun)):
        obj.fun()
    else:
        obj.gun()

# int x = 10 SyntaxError
# Demo obj = Demo() SyntaxError

fun = Demo()

gun = Memo()

callerFun(fun)
