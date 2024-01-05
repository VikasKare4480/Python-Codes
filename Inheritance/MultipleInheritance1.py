
class A:
    
    def fun(self):
        print('In A fun')
    
class B:

    def fun(self):
        print('In fun B')

class C:

    def fun(self):
        print('In fun C')

class D(A, B):

    def fun(self):  
        print('In fun D')
        super().fun()

class E(B, C):
    
    def fun(self):
        print('In fun E')
        super().fun()

class F(D, C):

    def fun(self):
        print('In fun F')
        super().fun()

obj = F()
obj.fun()
