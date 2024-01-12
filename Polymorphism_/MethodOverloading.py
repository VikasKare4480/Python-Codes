 

def add(x, y = None, z = None):
    print(x + y + z)


# add(10) # TypeError: Unsupported Operator + for 'int' and 'Nonetype'

# add(10, 20) # SameError : Unsupported Operator + for 'int' and 'NoneType'

add(10, 20, 30) # 30


