import networkx as nx
import matplotlib.pyplot as plt

def SortEdge(a, b):
    for i in a:
        c = a[i]
        cc = i
        for j in a:
            if (a[j] < c) and not(j in b):
                c = a[j]
                cc = j
            if cc in b and not(j in b):
                c = a[j]
                cc = j
        b.append(cc)

def Fcicl(a, b):
    c = b[1]
    while(1):
        flag = True
        for i in a:
            if(i[0] == c):
                flag = False
                if i[1] == b[0]:
                    return False
                c = i[1]
        if flag == True:
            return True
f = open("test2.txt", "r")
n = int(f.readline())
b = {}
for i in range(n):
    a = f.readline()
    aa = a.split()
    b[aa[0], aa[1]] = int(aa[2])
G= nx.Graph(directed=True)
edge = []
SortEdge(b, edge)
ansg = {}
nodes = set([])

nodes.add(edge[0])
ansg[edge[0]] = b[edge[0]]
for i in edge[1:]:
    if Fcicl(ansg, i) and not((i[0] in nodes) and (i[1] in nodes)):
        nodes.add(i[0])
        nodes.add(i[1])
        ansg[i[0], i[1]] = b[i[0], i[1]]
#отрисовка
print(ansg)
for i in ansg:
    G.add_nodes_from(i)
    G.add_edge(i[0], i[1])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True)
nx.draw_networkx_edge_labels(G,pos, edge_labels = , font_color='red')
plt.show()
