# 1P. Saraksts par skaitli. Piemēram, [2, 8, 4] -> 284
arr = [3,8,8,8,1,2,3]
sk = 0
it = pow(10, len(arr)-1)
for e in arr:
    sk += e * it
    it = it // 10
print(sk)

# 2P. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 lielākos pāra skaitļus.
n = int(input("Skaitlis: "))
arr = []
while n != 0:
    arr.append(n)
    n = int(input("Skaitlis: "))
arr.sort()
a2 = []
for i in range(len(arr)-1, 0, -1):
    if arr[i] % 2 == 0 and len(a2) < 3:
        a2.append(arr[i])
print(a2)

# 3P. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).
import random
arr = []
while len(arr) < 10:
    s = random.randint(1,30)
    if s % 2 != 0:
        arr.append(s)
print(arr)

# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.
#   1523
#  -1230
#  = 293
a = [1, 5, 2, 3]
b = [1, 2, 3, 0]

c = []
sub = 0
for i in range(len(a)-1, -1, -1):
    fn = a[i] - b[i]
    if fn < 0:
        fn += 10
        sub = 1
    a[i-1] -= sub
    sub = 0
    if fn == 0 and i == 0:
        pass
    else:
        c.insert(0, fn)
print(c)