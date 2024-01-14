"""
Escreva um algoritmo de Divisão e Conquista para determinar se todos os elementos em um array
fornecido são iguais. Seu algoritmo deve retornar verdadeiro, se todos os elementos forem iguais, ou
falso, caso contrário.
"""

def todosIguais(lista):

   if len(lista) <= 1:
      return True

   if lista[0] == lista[len(lista)-1]:
      mid = len(lista) // 2
      return todosIguais(lista[:mid]) and todosIguais(lista[mid:])
   else:
      return False

lista = [2,2,2,2,2,2,2,2,2,2]
print(todosIguais(lista))
