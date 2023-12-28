
class Demo(object):

    def __init__(self):
        print('In Demo Cons')
    
    def __init__(self, x):
        print('In Demo x')
    # always uses the latest object not the old one
    
obj = Demo(10)