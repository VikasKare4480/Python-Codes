

def outer():

    def inner():

        return outer
    
    return inner

if __name__ == '__main__':

    retObj = outer()
    retInner = retObj()
    print(retInner) # Address of outer 

    # <function outer at 0x000002320F5F0B80>

