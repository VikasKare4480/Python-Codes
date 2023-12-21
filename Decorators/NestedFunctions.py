
def outer() :

    print("In Outer")

    def inner1():
        print("In Inner 1")
    
    def inner2():
        print("In inner 2")

    return inner1, inner2

inner1, inner2 = outer()

print('Inner 1 call')
inner1()

print('Inner 2 call')
inner2()

print("Inner1 type : {}".format(str(type(inner1)).isalpha()))

