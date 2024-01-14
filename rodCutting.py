def rodCut(n):
    if n <= 0:
        return 0
    
    if cache[n] != -1:
        return cache[n]
    
    for i in range(1, n+1):
       for k in range(1, n+1):
            if i>=k:
                cache[i] = max(preco[k] + rodCut(i-k), cache[i])
        
    return cache[n]


preco = [0, 1, 5, 8, 9, 13, 14, 18, 20]
n = 8
cache = [-1] * (n+1)

print(rodCut(n))