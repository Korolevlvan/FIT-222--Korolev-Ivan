import math
def get_max_vertex(k, V, S):
    m = 0  
    v = -1
    for i, w in enumerate(V[k]):
        if i in S:
            continue
        if w[2] == 1:  
            if m < w[0]:
                m = w[0]
                v = i
        else:           
            if m < w[1]:
                m = w[1]
                v = i

    return v

def get_max_flow(T):
    w = [x[0] for x in T]
    return min(*w)

def updateA(V, T, f):
    for t in T:
        if not(t[1] == -1):  
            sgn = V[t[2]][t[1]][2]
            V[t[1]][t[2]][0] -= f * sgn
            V[t[1]][t[2]][1] += f * sgn
            V[t[2]][t[1]][0] -= f * sgn
            V[t[2]][t[1]][1] += f * sgn

file = open("seti-i-potoki.txt")
N = int(file.readline())
M = int(file.readline())
a = [[[0,0,1] for j in range(N)] for i in range(N)]
for i in range(M):
    b = file.readline().split()
    a[int(b[0])-1][int(b[1])-1][0] = int(b[2])
    a[int(b[1])-1][int(b[0])-1][0] = int(b[2])
    a[int(b[1])-1][int(b[0])-1][2] = -1
init = 0    
end = N-1    
Tinit = (math.inf, -1, init)      
f = []      
j = init
while j != -1:
    k = init  
    T = [Tinit] 
    S = {init}  
    while k != end:     
        flag = True
        j = get_max_vertex(k, a, S)
        if j == -1:        
            if k == init:      
                break         
            else:           
                k = T.pop()[2]
                flag = False
        if flag:
            c = a[k][j][0] if a[k][j][2] == 1 else a[k][j][1]   
            T.append((c, j, k))   
            S.add(j)           
            if j == end:    
                f.append(get_max_flow(T))     
                updateA(a, T, f[-1])        
                break
            k = j
F = sum(f)
print(f"Максимальный поток: {F}")


