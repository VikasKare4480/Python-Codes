
import array as arr

def factorailArray(array):

    factArray = arr.array('i', [])
    for num in array:
        fact = factorial(num)
        factArray.append(fact)
    return factArray

def factorial(num):
    
    fact = 1
    for i in range(1, num + 1):
        fact *= i

    return fact
    

array = arr.array('i', [5,12,3,4,6,7,9])
print(array)

finalArray = factorailArray(array)

print(finalArray)