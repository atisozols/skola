# print("hello world!")
# x = 5
# y = 4
# y += 4
# z = x + y
# print(z)

# print("saskaitīšana", x + y)
# print("atņemšana", x - y)
# print("dalīšana", x / y)
# print("reizināšana", x * y)
# print("atlikums", x % y)
# print("kāpināšana", x ** 2)
# print("kvadrātsakne (kāpināšana ar apgrieztu)", x ** 0.5)
# print("dalīšana veselos skaitļos bez atlikuma", x // y)
# print("pārbaudes darbības", x == 4, x != 4, x > 2)

# x = 5
# x = 4

# if x < 2:
#     print("jā")
# else:
#     print("nē")

# if x < 4:
#     print("mazaks par 4")
# else:
#     if x == 4:
#         print("vienads ar 4")
#     else:
#         print("lielaks par 4")

# if x < 4:
#     print("mazaks par 4")
# elif x == 4:
#     print("vienads ar 4")
# else:
#     print("lielaks par 4")

# vards = input("ievadi vardu: ")
# print("Sveiks,",vards)

# x = int(input("ievadi x: ")) # int - Integer - veseli skaitļi
# print(x ** 2)

# 1. Ievada x un ievada y. No lielākā atņem mazāko un izvada starpību!

# x = int(input("ievadi x: "))
# y = int(input("ievadi y: "))
# if x > y:
#     print(x - y)
# else:
#     print(y - x)

# 2. Ievada x. Programma nosaka, vai tas ir pāra vai nepāra.

# x = int(input("ievadi x: "))
# if x % 2 == 0:
#     print(x, "ir pāra")
# else:
#     print(x, "ir nepāra")

# 3. x un y. Programma nosaka, kurā kvadrantā atrodas šis punkts.

# x = int(input("ievadi x: "))
# y = int(input("ievadi y: "))

# if x > 0:
#     if y > 0:
#         print(1)
#     else:
#         print(4)
# else:
#     if y > 0:
#         print(2)
#     else:
#         print(3)

# 4. Saskaitīt trīscipara skaitļa ciparus.

# sk = int(input("trisciparu skaitlis: "))

# if sk > 99 and sk < 1000:
#     v = sk % 10
#     d = ((sk - v) // 10) % 10
#     s = sk // 100
#     print(v + d + s)
# else:
#     print("nav trisciparu")

# 5. Trīs ievadīti skaitļi, programma izvada tos augošā secībā

# x = int(input("ievadi x: "))
# y = int(input("ievadi y: "))
# z = int(input("ievadi z: "))

# if x >= y and x >= z:
#     if y >= z:
#         print(z, y, x)
#     else:
#         print(y, z, x)
# elif y >= x and y >= z:
#     if x >= z:
#         print(z, x, y)
#     else:
#         print(x, z, y)
# else:
#     if x >= y:
#         print(y, x, z)
#     else:
#         print(x, y, z)

# 6. Datuma validācija. Tiek ievadīts mēnesis un 
#    diena. Nosaka, vai šāds datums eksistē

# d = int(input("diena: "))
# m = int(input("mēnesis: "))

# if d > 0 and d < 32 and m > 0 and m < 13:
#     if m == 2 and d < 29:
#         print("ok")
#     elif m == 4 or m == 6 or m == 9 or m == 11:
#         if d < 31:
#             print("ok")
#         else:
#             print("false")
#     elif m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
#         print("ok")
#     else:
#         print("false")
# else:
#     print("invalid input")

# 7. Ievadīti četri skaitļi. No šiem trim skaitļiem 
# saskaitīt tikai pāra skaitļus.

# sum = 0
# for i in range(4):
#   num = int(input("ievadi skaitli: "))
#   if num % 2 == 0:
#     sum += num
    
# print("pāra skaitļu summa:", sum)
    
# 8. Divi skaitļi a, b. Programma aprēķina atbilstošā
#  taisnstūra perimetru un laukumu.

