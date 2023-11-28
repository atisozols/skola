# a = int(input("ievadi a: ")) # int - integer - vesels skaitlis
# print(a)
# print(a + 5)
# print(a - 1)
# print(a * 3)
# print(a / 2)
# print(a // 2) # dala bez atlikuma 5 // 2 = 2
# print(a % 2) # dalam, iegustot tikai atlikumu 5 % 2 = 1
# print(a ** 2) # kapinasana
# print(a ** 0.5) # kvadratsakne

# 15. Tiek ievadīts skaitlis. Programma nosaka, vai tas ir pozitīvs.

# a = int(input("ievadi a: "))

# if a > 0:
#   print("a ir pozitīvs")
# else:
#   if a == 0:
#     print("a nav ne poz, ne neg")
#   else:
#     print("a ir negatīvs")
    
# if a > 0:
#   print("a ir pozitīvs")
# elif a == 0:
#   print("a nav ne poz, ne neg")
# else:
#   print("a ir negatīvs")

# 16. Ievada trīs vērtības. Programma nosaka trijstūra eksistenci, 
#     ja šīs vērtības ir trijstūra malas

# a = int(input("ievadi a: "))
# b = int(input("ievadi b: "))
# c = int(input("ievadi c: "))

# if a + b > c:
#   if a + c > b:
#     if b + c > a:
#       print("eksistē")
#     else:
#       print("neeksistē")
#   else:
#     print("neeksistē")
# else:
#   print("neeksistē")

# if a + b > c and a + c > b and b + c > a:
#   print("eksistē")
# else:
#   print("neeksistē")  
  
# 17. Ievada dienas numuru (1 - 7), programma pasaka:
#     1) darba diena vai brivdiena
#     2) pasaka dienas nosaukumu (1 -> pirmdiena)

# d = int(input("diena: "))

# # 1)
# if d < 6:
#   print("darba diena")
# elif d < 8:
#   print("brivdiena")
# # 2)
# if d == 1:
#   print("pirmdiena")
# elif d == 2:
#   print("otrdiena")
# elif d == 3:
#   print("tresdiena")
# elif d == 4:
#   print("ceturtdiena")
# elif d == 5:
#   print("piektdiena")
# elif d == 6:
#   print("sestdiena")
# elif d == 7:
#   print("svetdiena")
  
# 18. Noteikt, vai ievadītais skaitlis ir pāra vai nepāra.

# x = int(input("skaitlis: "))
# if x % 2 == 0:
#   print("skaitlis ir para")
# else:
#   print("skaitlis ir nepāra")

# 19. Ievadīti divi skaitļi. No tiem izvadīt lielāko.

# x = int(input("skaitlis x: "))
# y = int(input("skaitlis y: "))

# if x > y:
#   print(x)
# elif x == y:
#   print("vienādi")
# else:
#   print(y)

# 20. Ievadīti trīs skaitļi. No tiem izvadīt lielāko.
 
# x = int(input("skaitlis x: "))
# y = int(input("skaitlis y: "))
# z = int(input("skaitlis z: "))

# if x >= y and x >= z:
#   print(x)
# elif y >= x and y >= z:
#   print(y)
# elif z >= x and z >= y:
#   print(z)

# 21. Trīs skaitļi. Izvadīt kvadrātvienādojuma saknes, ja šie skaitļi ir koeficienti a, b, c

# a = int(input("skaitlis a: "))
# b = int(input("skaitlis b: "))
# c = int(input("skaitlis c: "))

# d = b ** 2 - 4 * a * c

# if d < 0:
#   print("saknes nav")
  
# elif d == 0:
#   print(-b/(2*a))
  
# else:
#   print((-b + d ** 0.5)/(2 * a))
#   print((-b - d ** 0.5)/(2 * a))
  
# if a > 0:
#   print("zari uz augsu")
# else:
#   print("zari uz leju")
  
# x0 = -b/(2*a)
# y0 = a * x0 ** 2 + b * x0 + c

# print(x0, y0)

# 22. Ievada skaitli. Noteikt mazāko iespējamo nominālu vērtību un skaitu, lai iegūtu ievadīto skaitli.

# 238
# 1 200
# 1 20
# 1 10
# 1 5
# 1 2
# 1 1

# % //

# n = int(input("summa: "))

# b500 = n // 500
# if b500 > 0:
#   print(500, b500)
#   n = n - b500 * 500
  
# b200 = n // 200
# if b200 > 0:
#   print(200, b200)
#   n = n - b200 * 200
  
# b100 = n // 100
# if b100 > 0:
#   print(100, b100)
#   n = n - b100 * 100
  
# ...

# b1 = n // 1
# if b1 > 0:
#   print(1, b1)
  
