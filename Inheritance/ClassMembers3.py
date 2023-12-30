

class Demo(object):

    def __init__(self):
        print('In init')

    def __del__(self):
        print('In del')
    
def fun(): # StackFrame on Stack 
    
    print('Start fun')
    obj = Demo()
    print('End fun')

fun()
print('End Code')