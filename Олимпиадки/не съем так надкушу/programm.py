class branch:
    def __init__(self, basis, length, number):
        self.basis = basis
        self.length = length
        self.number = number
    def path(self, past_path, n):
        n += (self.length*2)
        past_path.add(self.number)
        if(self.basis == None)or(self.basis.number in past_path):
            return n
        else:
            return self.basis.path(past_path, n)
    def ancestry(self, a):
        if(self.basis != None):
            a.add(self.basis.number)
            self.basis.ancestry(a)
def path_XA(a, b):
    pp = set()
    a.ancestry(pp)
    n = 0
    n = b.path(pp, n)
    pp = set()
    b.ancestry(pp)
    n = a.path(pp, n)
    return n/2
f = open("input_s1_13.txt")
a = f.readline().split()
N = int(a[0])
M = int(a[1])
branches = {}
past_path = set()
a = f.readline().split()
branches[1] = branch(None, int(a[1]), int(1))
for i in range(2,N+1):
    a = f.readline().split()
    if(int(a[0]) == 0):
        branches[i] = branch(None, int(a[1]), int(i))
    else:
        branches[i] = branch(branches[int(a[0])], int(a[1]), int(i))
Ansver = 0
apples = {}
for i in range(M):
    a = f.readline().split()
    apples[int(a[0])] = int(a[1])
a = f.readline().split()
X = int(a[0])
Z = int(a[1])
final_apple = 0
first_apple = 0
#убираем яблоки
bad_apples = []
for i in apples:
    if apples[i] < Z:
        bad_apples.append(i)
for i in bad_apples:
    apples.pop(i, None)
#перебираю лишние пути
extra_ways = []
extra_ways.append(path_XA(branches[1], branches[X]))
extra_ways.append(path_XA(branches[N], branches[X]))
for i in range()
