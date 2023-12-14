
print('sum of all the angles of triagle must be 360')

angle1 = int(input('Enter angle 1 : '))
angle2 = int(input('Enter angle 2 : '))
angle3 = int(input('Enter angle 3 : '))


if(angle1 == 90 or angle2 == 90 or angle3 == 90):
    print("is right angle triangle")
else:
    print('is not a right angle triangle')