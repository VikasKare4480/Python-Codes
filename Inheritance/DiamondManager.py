
class Manager:

    def project(self):
        print("In Project : Manager")

class TeamLead1(Manager):
    pass

class TeamLead2:

    def project(self):
        print('In Project : TeadLead2')

class Develper(TeamLead1, TeamLead2):
    pass

obj = Develper()
obj.project()
