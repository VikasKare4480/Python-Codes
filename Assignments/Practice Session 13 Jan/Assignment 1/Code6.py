
class Parent:

    def palindrome(self, num):
        
        numCopy = num
        reversed = 0

        while(num > 0):

            reversed = reversed * 10 + num % 10
            num //= 10

        return numCopy == reversed
    

    def myIndex(self, list, target):
        
        index = 0
        for i in list:

            if(i == target):
                return index
            index += 1
        
        return -1

obj = Parent()

print(obj.palindrome(121))


list = [1,2,3,4,5]

target = 5

index = obj.myIndex(list,target)


if(index != -1):
    print('Element found at {}'.format(index))
else:
    print('Element not found the list')



print("1. isPalindrome \n 2. myIndex")

choice = int(input("Enter Choice : "))


if(choice == 1):

    num = int(input("Enter the input : "))

    if(obj.palindrome(num)):

        print(num, ' is Palindrome')
    else:

        print(num, ' is not palindrome')

elif(choice == 2):

    print(list)

    target = int(input("Enter the target from the list : "))

    index = obj.myIndex(list, target)

    if(index != -1):

        print(target, "present at the index : {}".format(index))

    else:

        print(target, " is not present int the list")
    

        