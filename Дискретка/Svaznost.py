def arg_min(T, S):
    amin = -1
    m = float('inf') 
    for i, t in enumerate(T):
        if t < m and i not in S:
            m = t
            amin = i
    return amin
print("Выбирите граф:")
print("1 Diikstra(связан)")
print("2 Svasnost(не связан)")
gg = int(input())
if(gg == 1):
    f = open("Diikstra.txt","r")
else:
    f = open("Svaznost.txt","r")
N = int(f.readline())
M = int(f.readline())
a = [[float('inf')]*N for i in range(N)]
for i in range(N):
    a[i][i] = 0
for i in range(M):
    b = f.readline().split()
    a[int(b[0])-1][int(b[1])-1] = int(b[2])
    a[int(b[1])-1][int(b[0])-1] = int(b[2])
T = [float('inf')]*N   
v = 0       
S = {v}     
T[v] = 0    
G = [0]*N   
while v != -1:          
    for j, dw in enumerate(a[v]):   
        if j not in S:           
            w = T[v] + dw
            if w < T[j]:
                T[j] = w
                G[j] = v        
    v = arg_min(T, S)            
    if v >= 0:                   
        S.add(v)
if(float('inf') in T):
    print("Граф не связан.")
else:
    print('Граф связан.')
