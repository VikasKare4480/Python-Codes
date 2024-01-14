
def outer(flag):


    def inner():

        return "This is True." if flag else "This is False."

    return inner

if __name__ == '__main__':

    true_func = outer(True)  # This is True
    fasle_func = outer(False) # This is False

print(true_func())
print(fasle_func())





    

