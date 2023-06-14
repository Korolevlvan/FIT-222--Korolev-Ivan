f = open("input10.txt", "r")
k = 1
a = {}
while(1):
    b = f.readline()
    if(b == ''):
        break
    g = b.split()
    for i in range(len(g)):
        if g[i].isnumeric():
            g[i] = a[int(g[i])]
    if g[0] == 'MIX':
        a[k] = 'MX'
        for i in range(1, len(g)):
            a[k] = a[k] + g[i]
        a[k] =  a[k] + 'XM'
    if g[0] == 'WATER':
        a[k] = 'WT'
        for i in range(1, len(g)):
            a[k] = a[k] + g[i]
        a[k] =  a[k] + 'TW'
    if g[0] == 'DUST':
        a[k] = 'DT'
        for i in range(1, len(g)):
            a[k] = a[k] + g[i]
        a[k] =  a[k] + 'TD'
    if g[0] == 'FIRE':
        a[k] = 'FR'
        for i in range(1, len(g)):
            a[k] = a[k] + g[i]
        a[k] =  a[k] + 'RF'
    k += 1
print(a[k-1])
    
