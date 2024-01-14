
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



flag = True

while(flag == True):

    print("1.Palindrome Check : \n2. Index Check : ")

    choice = int(input("Enter Choice : "))

    match choice:

        case 1 :

            num = int(input("Enter the input : "))

            if(obj.palindrome(num)):

                print(num, ' is Palindrome')
            else:

                print(num, ' is not palindrome')      
            

        case 2 :

            print(list)

            target = int(input("Enter the target from the list : "))

            index = obj.myIndex(list, target)

            if(index != -1):

                print(target, "present at the index : {}".format(index))

            else:

                print(target, "is not present int the list")

        case _ : # this is default case

            print('Invalid Choice Entered please enter valid index')
            

    str = input('Do you want to continue (Y/y) : ')    

    if(str == 'Y' or str == 'y'): flag = True
    else: flag = False

        