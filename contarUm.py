lista = '1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0'.split()
lista = [int(x) for x in lista]

def contarUm(lista, inicio, fim):
    if inicio >= fim:
        return lista[inicio]
    
    else:
        meio = (inicio + fim) // 2
        if lista[meio] == 0:
            return contarUm(lista, inicio, meio-1)
        else: #meio da lista é 1.
            return (meio - inicio + 1) + contarUm(lista, meio+1, fim)
    

print(contarUm(lista,0, len(lista)-1))