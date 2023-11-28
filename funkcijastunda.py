# Izveidot funkciju, kas:

# 1. atgriež padotā skaitļa ciparu summu

def ciparu_summa(num):
    sum = 0
    while num > 0:
        p = num % 10
        sum += p
        num = (num - p) // 10
    return sum

    
# 2. apgriež skaitli otrādā secībā ( 356 -> 653 )

def otradi(num):
    sk = 0
    while num > 0:
        p = num % 10
        sk = sk * 10 + p
        num = (num - p) // 10
    return sk

# 3. skaitlis par masīvu ( 356 -> [3, 5, 6] )

def masivs_no(num):
    m = []
    while num > 0:
        p = num % 10
        m.insert(0, p) # append
        num = (num - p) // 10
    return m

# 4. saskaita pāra elementu skaitu masīvā

def countEven(masivs):
    count = 0
    for elem in masivs:
        if elem % 2 == 0:
            count += 1
    return count
    
# 5. nosaka, vai masīvs ir sakārtots augoši

def augoss(masivs):
    ok = True
    for i in range(len(masivs) - 1):
        if masivs[i] > masivs[i + 1]:
            ok = False

    return ok

# 6. nosaka, vai masīvs ir sakārtots ( augoši vai dilstoši )

def sakartots(masivs):
    ok = 1
    for i in range(len(masivs) - 1):
        if masivs[i] > masivs[i + 1]:
            ok = -1
    for i in range(len(masivs) - 1):
        if masivs[i] < masivs[i + 1]:
            ok = 0

    return  ok

print(sakartots([1, 2, 3]))
print(sakartots([3, 2, 1]))
print(sakartots([1, 6, 3]))

# faktorials

def faktorials(n):
    if n == 1:
        return n
    return n * faktorials(n - 1)

# diskriminants

def d(a, b, c):
    return b**2 - 4 * a * c

# lielakais_cipars

def lielakais_cipars(n):
    max = 0
    while n > 0:
        p = n % 10
        if p > max:
            max = p
        n = (n - p) // 10
    return max


# lkd

def lkd(a, b):
    if b == 0:
        return a
    return lkd(b, a % b)


# 1) 2d masiva diagonale

a = [[1, 2],
     [7, 9]]

b = [[1, 6, 3],
     [8, 0, 2],
     [9, 4, 4]]

def diagonale(m):
    diagonale = []
    for i in range(len(m)):
        for j in range(len(m[i])):
            if i == j:
                diagonale.append(m[i][j])
    return diagonale

print(diagonale(a))
print(diagonale(b))

# 2) viendimensiju masīva el summa

def elementuSumma(m):
    sum = 0
    for elem in m:
        sum += elem
    return sum

print(elementuSumma([1, 2, 3, 4, 5, 6]))



# 3) funkcija atgriež masīva lielākā elementa indeksu

def maxIndex(m):
    max = m[0]
    indekss = 0
    for i in range(len(m)):
        if m[i] > max:
            max = m[i]
            indekss = i
    return indekss

m = [1, 3, 6, 8, 2, 4, 1]
print(m[maxIndex(m)])

# 4) funkcija, kas atgriež visus skaitļus virs diagonāles kā vienu masīvu

m = [[8, 6, 4, 3, 7],
     [7, 9, 5, 2, 3], 
     [5, 8, 7, 3, 7], 
     [1, 5, 5, 9, 1], 
     [6, 4, 4, 5, 3]]

def virsDiagonales(m):
    arr = []
    for i in range(len(m)):
        for j in range(i + 1, len(m[i])):
            arr.append(m[i][j])
    return arr

# 5) masivs par skaitli [1, 15, 2, 4] - > 11524

def masivsParSkaitli(m):
    sk = 0
    for elem in m:
        sk = sk * 10 + elem
    return sk

o = [12, 11, 5, 2, 4]
n = masivsParSkaitli(o)
m = masivs_no(n)
print(m)


# print(masivsParSkaitli(virsDiagonales(m)))
# print(masivsParSkaitli(diagonale(m)))

def kolonna(m, kol):
