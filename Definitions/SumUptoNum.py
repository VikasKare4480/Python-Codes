

def sumUptoNumber(num):

    sum = 0;
    
    for i in range(1,num + 1):
        sum += i;

    return sum;

num = int(input("Enter number : "))

sumUptoNum = sumUptoNumber(num); 

print(sumUptoNum)

