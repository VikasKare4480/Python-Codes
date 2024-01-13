

def outer():

    def digitCount(num):
        count = 0
        # print(num)
        while(num > 0):
            count += 1
            num //= 10
        
        # print(count)
        return count


    def evenCount(num):
        eCount = 0

        while(num > 0):

            if(num % 2 == 0):
                eCount += 1

            num //= 10

        return eCount


    def oddDigitCount(num):

        oCount = 0
        while(num > 0):

            if(num % 2 == 1):
                oCount += 1

            num //= 10
        
        return oCount

    return digitCount, evenCount, oddDigitCount

num = int(input("Enter the number : "))

digitCount, evenCount, oddCount = outer()

print("Digit Count : ", digitCount(num))

print("Odd Count : ", oddCount(num))

print("Even Count : ", evenCount(num))



