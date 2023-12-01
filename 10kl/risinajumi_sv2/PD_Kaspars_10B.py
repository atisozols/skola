# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]

ievade = input("ievadi skaitli: ")
skaitlis = int(ievade)
cipari = list(map(int, str(skaitlis)))
print("ievaditais skaitlis sarakstaa:", cipari)

# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.

saraksts = []

while True:
    ievade = input("ievadi 0, lai partrauktu:")
    skaitlis = int(ievade)

    if skaitlis == 0:
        break
    else:
        saraksts.append(skaitlis)
nepara_skaitlis = [skaitlis for skaitlis in saraksts if skaitlis % 2 != 0]
mazakaie_n_skaitlis = sorted(nepara_skaitlis)[:3]

print("ievaditie skaitli:", saraksts)
print("3 mazakie nepara skaitli", mazakaie_n_skaitlis)

# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

import random

skaitli = random.sample(range(1, 12), 10)

print("saraksts ar 10 random skaitliem:", skaitli)

# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

a = [3, 5, 6, 4]
b = [2, 2, 3, 1]

c = []
