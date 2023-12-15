
class Company(object):

    def __new__(self): 
        print("in the new method")
        return super().__new__(self)
    
    def __init__(self):
        print("in the init method")
    
    def disp(self):
        print("in disp method")

    
print("Start")

obj = Company();
obj.disp();

print("End")


# class Demo(object):

#     def __new__(self):
#         print("This is new method and called before the init method")

#     def __init__(self):
#         self.x = 10;
#         self.y = 20;
#         print("thds is init method and called after the new method")

#     def display(self):
#         print("x is : " , self.x)


# demoObj = Demo();
# demoObj.display();



    