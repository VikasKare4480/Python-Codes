
from abc import *


class Demo(ABC):

    def __init__(self):
        print('This is abstract Demo Cons')

    @abstractmethod
    def info(self):
        print('This is instance of the class')
    
    @classmethod
    def classWali(self):
        print('This is class wali')

class DemoChild(Demo):

    def __init__(self):
        print('This is Demochild Cons')

    def info(self):
        super().info()
        # print('Demochild overrided')

obj = DemoChild()
obj.info()
