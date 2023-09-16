import numpy as np

def potencias(matriz,vector,it):
    Av = vector
    a = []
    lambda_list = []
    list_vector=[]
    x = 0
    for i in range(it):
        Av = np.dot(matriz, Av)
        a.append(Av)
        if i > 0:
            lambda_max = np.max(a[x+1]/np.max(a[x]))
            lambda_list.append(lambda_max)
            x+=1
        else:
            lambda_max = np.max(a[i])
            lambda_list.append(lambda_max)
        
        list_vector.append(a[i]/np.max(a[i]))

    return lambda_list, list_vector
