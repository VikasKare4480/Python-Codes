import copy as cp

lang = ["Java", "Cpp", "Python", ["Rust", "Ruby", "Perl", "Dart"]]

print(lang); # prints the whole list 

print(lang[0]); # Java

print(lang[3][0]) # Rust

# creating the copy of the lang

copy = lang.copy()

print(" copy : ", copy)

lang[3][1] = "JavaScript"


# Shallow Copy
print(lang)
print(copy)

# copy as well as the original list is chaning it is like the array having the same addresses 

print(id(lang) == id(copy))


# deep copy

players = ["Shubman", "Shreyash", "Rohit"]

print(players)

playersCopy = players.copy()

print(playersCopy)

# Change 

players[1] = "SKY"

print(players) # changed in the players but not in the playersCopy

print(playersCopy) 


games = ["Cricket", "Football", "Vollyball", "Baseball", "Kabdaddi"]

print(games)

gamesCopy = cp.deepcopy(games)

print(gamesCopy)

# chaning the Vollyball to the Karate

games[2] = "Karate"

print(games) # Changed
print(gamesCopy) # not changed
