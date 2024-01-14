def Change():
    row = 0
    for i in range(len(V)-1):
        if V[i] <= n:
            row += 1

    mat = [[0 for x in range(n+1)] for y in range(row+1)]

    for i in range(row + 1):
        mat[i][0] = 1

    for j in range(1, n + 1):
        mat[0][j] = 0
            
    for i in range(1,row+1):
        for j in range(1,n+1):
            if j >= V[i-1]:
                mat[i][j] = mat[i-1][j] + mat[i][j-V[i-1]]
            else:
                mat[i][j] = mat[i-1][j]

    print(mat[row][n])
                

V = [1, 2, 5, 8, 10, 100] 
m = 6
n = 15

Change()


