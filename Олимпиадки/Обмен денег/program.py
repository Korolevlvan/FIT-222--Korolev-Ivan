f = open("input14.txt", "r")
a1 = f.readline().split()
a2 = f.readline().split()
a3 = f.readline().split()
a4 = f.readline().split()
a5 = f.readline().split()
s1 = []
for i in a5:
    s1.append(int(i))
tr = 0
tabu1 = set([])
for i in a2[1:]:
    tabu1.add(int(i))
tabu2 = set([])
for i in a4[1:]:
    tabu2.add(int(i))
for i in range(len(s1)):
    g = 0
    for j in tabu1:
        if j <= s1[i]:
            g += 1
    s1[i] -= g
for i in range(len(s1)-1):
    s1[i+1] += s1[i]*int(a1[i+1])
tr = s1[-1]
a3.reverse()
s2 = [tr]
for i in range(int(a3[-1]) - 1):
    s2.append(s2[i]//int(a3[i]))
    s2[i] = s2[i]%int(a3[i])
for i in range(len(s2)):
    for j in tabu2:
        if j <= s2[i]:
            s2[i] += 1
for i in range(int(a3[-1]) - 1):
    s2[i+1] += s2[i]//int(a3[i])
    s2[i] = s2[i]%int(a3[i])
s2.reverse()
print(s2)
    

