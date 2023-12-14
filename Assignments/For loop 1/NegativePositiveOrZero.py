


def checking(num):

    if(num > 0):
        print("{} is grater than zero".format(num))
    elif(num < 0):
        print("{} is less than zero ".format(num))
    else:
        print("{} is equal to zero".format(num))

num = int(input("Enter number : "))

checking(num)
