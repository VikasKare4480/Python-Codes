

def evenOddChecking(num:int):


    if(num == 0):
        print("{} is zero ".format(num))

    elif(num % 2 == 0):
        print("{} is Even".format(num))

    else : 
        print("{} is Odd".format(num))

num = int(input("Enter number : "))

evenOddChecking(num)
