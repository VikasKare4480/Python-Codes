
def outer():

    
    def inner(outer):

        print(outer) # address of outer
        return inner
    
    return inner(outer)

if __name__ == '__main__':

    retObj = outer()
    print(retObj) # address of inner

# <function outer.<locals>.inner at 0x00000169DF8DDB20>
