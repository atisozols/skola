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