# Cikls ar skaitītāju - for

# for i in range(10):
#   print(i, "sveiki")

# for i in range(2, 10, 2): # (sakuma, beiguNeieskaitot, solis)
#   print(i)

# for i in range(10, -1, -1): # dilstosa seciba no 10 lidz 0
#   print(i)

# 23. Tiek ievadīts n. Programma izvada visus skaitļus no 1 līdz n ieskaitot.
# 4 -> 1 2 3 4

# n = int(input("n: "))

# for i in range(1, n + 1):
#   print(i)
  
# 24. Tiek ievadīts n. Programma izvada visus skaitļu no 1 līdz n kvadrāti.
# 4 -> 1 4 9 16

# n = int(input("n: "))

# for i in range(1, n + 1):
#   print(i ** 2)

# 25. Tiek ievadīts n. Iegūt un izvadīt visu skaitļu no 1 līdz n summu.

# n = int(input("n: "))
# summa = 0
# for i in range(1, n + 1):
#   summa = summa + i
#   print(i, summa)
  
# 26. Tiek ievadīts n. Programma izvada visus n dalītājus.

# n = int(input("n: "))
# for i in range(1, n + 1):
#   if n % i == 0:
#     print(i)
#   else:
#     print("nedalās ar ", i)
 
# 27. Ievada a un b. Izvada visus skaitļus no b līdz a dilstošā secībā.

# a = int(input("a: "))
# b = int(input("b: "))

# for i in range(b, a-1, -1):
#   print(i)
  
# 28. Programma liek ievadīt 7 skaitļus. Izvada skaitļu summu.

# summa = 0
# for i in range(7):
#   x = int(input('x: '))
#   summa = summa + x # summa += x
  
# print(summa)

# 29. Ievada 5 skaitļus. Programma izvada lielāko no ievadītajiem.

# max = 0
# for i in range(5):
#   x = int(input('x: '))
#   if x > max:
#     max = x
    
# print(max)

# max = 0
# for i in range(5):
#   x = int(input('x: '))
#   if x > max:
#     max = x
#   print('tika ievadits:', x, 'lidz sim lielaka vertiba:', max)
 
# 30. Ievada 5 skaitļus. Programma izvada mazāko no ievadītajiem.

# min = int(input('x: '))
# for i in range(4):
#   x = int(input('x: '))
#   if x < min:
#     min = x
    
# print(max)

# 31. Ievada n. Izvada n faktoriālu (n!)

# n = int(input("n: "))
# faktor = 1
# for i in range(1, n + 1):
#   faktor = faktor * i
#   print(i, faktor)


# print(fak)

# 32. Ievada n. Noteikt, vai n ir pirmskaitlis. (#25; #26)

# 13 // 5 = 2
# 13 % 5 = 3

# skaits = 0
# n = int(input('n: '))
# for i in range(1, n + 1):
#   print(n, '%', i, '=', n % i)
#   if n % i == 0:
#     skaits = skaits + 1 # skaits += 1
       
# if skaits == 2:
#   print(n, "ir pirmskaitlis")
# else:
#   print(n, "nav pirmskaitlis")

# 33. Programma, kas neprasa ievadīt skaitļus un izvada visus naturālus skaitļus no 1 līdz 32.

# 34. Tiek ievadīts n. Programma, kas izvada visus skaitļus no 1 līdz n, kas nedalās ar 4.

# n = int(input("n: "))
# for i in range(1, n + 1):
#   if i % 4:
#     print(i)

# 35. Programma liek ievadīt skaitli (jūsu datora nr) reizes un izvada visu ievadīto skaitļu summu.
    
# while cikls

# n = 1
# while n < 11:
#   print(n)
#   n = n * 2
  
# 36. Ievada skaitļus līdz tiek ievadīta 0. 
# Ievadītos skaitļus saskaita un izvada summu.

# sum = 0
# n = int(input("n pirmoreiz: "))
# while n != 0:
#   sum += n
#   n = int(input("n: "))
  
# print(sum)

# 37. Ievada skaitli. Programma izvada skaitļa ciparu summu.

# sum = 0
# n = int(input("n: "))
# while n > 0:
#   p = n % 10
#   print(p)
#   sum += p
#   n = n // 10
# print(sum)

# 38. Tiek vadīti skaitļi līdz ievada 0. 
# Programma nemitīgi pasaka, vai ievadītais 
# skaitlis ir lielāks par iepriekš ievadīto.

# x = int(input("sk: "))
# while x != 0:
#   y = int(input("sk: "))
#   print(x, y)
#   if x > y:
#     print("mazaks")
#   elif x == y:
#     print("vienads")
#   else:
#     print("lielaks")
#   x = y

