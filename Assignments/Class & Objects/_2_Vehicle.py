
class Vehicle:

    def __init__(self, brand, model, year, speed):
        self.brand = brand
        self.speed = speed
        self.model = model
        self.year = year

    def accelerate(self):
        print("In accelerate method")
    
    def honk(self):
        print('In honk method')

    def brake(self):
        print('In brake method')


class GVegan(Vehicle):

    def __init__(self, brand, model, year, speed):
        super().__init__(brand, model, year, speed)
        print('GVagan cons')

    def accelerate(self):
        super().accelerate()
        print('In GVagan acceleration')   
    
    def honk(self):
        print('This is GVagns honk')

myGVegan = GVegan("Mercedes","GVegan", 2015, 150)
myGVegan.accelerate()
myGVegan.honk()
myGVegan.brake()
        


