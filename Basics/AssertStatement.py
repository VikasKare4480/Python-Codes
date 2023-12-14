

name = input("Enter Your Name : ")

age = int(input("Enter Your Age : "))

assert age > 0, "Ege Must be grater than 0"

if(age >= 18):
    print("{} is eligible to vote".format(name))
else: 
    print("{} is not eligible to vote".format(name))
