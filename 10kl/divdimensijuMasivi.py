def printArray(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()


# i  0  1  2  3  4
m = [1, 5, 2, 7, 8]

# for elem in m:
#     print(elem)
    
# for i in range(len(m)):
#     print(m[i])

divd = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

# for row in divd:
#     for elem in row:
#         print(elem, end=" ")
#     print()

# for i in range(len(divd)):
#     for j in range(len(divd[i])):
#         print(divd[i][j], end=" ")
#     print()
        
    
# 1. Izvadīt 2D masīva nepāra rindas

# for i in range(len(divd)):
#     for j in range(len(divd[i])):
#         if i % 2 == 0:
#             print(divd[i][j], end=" ")
#     print()

# 2. Otro kolonnu

# for i in range(len(divd)):
#     for j in range(len(divd[i])):
#         if j == 1:
#             print(divd[i][j], end=" ")
#     print()
    
# 3. Diagonāles elementus

# for i in range(len(divd)):
#     for j in range(len(divd[i])):
#         if i == j:
#             print(divd[i][j], end=" ")
#     print()
    
# 4. Otru diagonāli

# for i in range(len(divd)):
#     for j in range(len(divd[i])):
#         if i + j == len(divd) - 1:
#             print(divd[i][j], end=" ")
#     print()

# 5. Izveidot 5x5 masīvu, aizpildot to ar 0

x, y = 10, 10
arr = [[0 for _ in range(x)] for _ in range(y)]
    
# 6. Programma, kas aizpilda masīvu ar 1 diagonālēs

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if j == i:
#             arr[i][j] = 1
#         elif j + i == 9:
#             arr[i][j] = 1
            
# printArray(arr)

# 7. Aizpilda rāmi ar 1

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if j == 0 or i == 0 or i == 9 or j == 9:
#             arr[i][j] = 1
            
# printArray(arr)

########## FUNKCIJAS

# 1. funkcija tilpums, kas ieejā saņem trīs parametrus 
#    un atgriež atbilstošā paralēlskaldņa tilpumu
#    nodemonstrēt funkcijas izsaukumu

# def tilpums(a, b, c):
    
    
# 2. funkcija max_value, kas ieejā saņem vienu parametru - patvaļīgi garu masīvu
#    funkcija atgriež masīva lielāko vērtību

# def max_value(m):
#     max = m[0]
#     for el in m:
#         if el > max:
#             max = el
#     return max

# masivs = [1, 5, 3, 7]

# print(max_value(masivs))
# print(max_value([7, 9, 2, 4, 1, 7]))

# 3. Funkcija isEven, kas ieejā saņem skaitli un izejā atgriež vai nu 
#    True vai False atkarībā no tā, vai skaitlis ir pāra

# def isEven(n):
#     if n % 2 == 0:
#         return True
#     else: 
#         return False
    

# if isEven(44):
#     print('yes')

# 8. Dots divdimensiju masīvs. Aprēķināt katras rindas vidējo vērtību;
#    katras kolonnas vid. vērtību

divd = [[8, 4, 3],
        [4, 5, 1],
        [7, 9, 9]]

# # "1. rindas vid = 5, 2.rindas ..."
# print("rindas:")
# for row in divd:
#     sum = 0
#     for elem in row:
#         sum += elem
        
#     print(sum/3)

# print("kolonnas:")

# for i in range(3):
#     sum = 0
#     for j in range(3):
#         sum += divd[j][i]
#     print(sum/3)
    
    
# Izvada visu elementu summu un vid vērtību

# sum = 0
# for row in divd:
#     for elem in row:
#         sum += elem
# print(sum, sum/9)

# 9. Uzrakstīt programmu, kas ļauj ievadīt lietotājam 3x3 masīva elementus.

# m = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         x = int(input("sk: "))
#         row.append(x)
#     m.append(row)
    
# printArray(m)
    
    
# 10. Divi 2D masīvi izmērā 2x2. Saskaitīt tos, izveidojot trešo masīvu.

# a = [[2, 5], 
#      [7, 1]]    

# b = [[3, 0], 
#      [-2, 4]]

# c = []


# for i in range(2):
#     row = []
#     for j in range(2):
#         x = a[i][j] + b[i][j]
#         row.append(x)
#     c.append(row)
    
# printArray(c)

# 11. Programma, kas saglabā grafu atmiņā.
#     Cik punkti? 
#     Ievadi virsotni 1:
#     Ievadi virsotni 2:


# sk = int(input('cik?')) # 4
# graph = [[] for _ in range(sk)] # [[], [], [], []]

# v1 = int(input("v1: ")) # 2
# v2 = int(input("v2: ")) # 0
#                         # [[2], [], [0], []]
# while v1 < sk and v2 < sk:
#     graph[v1].append(v2)
#     graph[v2].append(v1)
    
#     v1 = int(input("v1: "))
#     v2 = int(input("v2: "))

# print(graph)

# Dots 8x8 masīvs no nullēm

arr = [[0 for _ in range(8)] for _ in range(8)]

# 12. Ievadīt x, y. Masīvā ielikt 1 atbilstošajā pozīcijā.

# x = int(input('ievadi x: '))
# y = int(input('ievadi y: '))

# arr[x-1][y-1] = 1

# 13. Ievadīt šaha lauciņa pozīciju(e4).

# horizont = 'abcdefgh'

# poz = input('ievadi poziciju: ')

# y = horizont.index(poz[0]) # 4
# x = 8 - int(poz[1]) # 1

# arr[x][y] = 1

# 14. No ievadītās pozīcijas parādīt visus iespējamos gājienus:
#    a) tornim

# for i in range(8):
#     for j in range(8):
#         if i == x or j == y:
#             arr[i][j] = 1

#    b) laidnim

# for i in range(8):
#     for j in range(8):
#         if i + j == x + y or i - j == x - y:
#             arr[i][j] = 1

#    c) dāmai

# for i in range(8):
#     for j in range(8):
#         if i + j == x + y or i - j == x - y or i == x or j == y:
#             arr[i][j] = 1

#    d) karalim

# for i in range(8):
#     for j in range(8):
#         if abs(x - i) <= 1 and abs(y - j) <= 1:
#             arr[i][j] = 1

#    e) zirgam

# for i in range(8):
#     for j in range(8):
#         if (abs(x - i) == 1 and abs(y - j) == 2) or (abs(x - i) == 2 and abs(y - j) == 1):
#             arr[i][j] = 1

# arr[x][y] = 2

# printArray(arr)


# 15. Izveidojam 10x10 masīvu - reizināšanas tabulu!

# tabula = [[0 for _ in range(10)] for _ in range(10)]

# for i in range(10):
#         for j in range(10):
#                 tabula[i][j] = (i + 1) * (j + 1)

# printArray(tabula)

# 16. Dots masīvs garumā 9. Izveidot no masīva 3x3 2D masīvu.

# mas = [2, 5, 7, 2, 7, 1, 4, 9, 2]

# mas_after = [[2, 5, 7],
#              [2, 7, 1],
#              [4, 9, 2]]

# m1 = []
# a = 0
# for i in range(3):
#         row = []
#         for j in range(3):
#                 row.append(mas[a])
#                 a += 1
#         m1.append(row)
        
# printArray(m1)

# mas_afte2 = [[2, 2, 4],
#              [5, 7, 9],
#              [7, 1, 2]]

### Gatavošanās PD

# 17. Lietotājs ievada 9 skaitļus. Programma izveido 2D 3x3 masīvu. Izvadīt masīvu uz ekrāna.

# m = []

# for i in range(3):
#         row = []
#         for j in range(3):
#                 n = int(input(str(i) + ", " + str(j) + ": "))
#                 row.append(n)
#         m.append(row)
# printArray(m)

# 18. Izvadīt masīva lielāko elementu un tā atrašanās vietu masīvā. (9 atrodas poz (3, 1))

# x = 0
# y = 0
# max = m[x][y]

# for i in range(3):
#         for j in range(3):
#                 if m[i][j] > max:
#                         max = m[i][j]
#                         x = i
#                         y = j
                        
# print("max vērtība ir", max, "un atrodas poz", x, y)

# 19. Izvadīt katras rindas vidējo vērtību. (* katras kolonnas vidējo)

# for row in m:
#         sum = 0
#         for elem in row:
#                 sum += elem # sum += m[j][i]
#         print("vid:", sum/3)

# 20. Izvadīt summu tiem elementiem, kas neatrodas uz nevienas no diagonālēm.

# sum = 0
# for i in range(3):
#         for j in range(3):
#                 if i != j and i + j != 2:
#                         sum += m[i][j]
                        
# print("20. uzd =", sum)

# 21. Funkcija numSum(n), kas skaitlim n atgriež ciparu summu.

# def numSum(n):
#         sum = 0
        
#         while n > 0:
#                 sum += n % 10
#                 n //= 10 # n = n // 10
                
#         return sum

# print(numSum(123))
# print(numSum(11))
# print(numSum(27804609))

# 22. Funkcija saknes(a, b, c), kas trīs padotiem parametriem 
# (kvadrātvienādojuma koeficientiem), atgriež masīvu ar saknēm.

# (a, b, c) -> [x1, x2]

def saknes(a, b, c):
        roots = []
        d = b ** 2 - 4 * a * c
        
        if d < 0:
                return roots
        elif d == 0:
                x = (-b)/(2 * a)
                roots.append(x)
                return roots
        else:
            x1 = (-b + d ** 0.5)/(2 * a)
            x2 = (-b - d ** 0.5)/(2 * a) 
            roots.append(x1)
            roots.append(x2)
            return roots
    
print(saknes(2, 5, 12))
  
# 23. Dots divdimensiju masīvs. Noteikt, vai tajā ir vairāk pāra skaitļi vai nepāra.  
      
dd = [[2, 8, 3],
      [5, 0, 1],
      [6, 9, 2]]

# 24. Dots desu laukums. Noteikt, vai tajā ir uzvarētājs
# un kurš uzvarēja. (Spēlē vieninieki pret nullītēm)

tic_tac_toe = [[0, 1, 0],
               [0, 0, 1],
               [1, 0, 1]]

winner = None

# Rindas
for row in tic_tac_toe:
        if sum(row) == 0:
                winner = 0
        elif sum(row) == 3:
                winner = 1
               
# Kolonnas 
for i in range(len(tic_tac_toe)):
        sum = 0
        for j in range(len(tic_tac_toe)):
                sum += tic_tac_toe[j][i]
        if sum == 3:
                winner = 1
        elif sum == 0:
                winner = 0
                
# Pirmā diagonāle
sum = 0
for i in range(len(tic_tac_toe)):
        for j in range(len(tic_tac_toe[i])): 
                if i == j:
                        sum += tic_tac_toe[i][j]  
if sum == 3:
        winner = 1
elif sum == 0:
        winner = 0  
        
# Otrā diagonāle
sum = 0
for i in range(len(tic_tac_toe)):
        for j in range(len(tic_tac_toe[i])): 
                if i + j == 2:
                        sum += tic_tac_toe[i][j]  
if sum == 3:
        winner = 1
elif sum == 0:
        winner = 0 
       
print(winner)

print(tic_tac_toe[1][0])

## SV

def printArray(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()

# 1. Dots 4x4 masīvs no nullēm. Aizpildīt to tā, ka sekojošā vieta masīvā satur koordinātu summu.

m = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

# 2. Izveidot funkciju maxValue2D(m), kas padotajam masīvam atgriež lielāko vērtību.

# 3. Programma pieprasa ievadīt 6 skaitļus. Tiek izveidots 3x2 divdimensiju masīvs.

# 4. Dots 4x4 masīvs no nullēm. Aizpildīt to ar skaitļiem no 1 līdz 10, skaitļus novietojot zem diagonāles.

# Rezultāts:
#   1 0 0 0
#   2 3 0 0
#   4 5 6 0
#   7 8 9 10

m = [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]]

# 5. Dots šaha laukums kurā stāv divas dāmas. Uzrakstīt programmu, kas pasaka, vai dāmas viena otru "redz".

import random

chess = [[0 for _ in range(8)] for _ in range(8)]
chess[random.randint(0,7)][random.randint(0,7)] = 1
chess[random.randint(0,7)][random.randint(0,7)] = 1

printArray(chess)

                


