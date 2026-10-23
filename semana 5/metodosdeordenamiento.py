###Clase 8: Busqueda secuencial y binaria
#Busqueda secuencial:
from heapq import merge


def busquedaSecuencial(secuencia, elemento):
    for i in range (len(secuencia)):
        if elemento == secuencia[i]:
            return i
    return -1

#Busqueda binaria:
def busquedaBinaria(secuencia, elemento):
    izq = 0
    der = len(secuencia) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if secuencia[medio] == elemento:
            return medio
        elif secuencia[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
###Clase 9: Ordenamiento
#Metodo de ordenamiento por seleccion:
def ordenar_seleccion(L):
    for i in range(len(L) - 1):
        p = buscar_minimo(L, i, len(L) - 1)
        L[p], L[i] = L[i], L[p]

def buscar_minimo(L, desde, hasta):
    '''
    Busca el minimo en L[desde]..L[hasta] inclusive.
    '''
    min = L[desde]
    p = desde
    for i in range(desde + 1, hasta + 1):
        if L[i] < min:
            min = L[i]
            p = i
    return p 

#Metodo de ordenamiento por insercion:
def ord_insercion(L):
    """Ordena una lista de elementos según el método de
    inserción.
    Pre: los elementos de la lista deben ser comparables.
    Post: la lista está ordenada.
    """
    for i in range(1, len(L)):
        insertar_ordenado(L, i)

def insertar_ordenado(L, i):
    """
    Pre: L[:i] está ordenada
    Post: L[:i+1] está ordenada y contiene los mismos
    elementos que estaban en L[:i] más el elemento que
    estaba en i.
    """
    v = L[i]
    j = i -1
    while j >= 0 and L[j] > v:
        v = L[j]
        j -= 1
    L[j + 1] = v

#Metodo de ordenamiento merge sort:
def mergesort(L):
    if len(L) < 2:
        return L
    med = len(L) // 2
    izq = mergesort(L[:med])
    der = mergesort(L[med:])
    return merge(izq, der)

def merge(L1, L2):
    i, j = 0, 0
    R = []
    while i < len(L1) and j < len(L2):
        if L1[i] < L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
    j += 1
    R += L1[i:]
    R += L2[j:]
    return R

#Metodo de ordenamiento quick sort:
def quicksort(L):
    if len(L) < 2:
        return L
    menores, med, mayores = particionar(L)
    return quicksort(menores) + [med] + quicksort(mayores)

def particionar(L):
    pivote = L[0]
    menores = []
    mayores = []
    for i in range(1, len(L)):
        if L[i] < pivote:
            menores.append(L[i])
        else:
            mayores.append(L[i])
    return menores, pivote, mayores