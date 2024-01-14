
class Human:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def info(self):
        print("Name :", self.name)
        print("Age :", self.age)

name = input("Enter your name : ")
age = int(input("Enter age : "))

if __name__ == '__main__':

    human1 = Human(name, age)
    human1.info()

    