# *1. Eglīte augstumā n.

# n = int(input('n: '))
# for i in range(1, n + 1):
#   for j in range(1, i + 1):
#     print(i, end='')
#   print()

# for i in range(1, n + 1):
#   for j in range(1, n + 1):
#     print(i, j)

# 39. Vada skaitļus līdz tiek ievadīta 0. Programma izvada lielāko no ievadītajiem.

# max = 0
# n = int(input('n: '))
# while n != 0:
#   if n > max:
#     max = n
#   n = int(input('n: '))
  
# print(max)

# 40. Ievadītam skaitlim atrast lielāko ciparu pēc vērtības. (483 -> 8)

# max = 0
# n = int(input("n: "))
# while n > 0:
#   pedejais_cipars = n % 10 
#   if pedejais_cipars > max:
#      max = pedejais_cipars
#   n = n // 10 
# print(max)

# 41. Vada skaitļus līdz tiek ievadīta 0. Programma izvada vidējo vērtību.

# skaits = 0
# sum = 0
# n = int(input("n: "))
# while n != 0:
#   sum += n
#   skaits += 1
#   n = int(input("n: "))
  
# print(sum/skaits)

# import random

# # 1 - akmens, 2 - skeres, 3 - papirs
# play = 0
# while play == 0:
#   streak = 0

#   while True:
#     mansGajiens = int(input('1 - akmens, 2 - skeres, 3 - papirs: '))
#     compGajiens = random.randint(1, 3)

#     if mansGajiens - compGajiens == 1:
#       break
#     elif compGajiens - mansGajiens == 1:
#       streak = streak + 1
#       print('bang')
#     elif mansGajiens == 1 and compGajiens == 3:
#       break
#     elif mansGajiens == 3 and compGajiens == 1:
#       streak += 1
#       print('bang')
#     elif mansGajiens == compGajiens:
#       print('neizskirts')
      
#   print('tu zaudeji, tavs streak: ', streak)
#   play = int(input('ja velies spelet velreiz, ievadi 0: '))

import random

# 43. Programma, kas uzģenerē skaitli un ļauj lietotājam minēt, kamēr tas uzmin

# s = random.randint(1, 10)
# n = int(input('minejums: '))

# while n != s:
#   n = int(input('minejums: '))
  
# print('uzmineji!', s)

# 43.1 Pievienot funkcionalitāti, kas uzskaita, ar cik minējumiem uzminēja

# s = random.randint(1, 10)
# n = int(input('minejums: '))
# minejumuSkaits = 1

# while n != s:
#   minejumuSkaits += 1
#   n = int(input('minejums: '))
  
  
# print('uzmineji ar', minejumuSkaits, 'meginajumiem')

# 43.2 Pēc katra nepareiza minējuma programma 
#      iedod hint, kurā virzienā ir pareizā atbilde


# s = random.randint(1, 10000)
# n = int(input('minejums: '))
# minejumuSkaits = 1

# while n != s:
#   if n > s:
#     print('mazak')
#   else:
#     print('vairak')
#   n = int(input('minejums: '))
#   minejumuSkaits += 1
  
  
# print('uzmineji ar', minejumuSkaits, 'meginajumiem')

# 44. Ievadītam skaitlim noteikt, vai tam piemīt
#     vairāk pāra skaitļa dalītāji vai nepāra

# 12 - 1, 2, 3, 4, 6, 12 --> pāra

# n = int(input('n: '))
# neparaDalitajuSk = 0
# paraDalitajuSk = 0

# for i in range(1, n + 1):
#   if n % i == 0:
#     if i % 2 == 0:
#       paraDalitajuSk += 1
#     else:
#       neparaDalitajuSk += 1

# if paraDalitajuSk > neparaDalitajuSk:
#   print('pāra dalītāji ir vairāk')
# elif paraDalitajuSk < neparaDalitajuSk:
#   print('nepāra dalītāji ir vairāk')
# else:
#   print('vienādi')
  
# 45. Izvadīt visus skaitļus no 1 līdz 1000, kuriem nepāra skaitļa dalītāji vienādi ar pāra

# for n in range(1, 1001):
#   neparaDalitajuSk = 0
#   paraDalitajuSk = 0
#   neparaDalitaji = []
#   paraDalitaji = []

#   for i in range(1, n + 1):
#     if n % i == 0:
#       if i % 2 == 0:
#         paraDalitajuSk += 1
#         paraDalitaji.append(i)
#       else:
#         neparaDalitajuSk += 1
#         neparaDalitaji.append(i)

#   if paraDalitajuSk == neparaDalitajuSk:
#     print(n, paraDalitaji, neparaDalitaji)