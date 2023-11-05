

def outer():    

    # inner()
    def inner():
        print('In inner fuction')
   
    # inner()
    print('In outer fuction')
    return inner

outerObj = outer()

print(type(outerObj))
# outerObj()


def game():
    
    def inner1():
        print('in inner 1')
    
    def inner2():
        print('in inner 2')

    return inner1, inner2

gameTuple = game()

for i in gameTuple:
    i()
    

def multiply(*vargs):

    mult = 1
    for i in vargs:
        mult *= i

    return mult

print(multiply(1, 2, 3))

