f  = open("input_s1_09.txt", "r")
a = f.readline().split()
i = len(a)
ii = 1
iii = 0
bol = True
an = []
if(i%2==0):
    i = i/2
else:
    i = ((i-1)/2)+1
while(ii<= int(len(a))):
    if(bol):
        i = i + iii
        bol = False
    else:
        i = i - iii
        bol = True
    an.append([])
    i1 = len(a[int(i-1)])
    ii1 = 1
    iii1 = 0
    bol1 = True
    if(i1%2==0):
        i1 = (i1/2) + 1
    else:
        i1 = ((i1-1)/2)+1
    while(ii1<= len(a[int(i-1)])):
        if(bol1):
            i1 = i1 + iii1
            bol1 = False
        else:
            i1 = i1 - iii1
            bol1 = True
        an[int(i-1)].append(a[int(i-1)][int(i1-1)])
        ii1 = ii1 + 1
        iii1 = iii1 + 1
    ii = ii + 1
    iii = iii + 1
for j in an:
    for g in j:
        print(g, end = '')
    print(" ", end = '')

