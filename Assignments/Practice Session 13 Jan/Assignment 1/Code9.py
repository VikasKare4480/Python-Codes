

class IPL:

    oraganzer = "BCCI"

    def __init__(self, totalTeams, totalGrounds, totalPlayers):
        self.totalTeams = totalTeams
        self.totalGrounds = totalGrounds    
        self.totalPlayers = totalPlayers

    def IPLInfo(self):

        print("Total Teams : ", self.totalTeams)
        print("Total Grounds : ", self.totalGrounds)
        print("Total Players : ", self.totalPlayers)
    
obj = IPL(12, 10, 144)
obj.IPLInfo()


