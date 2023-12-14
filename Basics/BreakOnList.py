
PlayerList = ["Rohit", 'Virat', 'Shreyash', 'Bumrah']



playerName = input("Enter Player : ")

for player in PlayerList:

    if(player == playerName):
        print("{} is present in List of Players".format(playerName))
        break;

else:
    print("{} is not present in the List of players".format(playerName))


# with boolean flag

present = False


for player in PlayerList:

    if(player == playerName):
        print("{} is present in the List ".format(player))
        present = True


print(present)
if(present == False):
    print("{} is not present in the List of players".format(playerName))
    
