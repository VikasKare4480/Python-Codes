
list = [1,2,3,4,4,5,3]

print(list)

taget = int(input("Enter the taget : "))

count = 0

for i in list:

    if(taget == i):
        
        count += 1

print("Count of {} is : ".format(taget), count)