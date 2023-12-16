
import copy as cp
list = list([10,20,30,40,50,60,70,80,90,100])


#  Deep Copy(works with the non nested scenario) no change in other list 

langList = ["CPP", "Java", "Dart", "Python", "Ruby", "C", "BhaiLang"]
print(langList)

# Ceating the copy of this non nested list which always follows the Deep Copy means no changes

newLangList = langList.copy()
print(newLangList)
print(newLangList[2])
newLangList[2] = "Flutter"
print(newLangList) # Dart -> to flutter changed in newLangList but not in the langList

print(langList)


# Shallow copy 

gamesList = ["Cricket", "Football", "Baseball", "Kabaddi", ["Indian", "American", "German", "Banga", "Chinese"]]
print(gamesList)

newGamesList = gamesList.copy()
print(newGamesList)

gamesList[4][0] = "INDIANS"

print(newGamesList)
  
print(gamesList)

# To resolve this (import the copy as cp)

newGamesList2 = cp.copy(gamesList)

print(newGamesList2)
print(gamesList)

newGamesList2[4][4] = "Japanese"
print(newGamesList2)
print(gamesList)













