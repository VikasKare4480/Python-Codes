
class Boss:

    def report(self):
        print('In report : Boss')

class Manager(Boss):

    def report(self):
        print('In report : Child')

class TeadLead(Manager):

    def report(self):
        print('In report : TeamLead')

class Developer(TeadLead):

    def report(self):
        print("In report : Devloper")

dev1 = Developer()
dev1.report()

print(Developer.__mro__)

'''

(<class '__main__.Developer'>, 
<class '__main__.TeadLead'>, 
<class '__main__.Manager'>, 
<class '__main__.Boss'>, 
<class 'object'>)

'''




