

class Parent:

    def __init__(self):
        print('In Constructor')

    def __del__(self):
        print('In Destructor')

obj = Parent()
obj = Parent()
print("End of Code")

