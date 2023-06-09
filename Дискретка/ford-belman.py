f = open("ford-belman.txt","r")
N = int(f.readline())
M = int(f.readline())
a = [[float('inf')]*N for i in range(N)]
a1 = [[float('inf')]*N for i in range(N)]
for i in range(N):
    a[i][i] = 0
for i in range(M):
    b = f.readline().split()
    a[int(b[0])-1][int(b[1])-1] = int(b[2])
a1[0][0] = 0;
for i in range(1, N):
    for j in range(N):
        k = []
        for h in range(N):
            k.append(a1[i-1][h] + a[h][j])
        a1[i][j] = min(k)
for i in range(N):
    print(f"из 1 в {i+1} = {a1[N-1][i]}")
