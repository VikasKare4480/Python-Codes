

class Myclass:

    print('Myclass Start')

    def __init__(self):
        print('In Constructor')

    def __del__(self):
        print('In del')

    print('Myclass End')

    __x = 10 #  _Myclass__x
    print(_Myclass__x)

# print(type(id(Myclass)))
# print(type(object))
print('Start Code')

Myclass()  

print('End Code')
print(dir(Myclass))
print(Myclass._Myclass__x)



