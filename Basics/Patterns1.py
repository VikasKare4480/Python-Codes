

for i in range(3):

    for j in range(3):
        print("* ", end="")


print()

num = 1
for i in range(3):

    for j in range(3):
        print(num, end=" ")

    print()
    num += 1


print()

for i in range(3):

    num = 1
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

