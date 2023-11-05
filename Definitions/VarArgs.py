


def arArgs(*args):

    print(args)
    print(type(args))

arArgs(10,20,30)

def fun(num1, num2, *man):
    print(num1)
    print(num2)
    print(man)

fun(10, 20) # 10 20 ()
fun(11, 12, 13) # 11 12 (13,)
fun(10, 20, 90, 20, 230) # 10 20 (30---230)


def fun(num, sum, *args):
    print(num + sum)
    print(args)

fun(10, 20, 30)


def done(*args, num1, num2): #TypeError: done() missing 2 required keyword-only arguments: 'num1' and 'num2'

    print(num1)
    print(num2)
    print(args)

done(10, 20, 30, 40)
