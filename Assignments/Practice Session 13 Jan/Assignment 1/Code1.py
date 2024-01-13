
def outer():

    def inner():
        return 'Hello In inner function'
    
    return inner()

ans = outer()
print(ans) 

# Output

# Hello In inner function