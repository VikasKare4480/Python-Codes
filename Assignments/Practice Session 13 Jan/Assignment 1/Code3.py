
import array as arr

list = arr.array('i', [1,2,3,4,5])

# list = [1,2,3,4,5]
print(list)

listOfFact = []

def factorial(funList):
    
    for i in funList:
        print(i)

        fact = 1

        for j in range(1, i + 1):
            fact *= j; 
     
        listOfFact.append(fact)

factorial(list)

print(listOfFact)

            
    
