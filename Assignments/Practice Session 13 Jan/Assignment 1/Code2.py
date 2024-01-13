
def outer():

    def inner():

        return "Hello i am inner function"

    return inner

retObj = outer()
retInner = retObj()
print(retInner)

# // Output

# Hello I am inner function