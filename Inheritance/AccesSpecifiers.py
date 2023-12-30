

# public private protected

class AccesSpecifiers:

    z = 10 # public by default

    def __init__(self):
        self._x = 20 # _ -> protected
        self.__y = 30 # __ -> private

        print('In cons')
    
    # def __del__asf(self):
    #     print('In del')


print(dir(AccesSpecifiers))

print(AccesSpecifiers.z) # z is public accessed from anywhere

obj = AccesSpecifiers()

print(obj._x)  # _x is protected accessed from base class and here also

print(obj._AccesSpecifiers__y)

print(dir(AccesSpecifiers))

print(dir(obj))










