

def isDivisibleByFive(num:int):

    if(num % 5 == 0):

        print("{} is divisible by five".format(num))
    else:

        print("{} is not divisible by 5".format(num))

num = int(input("Enter numbre : "))

isDivisibleByFive(num);