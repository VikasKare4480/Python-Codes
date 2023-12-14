""""
        Take a input from the user and beteen 1 t0 10 and check wheater the given square of 
        that number is even or odd
"""

num = int(input("Enter number : "))

print(num * num)

if(num * num % 2 == 0):
    print("{} is even".format(num * num))
else:
    print("{} is odd".format(num * num))