

def add(x): # 3

    def inner(y): # 7

        return x * y; # 21 

    return inner

if __name__ == '__main__':
    add_3 = add(3)
    result = add_3(7)
    print(result) # 21
    
