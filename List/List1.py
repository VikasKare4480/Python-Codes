
#  List Using dictinary

players = [{18 : "Virat", 10 : "Sachin"}, {45 : "Rohit"}, { 77 : "Shubman"}]
print(players)
print(type(players)) # <class 'list'>
print(players[0][18]) # Virat 


# List using set
newPlayers = [{100, "Ashish", 10.10}, {200, "Kanha", 30.20}, {300, "Rahul", 12.09}]
print(newPlayers)

# List using tuple

batsmans = [("Rohit", "Vitat", "Dhoni"), ("Ashis", "Mahi", "Shubhman")]
print(batsmans)
print(type(batsmans))

# Using the constructor of the list class

tuple = tuple((10, 20, 30))
listwituTuple = list(tuple)
print(" listwituTuple : ", listwituTuple)

dict = dict({18 : "Virat", 10 : "Sachin"})
print(dict)

numberList = list([10, 20, 30]) 
print(numberList)

# Comprehenssion Type

normalList = [num for num in range(0, 10)]
print(normalList)
print(type(normalList))

# create a list of squares upto the 100

squaresList = list([num * num for num in range(1, 101)]) 
print(squaresList)

# adding condition to the comprehension list 

# lsit of only even numbers upto 200

evenNumbers = list([num for num in range(1, 201) if (num % 2 == 0) and (num % 5 == 0)])

print(evenNumbers)








