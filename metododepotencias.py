import numpy as np
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
