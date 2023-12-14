

num = int(input("Enter number to reverse : "))

reversed = 0

while(num != 0):
    reversed = reversed * 10 + num % 10
    num //= 10

print("reversed number : {}".format(reversed))