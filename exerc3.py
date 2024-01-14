"""
Considere um dado array de inteiros A=[a1,a2, ..., an]. Suponha que exista um índice k tal que o subarray [a1,a2, ..., ak] esteja ordenado em ordem estritamente crescente e o subarray [ak,a2, ..., an] esteja ordenado em ordem estritamente decrescente. Em outras palavras, se 1i<jk então ai<aj, e se ki<jn então ai>aj. Descreva em pseudocódigo um algoritmo de divisão e conquista para determinar o valor de k. Analise o tempo de execução do algoritmo proposto.

"""

#import time

lista = [1, 3, 5, 8, 11, 13, 16, 19, 23, 25, 27, 30, 29, 28, 26, 22, 18, 15, 12, 10]
def findIndex(lista):
    if len(lista) == 0:
        return 0
    
    if len(lista) == 1:
        return lista[0]
    
    mid = len(lista) // 2

    if (mid == len(lista)-1) or ((lista[mid-1] < lista[mid]) and (lista[mid+1] < lista[mid])):
        return lista[mid]
    elif lista[mid+1] > lista[mid]:
        return findIndex(lista[mid:])
    else:
        return findIndex(lista[:mid])

#start = time.perf_counter()
print(lista.index(findIndex(lista)))
#end = time.perf_counter()

#print(f'O tempo de execução foi: {end-start:.6f}')
