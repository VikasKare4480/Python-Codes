
numbers = [10, 20, 30]

def mainOuter():

    def myIndex(list, taget):

        index = -1

        for i in range(len(list)):

            if(list[i] == taget):
                index = i;
        
        return index
    
    def isPalindrome(num):

        numCopy = num
        reversed = 0

        while(numCopy > 0):

            reversed = reversed * 10 + (numCopy % 10)
            numCopy //= 10

        print(reversed)

        return reversed == num
    
    return myIndex, isPalindrome

    
target = int(input('Ente the taget : '))

myIndex, isPalindrome = mainOuter()

index = myIndex(numbers, target)

print("Elemet found at index : {}".format(index))

num = int(input('Enter the number to check palindrome : '))


if(isPalindrome(num)):
    print(num , "is palindrome")
else:
    print(num , "is not a palindrome")


