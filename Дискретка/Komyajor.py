f = open("Komyajor.txt","r")
N = int(f.readline())
M = int(f.readline())
a = [[float('inf')]*N for i in range(N)]
for i in range(N):
    a[i][i] = float('inf')
for i in range(M):
    b = f.readline().split()
    a[int(b[0])-1][int(b[1])-1] = int(b[2])
    a[int(b[1])-1][int(b[0])-1] = int(b[2])
way = 0
hh = [[3, 1],[4,2],[2,0],[1,1],[1,0]]
for i in hh:
    print(a[i[0]][i[1]])
while len(a) != 1:
    minw = 0
    for string in a:
        minwt = string[0]
        mini = 0
        for weight in string:
            if weight < minwt:
                minwt = weight
        for i in range(len(string)):
            string[i] -= minwt
        minw += minwt
    for i in range(len(a)):
        minwt = a[0][0]
        mini = 0
        for j in range(len(a)):
            if a[j][i] < minwt:
                minwt = a[j][i]
                mini = j
        for j in range(len(a)):
            a[j][i] -= minwt
        minw += minwt
    maxnol = 0
    inol = 0
    jnol = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                minstr = float('inf')
                mincol = float('inf')
                for r in a[i][0:j] + a[i][j+1:]:
                    minstr = min(minstr, r)
                for g in range(len(a)):
                    if g != i:
                        mincol = min(mincol, a[g][j])
                if minstr + mincol >maxnol:
                    maxnol = minstr + mincol
                    inol = i
                    jnol = j
    a[jnol][inol] = float('inf')
    a.pop(inol)
    for i in range(len(a)):
        a[i].pop(jnol)
    print(minw)
    way += minw
print(f"минимульный путь:{way}")
