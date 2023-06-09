f = open("Floyd.txt","r")
N = int(f.readline())
M = int(f.readline())
a = [[float('inf')]*N for i in range(N)]
for i in range(N):
    a[i][i] = 0
for i in range(M):
    b = f.readline().split()
    a[int(b[0])-1][int(b[1])-1] = int(b[2])
for i in range(N):
    for ii in range(N):
        for iii in range(N):
            a[ii][iii] = min(a[ii][iii], a[ii][i] + a[i][iii])
print('\n'.join('\t'.join(map(str, row)) for row in a))

            
