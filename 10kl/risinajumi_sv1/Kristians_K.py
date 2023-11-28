# 1P. Programma, kas izvada visus skaitļus no -1 līdz -10 dilstošā secībā

# for i in range(-1, -11, -1):

#  print(i)

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no šiem skaitļiem ir lielāka ciparu summa.

# sumx = 0 
# sumy = 0
# x = int(input("ievadi x:"))
# y = int(input("ievadi y:"))
# while x > 0:
#     p = x % 10
#     sumx += p 
#     x = x // 10
# while y > 0:
#     v = y % 10
#     sumy += v 
#     y = y // 10
# if sumx > sumy:
#     print(sumx)
# elif sumx == sumy:
#     print('vienādi')
# else: 
#     print(sumy)

# Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. No ir ievadītajiem skaitļiem atrast lielāko pāra skaitli.

# max = 0
# x = int(input("x: "))
# while x != 0:
#     if x % 2 == 0:
#         if x > max:
#             max = x
#     x = int(input("x: "))
# print(max)




# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.\

# sum = 0
# skaits = 0
# n = int(input('n:'))
# while n != 0:
#       p = n % 10
#       sum += p
#       skaits += 1
#       n = n // 10
#       if skaits == 3:
#             a = sum // 3
# print(a)           


# # Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

# sumx = 0
# n = int(input('n: '))
# for i in range(1, n + 1):
#     if n % i == 0:
#          p = n % 10
#          sumx += p
#          print(sumx)
#     elif n % i != 0:
#          v = n % 10
#          print(v)
