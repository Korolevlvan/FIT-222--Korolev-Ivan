def substractL(a, A, AA, B):
    for pair in B:
        if pair[0] == a and (pair[1] in AA):
            if (A[pair[0]] >= B[pair]) and (AA[pair[1]] >= B[pair]):
                A[pair[0]] = A[pair[0]] - B[pair]
                AA[pair[1]] = AA[pair[1]] - B[pair]
                B[pair] = 0
            else:
                if(A[pair[0]] >= AA[pair[1]]):
                    A[pair[0]] -= AA[pair[1]]
                    B[pair] -= AA[pair[1]]
                    AA[pair[1]] = 0
                else:
                    AA[pair[1]] -= A[pair[0]]
                    B[pair] -= A[pair[0]]
                    A[pair[0]] = 0
def substractR(a, A, AA, B):
    for pair in B:
        if pair[1] == a and (pair[0] in A):
            if (A[pair[0]] >= B[pair]) and (AA[pair[1]] >= B[pair]):
                A[pair[0]] = A[pair[0]] - B[pair]
                AA[pair[1]] = AA[pair[1]] - B[pair]
                B[pair] = 0
            else:
                if(A[pair[0]] >= AA[pair[1]]):
                    A[pair[0]] -= AA[pair[1]]
                    B[pair] -= AA[pair[1]]
                    AA[pair[1]] = 0
                else:
                    AA[pair[1]] -= A[pair[0]]
                    B[pair] -= A[pair[0]]
                    A[pair[0]] = 0
def substractLL(a, A, AA, B):
    d = 0
    for pair in B:
        if pair[0] == a and (pair[1] in AA):
            if (A[pair[0]] >= B[pair]) and (AA[pair[1]] >= B[pair]):
                A[pair[0]] = A[pair[0]] - B[pair]
                AA[pair[1]] = AA[pair[1]] - B[pair]
                d += B[pair]
                B[pair] = 0
            else:
                if(A[pair[0]] >= AA[pair[1]]):
                    A[pair[0]] -= AA[pair[1]]
                    B[pair] -= AA[pair[1]]
                    d += AA[pair[1]]
                    AA[pair[1]] = 0
                else:
                    AA[pair[1]] -= A[pair[0]]
                    B[pair] -= A[pair[0]]
                    d += A[pair[0]]
                    A[pair[0]] = 0
    return d
def substractRR(a, A, AA, B):
    d = 0
    for pair in B:
        if pair[1] == a and (pair[0] in A):
            if (A[pair[0]] >= B[pair]) and (AA[pair[1]] >= B[pair]):
                A[pair[0]] = A[pair[0]] - B[pair]
                AA[pair[1]] = AA[pair[1]] - B[pair]
                d += B[pair]
                B[pair] = 0
            else:
                if(A[pair[0]] >= AA[pair[1]]):
                    A[pair[0]] -= AA[pair[1]]
                    B[pair] -= AA[pair[1]]
                    d += AA[pair[1]]
                    AA[pair[1]] = 0
                else:
                    AA[pair[1]] -= A[pair[0]]
                    B[pair] -= A[pair[0]]
                    d += A[pair[0]]
                    A[pair[0]] = 0
    return d
    
#Считывание
f = open("input_s1_07.txt")
pairs = {}
n = int(f.readline())
for i in range(n):
    a = f.readline()
    if (a[0], a[-2]) in pairs:
        pairs[a[0], a[-2]] = int(pairs[a[0], a[-2]]) + 1
    else:
        pairs[a[0], a[-2]] =  1
lettersL = {}
n = int(f.readline())
for i in range(n):
    a = f.readline().split()
    lettersL[a[0]] = int(a[1])
lettersR = {}
n = int(f.readline())
for i in range(n):
    a = f.readline().split()
    lettersR[a[0]] = int(a[1])
#Алгоритм
Ansver = 0
sum_of_pairs = 0
for letter in lettersL:
    sum_of_pairs = 0
    for pair in  pairs:
        if pair[0] == letter and pair[1] in lettersR:
            sum_of_pairs = sum_of_pairs + pairs[pair]
    if sum_of_pairs <= lettersL[letter]:
        Ansver = Ansver + sum_of_pairs
        substractL(letter, lettersL, lettersR, pairs)  
for letter in lettersR:
    sum_of_pairs = 0
    for pair in  pairs:
        if pair[1] == letter and pair[0] in lettersL:
            sum_of_pairs = sum_of_pairs + pairs[pair]
    if sum_of_pairs <= lettersR[letter]:
        Ansver = Ansver + sum_of_pairs
        substractR(letter, lettersL, lettersR, pairs)
for letter in lettersL:
    Ansver += substractLL(letter, lettersL, lettersR, pairs)
for letter in lettersR:
    Ansver += substractRR(letter, lettersL, lettersR, pairs)
print(Ansver)
