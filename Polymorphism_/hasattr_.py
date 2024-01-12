
class Demo:

    def fun(self):
        print('In Demo fun')
    
class Memo:

    def fun(self):
        print('In Memo fun')


def callerFun(obj):

    if hasattr(obj, 'fun'):
        obj.fun()

    elif(hasattr(obj, 'gun')):
        obj.gun()

    else:
        print('No Match')

demo = Demo()
memo = Memo()

# print(Demo.__mro__)
# print(Demo.mro())

callerFun(demo)
callerFun(memo)

