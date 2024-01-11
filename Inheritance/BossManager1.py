
class Boss:

    def report(self):
        print("In report : Boss")

class Manager1(Boss):

    def report(self):
        print("In report : Manager1")

class Manager2(Boss):

    def report(self):
        print("In report : Manager2")

class Manager3(Boss):

    def report(self):
        print("In report : Manager3")

class TeamLead1(Manager1, Manager2):
    
    def report(self):
        print('In report : TeamLead')

class TeamLead2(Manager2, Manager3):

    def report(self):
        print('In report : TeamLead2')

class Developer(TeamLead1, TeamLead2):
    def report(self):   
        print('In report : Developer')

dev1 = Developer()
dev1.report()

print(Developer.__mro__)
print(Developer.mro())
