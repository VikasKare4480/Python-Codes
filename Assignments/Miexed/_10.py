
class Life:

    def __new__(self):
        print('In new method')
        return super().__new__(self)
    
    def __init__(self):
        print('In init method')


    @staticmethod
    def staticmethod():
        print('in static method')

    @classmethod
    def classmethod():
        print('In the class method')


vikas = Life()

Life.staticmethod()
vikas.classmethod()
vikas.staticmethod()








