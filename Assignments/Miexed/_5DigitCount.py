
def mainOuter():

    def countDigits(num):

        digits = 0

        while(num > 0):
            digits += 1
            num //= 10
        
        return digits

    def evenDigits(num):

        evenDigits = 0

        while(num > 0):

            if(num % 10 % 2 == 0):
                evenDigits += 1
            num //= 10

        return evenDigits

    def oddDigits(num):

        oddDigits = 0

        while(num > 0):

            if((num % 10) % 2 != 0):
                oddDigits += 1

            num //= 10

        return oddDigits

    return countDigits, evenDigits, oddDigits

countDigits, evenDigits, oddDigits = mainOuter()

num = int(input('Enter the number : '))

print('Digits in {} are :'.format(num), countDigits(num))

print('Even Digits Count in {} are :'.format(num), evenDigits(num))

print('Odd Digits Count : {}  are :'.format(num), oddDigits(num))

listOfCount = [countDigits(num),evenDigits(num), oddDigits(num)]

print(listOfCount)

