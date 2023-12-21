
class Employee(object):

    compName = 'Google'

    def __new__(self):
        print('this is new method : ')
        return super().__new__(self)

    def __init__(self):
        self.empId = empId
        self.empName = empName

    def empInfo(self):
        print(Employee.compName)
        print(self.empId)
        print(self.empName)

empId = int(input('Enter the empId : '))
empName = input('Enter the empName : ')

emp1 = Employee()

emp1.empInfo()
