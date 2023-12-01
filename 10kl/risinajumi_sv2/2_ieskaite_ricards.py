# 1. Sarakasts par skaitli, piemēram, [2, 8, 4] -> 284.


# 2. Ievada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu, sarakstā atrod 3 lielākos pāra skaitļus.

max = 0
max1 = 0
max2 = 0
asd = []
n = int(input("n: "))
while n != 0:
    asd.append(n)
    n = int(input("n: "))

print(list(asd))
for i in asd:
    if i % 2 == 0 and i > max and i > max1 and i > max2:
        i == max
        for j in asd:
            if j % 2 == 0 and j < max and j > max2:
                j == max1
                for k in asd:
                    if k % 2 == 0 and k < max1:
                        k == max2

print(max, max1, max2)

# 3. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).

# import random
# a = []
# a = random.randint(1, 30)
# print(a)
# for i in a:
#     if i % 2 == 1:
#         a.append(i)
#         print(i)
# for i in range(10):
#     print(list(a))



# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c = []