
def decorFun(func):

    def wrapper():
        print('In wrapper')
        func()
        print('Out wrapper')
    return wrapper

@decorFun
def normalFunc():
    print('Normal function')

normalFunc()

# def keyWardArgs(**kargs):

#     sum = 0
#     for key, value in kargs.items():
#         sum += value

#     return sum

# print(keyWardArgs(x = 20, y = 90, z = 60))
