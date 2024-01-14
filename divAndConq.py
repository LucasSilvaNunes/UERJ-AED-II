def contarUm(lista, start, end):
    mid = int((end + start)/2)
    if len(lista) <= 1:
        return 0
    else:
        if lista[mid] == 1:
            cont += mid - start
            start = mid
            return contarUm(lista, start+1, end)
        else:
            end = mid
            return contarUm(lista, start, end-1)
        



lista = '1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0'.split()
lista = [int(x) for x in lista]
cont = 0


print(contarUm(lista, 0, len(lista)-1))

#print(lista)

"""
Considere um vetor no qual existe uma sequência de bits ('0's e '1's), onde todos os bits '1's aparecem antes dos bits '0's. Descreva um algoritmo em pseudocódigo, usando o paradigma Divisão e Conquista, que mostre como saída o número de "1"s existentes na sequência com a característica anterior recebida como entrada. Proponha uma implementação (em Python, C ou C++) para o seu algoritmo e apresente aqui o código-fonte e o print da saída produzida por sua implementação para a entrada composta pela seguinte sequência de bits: 1111111111100000000.
"""