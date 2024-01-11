
class Data(object):
    pass

# print(dir(object))
print(Data.__mro__)
obj = Data()
print(Data.mro())
print(dir(obj))

