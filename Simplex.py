import numpy as np
class Simplex:

    def generate_tableau(self):
        self.tableau = np.concatenate((self.coeficientes,np.eye( self.coeficientes.shape[0]),self.b) , axis = 1)
        self.tableau = np.vstack((self.tableau,self.obj))

    def objprocess(self):
        self.obj = np.concatenate((self.obj * (-1), np.zeros( self.coeficientes.shape[0]),np.zeros(1)))

    def __init__(self):
        self.coeficientes = np.array([[1,2,3], [1,2,3], [1,2,3]])
        self.obj = np.array([1 , 2 , 3])
        self.b = np.array([[1] , [2] , [3]])
        self.objprocess()
        self.generate_tableau()

    def scaleline(self, k, line):
        tam = self.coeficientes.shape[1]
        for i in range(tam):
            self.coeficientes[line , i] = self.coeficientes[line , i] * k

    def addrow(self, l1 , l2):
        tam = self.coeficientes.shape[1]
        for i in range(tam):
            self.coeficientes[l2 , i] = self.coeficientes[l2 , i] + self.coeficientes[l1 , i]

    def show(self):
        print(self.tableau)

brabo=Simplex()
brabo.show()
'''
teste = np.array([[1,2,3],[1,2,3]])
print(teste.shape[1])
print(teste)
'''




