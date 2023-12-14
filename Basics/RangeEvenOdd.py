

x = int(input("Enter X : "))
y = int(input("Enter Y : "))

for i in range(x, y + 1):

    if(i % 2 == 0):
        print("{} is even ".format(i))
    else:
        print("{} is odd ".format(i))

