

class Employee(object):

    def __new__(self):
        return super().__new__(self)
    
    def __init__(self):
        self.empId = 10
        self.empName = 'Rahul'

    
    def empInfo(self):
        print('In static method')
        print('self : {}',format(self))


    @classmethod
    def classMethod(cls):
        print('in class method')
        print('cls : {}'.format(cls))

    def staticmethod():
        print('in static method')
        

emp1 = Employee()
emp1.empInfo()
emp1.classMethod()

