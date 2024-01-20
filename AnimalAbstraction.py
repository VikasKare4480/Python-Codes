from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    @abstractmethod
    def animalInfo(self):
        print("Name : ", self.name)
        print("Age : " , self.age)
        print("Weight : ", self.weight)

class Dog(Animal):

    def __init__(self, name, age, weight, breed):
        super().__init__(name, age, weight)
        self.breed = breed

    def animalInfo(self):
        super().animalInfo()
        print("Breed : ", self.breed)


myDog = Dog("Rocky", 10, 20, "Vodafone")
myDog.animalInfo()




    