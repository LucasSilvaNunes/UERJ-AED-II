def Perm(np):
    for i in range(1, n+1):
        if not s[i]:
            P[np] = i
            s[i] = True
            if np == n:
                if P[2] == 6 and P[4] == 4:
                    print(P[1:])
            else:
                Perm(np + 1)
            s[i] = False

n = 8
P = [-1] * (n + 1)
s = [False] * (n + 1)

Perm(1)