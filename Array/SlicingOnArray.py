

import array as arr

arrData = arr.array('i', [10, 20, 30, 40, 50])

for i in arrData:
    print(i, end=" ")

print()

for i in arrData[1:4:1]:
    print(i, end=' ')

print()


#  reverse print array elements

for i in arrData[::-1]:
    print(i, end=' ')


print(arrData[4]) # 50

print(arrData[6]) # IndexError: array index out of range 

