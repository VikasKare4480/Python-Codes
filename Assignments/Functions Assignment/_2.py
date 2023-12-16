def outer():

    def inner():
        return "Hello this is inner"
    return inner

retObj = outer()
retInner = retObj()
print(retInner)