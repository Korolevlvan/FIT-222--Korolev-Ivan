f = open("input_s1_25.txt", "r")
b = f.readline().split()
N = int(b[0])
M = int(b[1])
a = [[float('inf')]*(N+1) for i in range(N+1)]
for i in range(N+1):
    a[i][i] = 0
for i in range(1, N+1):
    b = f.readline().split()
    a[i][int(b[0])] = int(b[1])
    a[int(b[0])][i] = int(b[1])
aples = {}
for i in range(M):
    b = f.readline().split()
    aples[int(b[0])] = int(b[1])
b = f.readline().split()
X = int(b[0])
Z = int(b[1])
apples = set([])
for i in aples:
    if aples[i] >= Z:
        apples.add(i)
for i in range(N+1):
    for ii in range(N+1):
        for iii in range(N+1):
            a[ii][iii] = min(a[ii][iii], a[ii][i] + a[i][iii])
way = float('inf')
for i in apples:
    tway = a[X][i]
    tapples = apples.copy()
    tapples.remove(i)
    j = i
    ttway = 0
    while(len(tapples) != 0):
        tttway = float('inf')
        for ii in tapples:
            if a[j][ii] < tttway:
                tttway = a[j][ii]
                jj = ii
        ttway += tttway
        j = jj
        tapples.remove(j)
    tway += ttway
    if tway < way:
        way = tway
print(way)
        
        

