
class Sum:

    def mysum(self, num1, num2):

        return num1 + num2
    

obj1 = Sum()

num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))

sum1 = obj1.mysum(num1, num2)

obj2 = Sum()

num1 = int(input('Enter num1 : '))
num2 = int(input('Enter num2 : '))

sum2 = obj1.mysum(num1, num2)

if((sum1 + sum2) % 2 == 0):
    
    print('Sum is Even {}'.format(sum1 + sum2))
else:
    print('sum is Odd : {}'.format(sum1 + sum2))






