

def fun(**args):

    print();
    print(args)
    print(type(args))

    for key, value in args.items():
        print(key , " : ", value)


fun(x = 10, y = 20, z = 30)


def function(**kwargs):
    # print(x/)
    # print(y)
    print(type(kwargs))

    for key, value in kwargs.items():
        print(key, " : ", value)


function(x = 20, y = 10, w = 30)