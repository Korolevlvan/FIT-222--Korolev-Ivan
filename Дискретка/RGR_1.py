N = int(input())
M = int(input())
a = [[float('inf')]*N for i in range(N)]
for i in range(N):
    a[i][i] = 0
for i in range(M):
    b = input().split()
    a[int(b[0])-1][int(b[1])-1] = int(b[2])
for i in range(N):
    for ii in range(N):
        for iii in range(N):
            a[ii][iii] = min(a[ii][iii], a[ii][i] + a[i][iii])
for i in range(N):
    for j in range(N):
        if a[i][j] != float('inf'):
            print(f"из {i} в {j}:{a[i][j]}")
        else:
            print(f"из {i} в {j}:-1")
            
