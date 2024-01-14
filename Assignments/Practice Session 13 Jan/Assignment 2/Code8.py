

def outer():

    msg = "I am outer function"

    def inner():

        return msg
    
    return inner

if __name__ == '__main__':

    inner_function = outer()
    result = inner_function()
    print(result) # msg will be printed


    


