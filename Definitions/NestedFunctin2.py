


# method returning address of method itself 

def narheCampous() -> object:

    def TSSM():
        print('in TSSM collage')
    
    def JSPM():
        print('in JSPM collage')
    
    print('in narhe campous')  

    return TSSM

objects = narheCampous()

objects()

print(type(objects))

def outer(x:int, y : int) -> int:

    def inner(a, b):

        print('in inner function')
        return  a + b
    
    print(' in outer function')
    print(x + y)

    return inner;

innerObj = outer(5,8)

print(innerObj)

sum = innerObj(10, 20)


print(sum)




