
str1 = input('Enter large 1 : ')
str2 = input('Enter small 2 : ')

# if str2 in str1:
#     print('{} is the substring of {} '.format(str2, str1))
# else:
#     print('not a substring')

if str1.find(str2) != -1:
    print('is substring')

for i in str1:
    
    count = 0
    for j in str2:

        if(i == j):
            count += 1
        else:
            break

    if(count == len(str2)):
        print('Is substring')
        break