# a = int(input("a: "))
# b = int(input("b: "))

# print("perimetrs:", 2 * (a + b), "laukums:", a * b)

# 9. Divciparu skaitlis. Samainīt vietām skaitļa ciparus
# un saskaitīt ar sākotnējo skaitli. (ievada 15 -> 15 + 51 = 66)

# x = int(input("x: "))
# x_copy = x
# skaitlis = 0
# while x_copy > 0:
#   p = x_copy % 10
#   skaitlis = skaitlis * 10 + p
#   x_copy //= 10
# print(x + skaitlis)

# x = int(input("x:"))
# print(int(x) + int(x[::-1]))

# 10. Programma, kas izvada visus nenegatīvos skaitļus, kas mazāki par 10!

# for i in range(10):
#   print(i)

# for i in range(10): # noklusetais sakuma punkts = 0, galapunkts neieskaitot
#     print(i, "sveiki")

# for i in range(1, 11): # iespēja norādīt sākuma indeksu
#     print(i)

# for i in range(0, 11, 2):
#     print(i)

# for i in range(10, 0, -1):
#     print(i)

# 11. Ievada piecus skaitļus un izvada to summu un vidējo vērtību.

# sum = 0
# for i in range(5):
#     x = int(input("ievadi skaitli: "))
#     sum += x
    
# print(sum, sum/5)

# 12. Lietotājs ievada, cik skaitļi tiks ievadīti,
#     skaitļus ievada, izvada vidējo vērtību.

# sk = int(input("cik skaitļus ievadīsi? "))
# sum = 0

# for i in range(sk):
#     x = int(input("ievadi skaitli: "))
#     sum += x

# print(sum/sk)

# 13. Visi skaitļi no 1 līdz 100, izvada tikai tos, kas dalās ar 3 un 8.

# for i in range(1, 101):
#     if i % 3 == 0 and i % 8 == 0:
#         print(i)

# 14. Programma, kas izvada n x n kvadrātu no "*" simboliem.

# n = int(input("n: "))
# for i in range(n):
#     for i in range(n):
#         print("*", end=" ")
#     print()

# 15. Eglīte no simboliem "*" augstumā n.

# n = int(input("n: "))
# for i in range(n):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
    
# 15.2 Ievada n. Izvadīt n-to nepāra skaitli

# h = int(input("h: "))
# w = -1

# for _ in range(h):
#     w += 2
    
# s = w - h
# b = s + 1
# for i in range(h):
#     for j in range(w):
#         if j >= s and j < b:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     s -= 1
#     b += 1
#     print()
        
# 16. While cikls. Ievadīt skaitļus līdz ievada 0. Izvadīt skaitļu summu.

# sum = 0

# n = int(input("skaitlis: "))
# while n != 0:
#     sum += n # sum = sum + n
#     n = int(input("skaitlis: "))

# print(sum)

# 17. Izvadīt visus skaitļus no 1 līdz n. Izmantot while ciklu

# n = int(input("skaitlis: "))
# i = 0
# while i < n:
#     i += 1
#     print(i)


# n = int(input("skaitlis: "))
# for i in range(1, n + 1):
#     print(i)


# 18. Programma, kas izvada pirmos n kvadrātus! (1, 4, 9, 36...)

# n = int(input("ievadi n: "))
# for i in range(1, n + 1):
#     print(i ** 2)

# 19. Programma, kas izvada visus kvadrātus, kas mazāki par n.

# n = int(input("ievadi n: "))
# i = 1
# while i ** 2 < n:
#     print(i ** 2)
#     i += 1

# 20. Ievada n. Programma, kas izvada visus skaitļus no n līdz 2n.

# n = int(input("n: "))
# for i in range(n, n * 2):
#     print(i)

# 21. Programma, kas saskaita visus skaitļus no 1 līdz 100.


# sum = 0
# for i in range(1, 101):
#     sum += i
    
# print(sum)

