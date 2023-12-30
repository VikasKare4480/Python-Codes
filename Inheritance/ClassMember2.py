
class Myclass:

    def __init__(self):
        print('In Init')
    
    def __del__(self):
        print('In del')

print(dir(Myclass))

print('Start Code')
obj1 = Myclass()
obj2 = Myclass()

obj3 = obj1

del obj1
print('end code')

