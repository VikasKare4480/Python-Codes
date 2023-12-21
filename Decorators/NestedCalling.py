
def gun():
    print('In gun')

def fun(x):
    x()
    print('In fun')

fun(gun)
