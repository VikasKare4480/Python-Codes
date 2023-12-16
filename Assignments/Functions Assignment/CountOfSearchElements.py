
def countOfSearchElement(list, target):

    count = 0

    for num in list:

        if(num == target):
            count += 1

    return count

length = int(input("Enter the size of the list : "))



list = []

for i in range(0, length):

    list.append(int(input("Enter the {} element : ".format(i+1))))

target = int(input("Enter the taget to Find : "))

count = 0

if(countOfSearchElement(list, target) == 0):

    print("Element is not present at all in the list")

else:

    print("count of {}  : {}".format(target, countOfSearchElement(list, target)))

    



