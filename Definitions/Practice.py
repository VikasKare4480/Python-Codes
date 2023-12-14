def Flat():
    def Room(fan):
        print('in Room')
        print(fan)

    def Kitchen(items):
        print('in Kitchen')
        print(items)

    Room("Fan")
    return KeyError

    print('in flat but not in Room and Kitchen')  # This line is after the return statement

result = Flat()
print("Result:", result)
