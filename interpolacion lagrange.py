from random import randint

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
    
    def mostrar(self): #Impresion de pares ordenados (x,f(x))
        print("")
        print("-----------VALORES-----------")
        print("       x             f(x)     ")
        for i in range(len(self.valores_x)):
            print("{:^15}{:^15}".format(self.valores_x[i],self.valores_y[i]))            

def main():
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

    interpolador.mostrar() #Se imprimen los pares ordenados

    valor = randint(0,10) #Se selecciona un valor al azar para evaluarlo en la Interpolacion de Lagrange
    print("\nValor a interpolar: ",valor) 
    resultado = interpolador.interpolacion_lagrange(valor) #Resultado de la evaluacion
    print("")
    print("Resultado de la interpolacion: ",resultado)
main()