

def decorFunc(fun):
    print('In decor')

    def wrapper():
        print('Start Wrapper')
        fun()
        print('End Wrapper')

    return wrapper

@decorFunc
def normalFunc():
    print('In Normal Func')

# normalFunc = normalFunc()
normalFunc()

