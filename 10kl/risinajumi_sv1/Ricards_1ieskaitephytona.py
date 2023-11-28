# 1P. Programma, kas izvada visus skaitļus no -1 līdz -10 dilstošā secībā 

# x = int(input("x: "))
# y = int(input("y: "))
# for i in range(x, y - 1, -1):
#     print(i)

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no šiem skaitļiem ir lielāka ciparu summa.

# a = int(input("a: "))
# b = int(input("b: "))
# sum1 = 0
# sum2 = 0
# p = a % 10
# r = a // 10
# sum1 = p + r
# s = b % 10
# t = b // 10
# sum2 = s + t
# if sum1 > sum2:
#     print(sum1, "pirma skaitla ciparu summa ir lielaka")
# elif sum1 < sum2:
#     print(sum2, "otra skaitla ciparu summa ir lielaka")
# elif sum1 == sum2:
#     print(sum1, sum2, "abu skaitlu ciparu summas ir vienadas")

# 3P. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. No ievadītajiem skaitļiem atrast lielāko pāra skaitli.

# max = 0
# n = int(input("n: "))
# while n != 0:
#     if n % 2 == 0 and n > max:
#         max = n
#         n = int(input("n: "))
#     elif n % 2 == 1:
#         n = int(input("n: "))

# print(max)

# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.
# Piemērs: 1326569 -> 132 -> 2.0

# n = int(input("n: "))
# a = n // 100
# b = n % 10
# c = n // 10
# d = c % 100
# summa = a + b + d
# e = summa / 3
# print(e)

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

# skaits = 0
# max = 0
# n = int(input("n: "))
# u = n % 10
# o = n // 10
# for i in range(1, n + 1):
#     if n % i == 0:
#         skaits += 1
#     elif skaits == 2:
#         summa = u + o
#         print(summa)
#     elif skaits != 2:
#         print(n)
#     elif n > max:
#         print(max)
        