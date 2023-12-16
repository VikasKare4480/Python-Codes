

def outer():

    def inner():
        return "Hello this is inner"
    
    return inner()

ans = outer()

print(ans)