

class IPL:

   
    teamName = "MumbaiIndians"
    captain= "The GOAT Rohit Sharma"

    def __new__(self):
        # print('In new method')
        return super().__new__(self)

    def __init__(self):
        # print('in Contructor IPL')
        self.sponsor = "Reliance Digital"
        self.budget = 120.00
        self.trofiesWon = 5

    def teamInfo(self):
        print("Captain : {}".format(IPL.captain))
        print("Sponsor : {}".format(self.sponsor))
        print("Budget : {}".format(self.budget))
        print("Trifies Won under Rohit :", self.trofiesWon)


team1 = IPL()
team1.teamInfo()





