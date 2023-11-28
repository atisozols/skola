# # vai lielaks par 10, mazaks vai vienads
# # 10 -> vienads
# # 5 -> mazaks
# # 11 -> lielaks
# x = int(input('ievadi skaitli: '))

# if x < 10:
#     print('mazaks par 10')
# elif x > 10:
#     print('lielaks par 10')
# else:
#     print('vienads')
# x = int(input('ievadi skaitli: '))
# if x > 9 and x < 100:
#         print('divciparu skaitlis')
# else:
#     print('nav')

# # ievada skaitli - menēša, programma pasaka, 
# # cik mēnesī dienu
# # mēneši 1 - 12
# # ievade      -> atbilde
# # 2           -> 28
# # 4, 6, 9, 11 -> 30
# # parejie     -> 31 

# m = int(input('ievadi menesi: '))
# if m > 0 and m < 13:
#     if m == 2:
#         print(m,'. menesi ir 28 dienas')
#     elif m == 4 or m == 6 or m == 9 or m == 11:
#         print(m,'. menesi ir 30 dienas')
#     else:
#         print(m,'. menesi ir 31 dienas')

# m = int(input('ievadi menesi: '))
# g = int(input('ievadi gadu: '))
# if m > 0 and m < 13:
#     if m == 2:
#         if g % 4 == 0:
#             print(m,'. menesi ir 29 dienas')
#         else:
#             print(m,'. menesi ir 28 dienas')
#     elif m == 4 or m == 6 or m == 9 or m == 11:
#         print(m,'. menesi ir 30 dienas')
#     else:
#         print(m,'. menesi ir 31 dienas')


# a = int(input('ievadi 1, ja ir dots radiuss, 2, ja dots laukums: '))
# if a == 1:
#     r = int(input('radiuss: '))
#     s = 3.14 * r**2
#     print('laukums:', s)
# elif a == 2:
#     s = int(input('laukums: '))
#     r = (s/3.14)**0.5
#     print('radiuss:', r)
# else:
#     print('nepareiza ievade')

# Tiek ievadadīts divciparu skaitlis
# samaina vietām ciparus un abus skaitļus
# saskaita. ievada 12, izvada 33




skaitlis1 = int(input("Ievadi divciparu skaitli:"))

if skaitlis1 > 9 and skaitlis1 < 100:
    vieni = skaitlis1 % 10
    desmiti = (skaitlis1 % 100 - skaitlis1 % 10 ) / 10
    skaitlis2 = vieni * 10 + desmiti
    print(skaitlis2 + skaitlis1)
# else:
#     print("Netika ievadīts divciparu skaitlis")

# skaitlis1 = int(input("Ievadi divciparu skaitli:"))

# if skaitlis1 > 9 and skaitlis1 < 100:
#     vieni = skaitlis1 % 10
#     desmiti = (skaitlis1 % 100 - vieni ) / 10
#     if vieni > desmiti:
#         print(vieni)
#     elif desmiti > vieni:
#         print(desmiti)
#     else:
#         print('vienādi')
# else:
#     print("Netika ievadīts divciparu skaitlis")

x = int(input('ievadi x: '))
y = int(input('ievadi y: '))
z = int(input('ievadi z: '))

if x >= y and x >= z: # 3 1 3
    if y >= z:
        print(z, y, x)
    else:
        print(y, z, x)
elif y >= x and y >= z:
    if x >= z:
        print(z, x, y)
    else:
        print(x, z, y)
elif z >= x and z >= y:
    if x >= y:
        print(y, x, z)
    else:
        print(x, y, z)
