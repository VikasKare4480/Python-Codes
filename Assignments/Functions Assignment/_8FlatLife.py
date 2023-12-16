

class Building:

    buildingMaterial = "Cement"
    noOfFloors = 35
    noOfFlats = 60
    
    def __init__(self, flatName, floorNo, flatType):
        self.flatName = flatName # Mandakini Nivas
        self.floorNo = floorNo # 12
        self.flatType = flatType # 3BHK
    
    def flatInfo(self):
        print('FlatName :', self.flatName)
        print('flat on floor :', self.floorNo)
        print('Building Material :', Building.buildingMaterial)
        print('Flat Type :', self.flatType)


flatName = input("Enter the flat Name : ")
floor = int(input('Enter the floor of the flat : '))
flatType = input('Enter the type of the flat : (2BHK/3BHK) : ')

flat1 = Building(flatName, floor, flatType)
flat1.flatInfo()





