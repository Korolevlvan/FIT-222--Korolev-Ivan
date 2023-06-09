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

def Fcicl(a, b, c):
    if c == b[0]:
        return False
    else:
        flag = True
        for i in a:
            if c == i[0]:
                cash1 = a.copy()
                cash1.pop(i)
                if not(Fcicl(cash1, b, i[1])):
                    flag = False
            elif c == i[1]:
                cash2 = a.copy()
                cash2.pop(i)
                if not(Fcicl(cash2, b, i[0])):
                    flag = False
    return flag
f = open("prim.txt", "r")
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
nodes.add(edge[0][0])
ansg[edge[0]] = b[edge[0]]
print(f"ребро{i} добавлено, вершина{j}")
for l in range(1, 8):
    flag = True
    nodesc = nodes.copy()
    for j in nodesc:
        if flag:
            for i in edge[1:]:
                if Fcicl(ansg, i, i[1]) and not(len(ansg) == 7) and (flag) and (j in i):
                    nodes.add(i[0])
                    nodes.add(i[1])
                    ansg[i[0], i[1]] = b[i[0], i[1]]
                    flag = False
                    print(f"ребро{i} добавлено, вершина{j}")
#отрисовка
for i in ansg:
    G.add_nodes_from(i)
    G.add_edge(i[0], i[1])
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels = True)
nx.draw_networkx_edge_labels(G,pos, edge_labels = ansg, font_color='red')
plt.show()
