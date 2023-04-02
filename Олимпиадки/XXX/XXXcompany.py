number_name = {}
bossAsubordinate = {}
sortnumbers = set()
intNTstr = {}
f = open("input_s1_16.txt")
flag = 1
while(flag):
    boss = f.readline().split(" ", 1)
    if boss[0] == "END\n":
        flag = 0
    else:
        subordinate = str(f.readline()).split(" ", 1)
        if(boss[0] in bossAsubordinate):
            bossAsubordinate[boss[0]].add(subordinate[0])
        else:
            bossAsubordinate[boss[0]] = set([subordinate[0]])
        intNTstr[int(boss[0])] = boss[0]
        intNTstr[int(subordinate[0])] = subordinate[0]
        sortnumbers.add(int(boss[0]))
        sortnumbers.add(int(subordinate[0]))
        if len(boss)>1:
            number_name[boss[0]] = boss[1]
        if len(subordinate)>1:
            number_name[subordinate[0]] = subordinate[1]
RbossAsubordinate = []
for i in bossAsubordinate:
    RbossAsubordinate.append(i)
for i in reversed(RbossAsubordinate):
    for j in bossAsubordinate:
        if i in bossAsubordinate[j]:
            for h in bossAsubordinate[i]:
                bossAsubordinate[j].add(h)
a = f.readline()
if not(a.isdigit()):
    for i in number_name:
        if number_name[i] == a + "\n":
            aa = i
        #print(number_name[i], a, i)
else:
    print("!")
    aa = intNTstr[int(a)]
if aa in bossAsubordinate:
    for i in sortnumbers:
        if intNTstr[i] in bossAsubordinate[aa]:
            if intNTstr[i] in number_name:
                print(intNTstr[i] , number_name[intNTstr[i]])
            else:
                print(intNTstr[i] , "Unknown Name")
else:
    print("NO")
            
        
        
