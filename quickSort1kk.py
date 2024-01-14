from datetime import datetime

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)
    
    
file = open('entrada1kk.txt', 'r')
read = file.read()
conteudo = read.replace(',','')
conteudo = conteudo.replace('\n','')
arr = conteudo.split()
arr = list(map(int,arr))
file.close()

start = datetime.now()
sorted_list = quicksort(arr)
end = datetime.now()

print(sorted_list)
print("\n Tempo de QuickSort (1kk elementos): {}".format(end-start))

