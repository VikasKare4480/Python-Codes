

def outer():

    def inner():
        return 'Greetings from the inner functio'
    
    return inner

if(__name__ == '__main__'):

    innObj = outer()
    print(innObj())
