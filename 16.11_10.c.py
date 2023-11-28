# # # Ievada n. Programma, kas izvada 
# # # visus skaitļus no n līdz 2n.

# # n = int(input('ievadi n:'))
# # for i in range(n, 2 * n + 1):
# #     print(i)

# # # Programma, kas saskaita visus
# # #  skaitļus no 1 līdz 100.

# # sum = 0
# # for i in range(1, 101):
# #     sum += i

# # print(sum)

# # # Izvadīt visus nepāra skaitļus dilstošā
# # #  secībā no 25 līdz 1.

# # for i in range(25, 0, -2):
# #     print(i)

# # # Izmantojot ciklu, izveidot programmu, kas liek
# # # ievadīt piecus skaitļus un izvada to summu.
# # sum = 0
# # for i in range(5):
# #     sk = int(input('ievadi skaitli: '))
# #     sum += sk

# # print(sum)


# # while cikls

# # f = 1
# # n = int(input('ievadi sk: '))
# # while n != 0:
# #     f = f * n
# #     n = n - 1

# # print(f)

# # visi skaitļu kvadrāti,
# # kas mazāki par 100
# # viens ar for, otrs ar while


# ievada skaitļus, kamēr ievada 0, pasakot, vai 
# ievadītais ir pāra vai nepāra

# x = int(input('ievadi skaitli: '))
# while x != 0:
#     if x % 2 == 0:
#         print('pāra')
#     else:
#         print('nepāra')
#     x = int(input('ievadi skaitli: '))

# # ievada skaitļus, kamēr ievada 0, programma no
# # ievadītajiem, izvada pāra skaitļu summu
# sum = 0
# x = int(input('ievadi skaitli: '))
# while x != 0:
#     if x % 2 == 0:
#         sum += x
#     x = int(input('ievadi skaitli: '))
# print(sum)

# tiek vadīti skaitļi, kamēr summa pārsniedz 20

# x = int(input('ievadi skaitli: '))
# sum = x
# while sum < 20:
#     x = int(input('ievadi skaitli: '))
#     sum += x

# print(sum)

# sadalīt patvaļīgu skaitli ciparos

# x = int(input('ievadi skaitli: '))

# while x > 0:
#     print(x % 10)
#     x = int(( x - x % 10 ) / 10)


# vada skaitļus, kamēr ievada nulli. 
# programma pasaka lielako no ievaditajiem

# x = int(input("ievade: "))
# lielakais = x
# while x != 0:
#     x = int(input("ievade: "))
#     if x > lielakais:
#         lielakais = x
# print(lielakais)

# izmantojot for ciklu, pateikt, cik dalītāju
# ir ievadītajam skaitlim x
 
# x = int(input("ievade: "))
# skaits = 0
# for i in range(1, x + 1):
#     if x % i == 0:
#         skaits += 1

# print(skaits)


for i in range(20):
    for j in range(20):
        if i % 2 == 0 and j % 2 == 0:
            print(1, end=' ')
        elif i % 2 != 0 and j % 2 != 0:
            print(1, end=' ')
        else:
            print(0, end=" ")
    print()








    

















