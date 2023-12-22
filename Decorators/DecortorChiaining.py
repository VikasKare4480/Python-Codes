
def decorFun(func):

    print('In decorFun')

    def wrapper():
        print('Start Wrapper Fun')
        func()
        print('End Wrapper Fun')

    return wrapper

def decorRun(func):

    print('In decorRun')

    def wrapper():

        print('Start wrapper Run')
        func()
        print('End wrapper Run')

    return wrapper

@decorFun
@decorRun
def normalFunc():
    print('In normal func')

normalFunc()

