# # # Parte 1- Busquedas
#Actividad 1.1 – Búsqueda secuencial
# """Copien la función buscar(secuencia, elemento) de la Clase 8 y respondan por escrito, en comentarios: qué hace cada línea y qué valor devuelve cuando el elemento no está"""
# def buscar(secuencia, elemento):         #1) Recibe una secuencia y un elemento a buscar
#     comparaciones = 0                    #2) Inicializa un contador de comparaciones en 0
#     for i in range(len(secuencia)):      #3) Itera sobre cada índice de la secuencia
#         comparaciones += 1               #4) Incrementa el contador de comparaciones en 1
#         if elemento == secuencia[i]:     #5) Compara el elemento buscado con el elemento en la posición i de la secuencia
#             return i, comparaciones        #6) Devuelve el índice i y el número de comparaciones si encuentra el elemento en la secuencia
#     return -1, comparaciones             #7) Si el elemento buscado no se encuentra en la secuencia, devuelve -1 y el número de comparaciones.

# nombres = ['María', 'Rosa', 'José', 'Carmen', 'Ana', 'Juana']
# x,y = buscar(nombres, input('Ingrese el nombre a buscar: '))
# print(f"El nombre se encuentra en la posición: {x}, el número de comparaciones realizadas fue: {y}")

#Actividad 1.2 – Búsqueda binaria
# def busqueda_binaria(secuencia, elemento):
#     izq = 0
#     der = len(secuencia) - 1
#     comparaciones = 0
#     while izq <= der:
#         medio = (izq + der) // 2
#         if secuencia[medio] == elemento:
#             return medio, comparaciones
#         if secuencia[medio] > elemento:
#             der = medio - 1
#         else:
#             izq = medio + 1
#         comparaciones += 1
#     return -1, comparaciones
# numeros = [1, 3, 5, 7, 9, 11, 13, 15]
# resultado, comparaciones = busqueda_binaria(numeros, int(input('Ingrese el número a buscar: ')))
# print(f"El número se encuentra en la posición: {resultado}, el número de comparaciones realizadas fue: {comparaciones}")

###Parte 2: Ordenamiento
# Actividad 2.1 – Ordenamiento por selección
