import numpy as np
import random 
class SistemaEcuaciones():
    #Creacion de la clase, que sus atributo sera la Matriz de coeficientes de las incognitas,
    # el Vector de los coeficientes independientes y el Determinante de la matriz y un ultimo atributo que sera el
    # Vector x donde estaran todas las variables que son solucion del sistema de ecuaciones
    
    __N = random.randint(3, 3)
    # Tamaño de la matriz y del vector de coeficientes independientes
    
    def __init__(self): # Inizialicacion de los atributos
        self.__Ax= np.random.randint(1, 4, (self.__N, self.__N))
        self.__B = np.random.randint(1, 4, (self.__N))
        self.__det = np.linalg.det(self.__Ax)
        self.__x= np.zeros(len(self.__B))
        self.__Verificacion__()
        self.__Solucion__()

    def __Verificacion__(self):
        while self.__det == 0:
            self.__Ax= np.random.randint(1, 4, (self.__N, self.__N))
            self.__B = np.random.randint(1, 4, (self.__N))
            self.__det = np.linalg.det(self.__Ax)
            self.__x= np.zeros(len(self.__B))
    
    def __Solucion__(self):
        #Funcion para encontrar la soluciones del sistema usando la regla de cramer
        # y almacenadolas en el Vector `x`
        for i in range(len(self.__B)):
            Ai = self.__Ax.copy()
            Ai.T[i] = self.__B
            Di= np.linalg.det(Ai)
            self.__x[i] = Di/self.__det

    def Mostrar(self):
        #Metodo que primero muestra la Matriz de coeficientes de las incognitas, luego muestra el Vector de coeficientes
        # independientes y por ultimo muestra el vector de todas las variables que son soluciones del sistema de ecuacionesS
        print("== Matriz de coeficientes de las incognitas ===")
        print(self.__Ax)
        print()
        print("++ Vector de valores independientes ++")
        print(self.__B)
        print()
        print("-- Vector de todas las soluciones del sistema --")
        print(self.__x)

def MostrarMetodoCramer():
    Solucion = SistemaEcuaciones()
    Solucion.Mostrar()

