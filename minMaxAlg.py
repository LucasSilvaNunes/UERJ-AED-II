def maxMin(lista):
    inicio = 0
    fim = len(lista)-1
    if inicio == fim:                            #Caso base de apenas um elemento no array
        return (lista[fim],lista[inicio])    #maior, menor
    elif inicio == fim-1:                        #Caso base de apenas dois elementos no array
        if lista[fim] > lista[inicio]:
            return (lista[fim], lista[inicio])    #maior, menor
        else:
            return (lista[inicio], lista[fim])    #maior, menor
    else:                                        #Caso geral
        meio = (fim + inicio) // 2    
        max_esq, min_esq = maxMin(lista[:meio])
        max_dir, min_dir = maxMin(lista[meio:])

        if max_esq < max_dir:
            max_esq = max_dir
        if min_esq > min_dir:
            min_esq = min_dir
        return (max_esq, min_esq)
    
lista = [50, 40, -5, -9, 45, 90, 65, 25, 75]
    
max, min = maxMin(lista)

print(max)
print("\n")
print(min)