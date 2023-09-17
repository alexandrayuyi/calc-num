from random import randint
import random
import numpy as np

#INICIA LAGRANGE
class Lagrange: #Clase Principal
    def __init__(self): #Constructor de los pares ordenados (x,f(x))
        self.valores_x = []
        self.valores_y = []

    def agregar_punto(self, x, y): #Metodo para añadir puntos
        self.valores_x.append(x)
        self.valores_y.append(y)     

    def interpolacion_lagrange(self, interpolador): #Resolucion de la Interpolacion de Lagrange dando valores a f(x) o y
        resultado = 0.0 #Valor a retornar
        vector_l = [] #Vector usado para multiplicar el resultado de un termino de lagrange por su termino f(x)
        repeticiones = len(self.valores_x) #Para determinar la cantidad de sumas y productos
        for i in range(repeticiones):
            L = 1
            for j in range(repeticiones):
                if j != i: #Condicion para que no haya divison entre 0
                    L *= (interpolador - self.valores_x[j])/(self.valores_x[i] - self.valores_x[j]) #Calculo de productorio
                else:
                    continue
            vector_l.append(L)
        
        for i in range(repeticiones):
            producto = self.valores_y[i] * vector_l[i] #Valores de f(x) * Valores de Lagrange
            resultado += producto #Sumatoria de terminos de Lagrange
        return resultado
    
    def mostrarPares(self): #Retorna el vector de valores de X
        Par = "       x             f(x)" + "\n"
        for i in range(len(self.valores_x)):
            Par = Par + str("{:^15}{:^15} \n".format(self.valores_x[i],self.valores_y[i]))
        return str(Par)
    
    #TERMINA LAGRANGE

#INICIA CRAMER
class SistemaEcuaciones():
    #Creacion de la clase, que sus atributo sera la Matriz de coeficientes de las incognitas,
    # el Vector de los coeficientes independientes y el Determinante de la matriz y un ultimo atributo que sera el
    # Vector x donde estaran todas las variables que son solucion del sistema de ecuaciones
    
    __N = random.randint(2, 8)
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
    
    def MostrarMatriz(self):
        #Metodo que muestra la Matriz de coeficientes de las incognitas
        return str(self.__Ax)
        
    
    def MostrarVectorIndependiente(self):
        #Metodo que muestra el Vector de coeficientes independientes
        return str(self.__B)
    
    def MostrarSoluciones(self):
        #Metodo que muestra el vector de todas las variables que son soluciones del sistema de ecuacionesS
        return str(self.__x)

#TERMINA CRAMER


#INICIA POTENCIAS
def Potencias(matriz,vector,it):
    """
    La función `Potencias` calcula el método de potencia para encontrar el los autovalores y
    los autovectores de una matriz dada.

    :param matriz: Una matriz cuadrada (matriz 2D) de tamaño n x n, donde n es el número de filas/columnas en
    la matriz
    :param vector: el parámetro vector representa una lista o matriz de números. es el vector inicial
    que se multiplicará por la matriz en cada iteración
    :param it: El parámetro "it" representa el número de iteraciones a realizar en el método de potencia.
    algoritmo
    return: `lambda_list` representa la lista de autovalores y `list_vector` represeta la lista de autovectores
    """
    #Inicialización de variables
    # de la función 
    Av = vector     #Variable que almacena el vector inicial
    a = []          #Lista que almacena los vector resultantes de la multiplicacion entre el `Av` y la `matriz`
    lambda_list = []    #Lista que almacena los autovalores que retornara la función
    list_vector=[]      #Lista que almacena los autovectore que retornara la función
    x = 0        #Variable bandera

    #Ciclo `for` que se repetira tantas veces se quiere 
    # para que los autovalore y autovectores den resultados mas cercanos 
    # a el valor maximo de la matriz y tambien el vector maximo del mismo
    for i in range(it):
        
        #Se almacena la en `Av` la multiplicacion entre `Av` y la matriz
        # esta multiplicacion sera usada despues para encontrar tanto el autvector
        # como el auto valor
        Av = np.dot(matriz, Av)

        #Almacenamos los resultados de `Av` en la lista `a` para determinar 
        # de manera mas sencilla los autovectore y autovalores
        a.append(Av)   

        #Condicion para no generar error ya que necesitaremos que 
        # la lista `a` tenga al menos dos resultados de `Av`
        if i > 0:
            lambda_list.append(np.max(a[x+1]/np.max(a[x])) )  #Determinamos los autovalores y almacenamos en la lista `lambda_list`
            x+=1   
        else:
            lambda_list.append(np.max(a[i]))    #Determinamos el primer autovalor y lo almacenamos en la lista `lambda_list`
        
        list_vector.append(a[i]/np.max(a[i])) #Determinamos los autovectores y los almacenamos en `list_vector`

    return lambda_list, list_vector

def matriz_random(filas, columnas, minimo, maximo):
  matriz = []
  for fila in range(filas):
    fila_aleatoria = []
    for columna in range(columnas):
      fila_aleatoria.append(random.randint(minimo, maximo))
    matriz.append(fila_aleatoria)
  return matriz

def vector_random(n, min, max):
  vector = []
  for i in range(n):
    vector.append(random.randint(min, max))
  return vector

def imprimir(matriz):
    for fila in matriz:
        fila_formateada = ' '.join(str(elemento) for elemento in fila)
        print(fila_formateada)

#TERMINA

def MostrarPotencias():
    #MOSTRAR METODO DE POTENCIAS
    matriz = matriz_random(3,3,3,100)
    A = np.array(matriz)

    vector = vector_random(3,1,100)

    v = np.array(vector)
    a, b = Potencias(A,v,5)
    h = []
    for i in range(len(b)):
        h.append(str(b[i]))
    return str(matriz), str(vector), str(a), str(h)
def MostrarInterpolacion():

    interpolador = Lagrange() #Se ctrea un objeto de la clase Lagrange()
    n = randint(1,5) #Se trabajar como maximo con 5 pares
    for i in range(n):

        numero_aleatorio_x = randint(-5,5)
        while numero_aleatorio_x in interpolador.valores_x:
            numero_aleatorio_x = randint(-5,5)

        numero_aleatorio_y = randint(-5,5)
        while numero_aleatorio_y in interpolador.valores_y:
            numero_aleatorio_y = randint(-5,5)
        
        interpolador.agregar_punto(numero_aleatorio_x,numero_aleatorio_y) #Se agregan los terminos (x,f(x)) a su respectivo vector

    valor = randint(0,10) #Se selecciona un valor al azar para evaluarlo en la Interpolacion de Lagrange
    resultado = interpolador.interpolacion_lagrange(valor) #Resultado de la evaluacion
    return interpolador.mostrarPares(),str(valor), str(resultado)

def MostrarCramer():
    #MOSTRAR CRAMER
    Solucion = SistemaEcuaciones()
    return Solucion.MostrarMatriz(), Solucion.MostrarSoluciones(), Solucion.MostrarVectorIndependiente()
