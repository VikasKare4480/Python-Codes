
num = int(input("Enter number : "))

def factorial(num:int):

    fact = 1;

    for i in range(1, num + 1):

        fact *= i;

    return fact;


fact = factorial(num)

print('Factorial of {} is : {}'.format(num, fact))

print(type(fact))

factorial = factorial("Vikas")