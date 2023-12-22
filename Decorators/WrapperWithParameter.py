
def decorFun(func):

    def wrapper(*vargs):

        print('Start wrapper')
        val = func(*vargs)
        print('End wrapper')
        return val
    
    return wrapper

@decorFun
def normalFunc(x, y):
    print('In normal func')
    return x + y

x = int(input('Enter x :'))
y = int(input('Enter y :'))

print(normalFunc(x, y))



