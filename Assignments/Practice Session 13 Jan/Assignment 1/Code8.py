
class Company:

    compName = 'Google'

    def __init__(self, empName, empId):
        self.empId = empId
        self.empName = empName

    def empInfo(self):

        print("Comp Naem: {}".format(self.compName))
        print("EmpName : ", self.empName)
        print("EmpId : ", self.empId)

obj = Company("Prashant", 101)
obj.empInfo()

