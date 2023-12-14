

"""
    multiple values are returned as a pyhon tuple

"""


def addByTen(a, b, c = 10):
    return a + 10, b + 10, c + 10


a = int(input('enter a : '))
b = int(input('enter b : '))
c = int(input('Enter c : '))
print(a)
print(b)
print(c)

returned = addByTen(a, b, c)

a, b, c = addByTen(a,b,c)
print(a)
print(b)
print(c)

print(type(returned)) # <class 'tuple'>

print(returned)

for i in returned:
    print(i, end=" ")

print() 

new = addByTen(100, 200)

for i in new:
    print(i)