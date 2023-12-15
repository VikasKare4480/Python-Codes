
players = list(["Rohit", "Virat", "Shubhman", "Shreyash", "KLRahul"])
print(players)

# appent(object)

players.append("MSDhoni")
print(players)

# extend(iterable)
addPlayers = ["Player1", "Player2"]

players.extend(["Vikas", "Laxman", "Kare"])
players.extend(addPlayers)
print(players)

# insert(index, object)

players.insert(0, 10)

print(players)
print(len(players))

# remove()

players.remove("Kare") # if the object is not presetn then the ValueErron will be given

print(players)

# pop() 

print(players.pop())
print(players)

# clear() # removes all the objects from the list 

# print(players.clear())

print(players)

# coutn(objcet) -- no of the objects in the list 

print(players.count("MSDhoni"))

# index(object) -->> index of specified object if found else ValueError 

print(players.index("Vikas"))

# revese() -->> reverses the list

players.reverse()
print(players)
players.reverse();


# sort() 
players.remove(10)
players.sort() 
print(players)


# copy() 

newList = players.copy()

print("newList : ",  newList)
print(players)

