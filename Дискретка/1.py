file = open("seti-i-potoki.txt")
N = int(file.readline())
M = int(file.readline())
a = [[[0,0,1] for j in range(N)] for i in range(N)]
for i in range(M):
    b = file.readline().split()
    a[int(b[0])-1][int(b[1])-1][0] = int(b[2])
    a[int(b[1])-1][int(b[0])-1][0] = int(b[2])
    a[int(b[1])-1][int(b[0])-1][2] = -1
print(a)