# 22. Izvadīt visus nepāra skaitļus dilstošā secībā no 25 līdz 1.

# for i in range(25, 0, -2): # sakums, beigas neieskaitot, solis
#     print(i)

# for i in range(25, 0, -1): # sakums, beigas neieskaitot, solis
#     if i % 2 != 0:
#         print(i)

# 23. Izmantojot ciklu, izveidot programmu, kas liek ievadīt piecus skaitļus
# un izvada to summu.

# sum = 0
# for i in range(5):
#     sk = int(input("skaitlis: "))
#     sum += sk
# print(sum)

# 24. Vada skaitļus, kamēr ievada nulli. izvadīta skaitļu summa.

# sum = 0
# sk = int(input("skaitlis: "))
# while sk != 0:
#     sum += sk
#     sk = int(input("skaitlis: "))
    
# print(sum)

# 25. Patvaļīga lieluma skaitlim aprēķināt ciparu summu.

# 7452 -> 2 --> 745 -> 5 --> 74 -> 4 --> 7 -> 7

# sk= int(input("sk: "))
# sum = 0

# while sk > 0:
#     ped = sk % 10
#     sum += ped # sum = sum + ped
#     sk = sk // 10 # dalit ar 10 veselos skaitlos -> 745 // 10 = 74
    
# print(sum)

# 26. Ievadītam skaitlim aprēķināt dalītāju skaitu. Noteikt, vai skaitlis ir pirmskaitlis.

# sk= int(input("sk: "))
# dalSk = 0

# for i in range(1, sk + 1): # [1..n]
#     if sk % i == 0:
#         dalSk += 1
# print(dalSk)

# if dalSk == 2:
#     print('pirmskaitlis')

# sk= int(input("sk: "))
# dalSk = 0

# for i in range(2, sk):
#     if sk % i == 0:
#         dalSk += 1
#         print('nav pirmskaitlis')
#         break

# if dalSk == 0:
#     print('pirmskaitlis')

# 27. Vadam skaitļus līdz ievadam nulli. 
#     Programma pasaka par katru nākošo, vai 
#     tas ir lielāks vai mazāks par iepriekšējo.

# n = int(input("skaitlis: "))
# m = int(input("skaitlis: "))
# while n != 0 and m != 0:
#     if m > n:
#         print("lielāks")
#     else:
#         print("nav lielāks")
#     n = m
#     m = int(input("skaitlis: "))

# 28. Vada skaitļus, kamēr ievada 0. Aprēķināt 
#     vidējo, maksimālo un minimālo vērtību.

# n = int(input("skaitlis: "))
# max = n
# min = n
# sum = 0
# skaits = 0
# while n != 0:
#     if n > max:
#         max = n
#     if n < min:
#         min = n
#     skaits += 1
#     sum += n
#     n = int(input("skaitlis: "))

# print("vid:", sum/skaits)
# print("max:", max)
# print("min:", min)

# 29. Vada skaitļus, kamēr ievada 0. Atrast modu.

# n = int(input("skaitlis: "))
# m = []
# while n != 0:
#     m.append(n)
#     n = int(input("skaitlis: "))

# print(m)

# 30. Klasē ir septiņi skolēni. Nepieciešams 
#     katram ievadīt atzīmes, kas var būt patvaļīgā skaitā.
#     Programma katram skolēnam izvada vidējo atzīmi.

# for i in range(1, 8):
#     n = int(input("atzīme: "))
#     sum = 0
#     skaits = 0
#     while n != 0:
#         skaits += 1
#         sum += n
#         n = int(input("atzīme: "))
#     print(i, "skolēna vidējā atzīme:", sum/skaits)

# for i in range(1, 8):
#     skaits = int(input("cik atzīmes ir skolēnam nr." + str(i) + "?"))
#     sum = 0
#     for j in range(skaits):
#         atz = int(input("atzīme: "))
#         sum += atz
#     print("vid. atzīme: " + str(sum/skaits))
    

    