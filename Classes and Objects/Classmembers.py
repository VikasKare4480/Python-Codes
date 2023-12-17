

class Employee:

    compName = 'Google'

    def __init__(self, empId, empName):
        self.empId = empId
        self.empName = empName

    def empInfo(self):
        print(Employee.compName)
        print(self.empId)
        print(self.empName)

emp1 = Employee(10, 'Vikas')
emp2 = Employee(20, 'Ram')

emp1.empInfo()
emp2.empInfo()


