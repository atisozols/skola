# m = [5, 3, 3, 4, 6, 2, 4, 7]
# # m.append(5) pievieno 5
# # m.pop() 
# # m.remove(4)
# # m.insert(1, 3)
# # len(m) masīva garums
# # m.count(3)

# # masiva izveide
# n = int(input("ievadi n: "))
# m = []
# while n != 0:
#     m.append(n)
#     n = int(input("ievadi n: "))

# # # izvade
# for element in m:
#     if element < 6:
#         print(element, end=" ")
# print()

# min
# m = [5, 3, 3, 4, 6, 2, 4, 7]
# min = m[0]
# for elem in m:
#     if elem < min:
#         min = elem

# # max
# max = m[0]
# for elem in m:
#     if elem > max:
#         max = elem

# # vid
# sum = 0
# for elem in m:
#     sum += elem
# vid = sum/len(m)

# print("min: ", min, "max: ", max, "vid: ", vid)

# numbers = [1, 4, 5, 2, 1]
# for number in numbers:
#     print(number)

# a = [1, 8, 3, 4, 2, 1, 6, 1, 2]

# for j in range(len(a) - 1):
#     for i in range(len(a) - 1):
#         if a[i] > a[i + 1]:
#             temp = a[i]
#             a[i] = a[i + 1]
#             a[i + 1] = temp
#     print(a)

# # Vada skaitļus līdz ievada 0, 
# # izveido masīvu ar skaitļiem.
# m = []
# a = int(input('ievadi skaitli: '))
# while a != 0:
#     m.append(a)
#     a = int(input('ievadi skaitli: '))
# # izvada masīvu

# for elem in m:
#     print(elem, end=' ')
# print()

# # pieprasa vērtību, kuru izņemt

# n = int(input('kuru vertibu iznemt? '))
# count = 0

# for elem in m:
#     if elem == n:
#         count += 1

# for i in range(count):
#     m.remove(n)

# # izvada masīvu

# for elem in m:
#     print(elem, end=' ')

# 1. ievadu skaitļus, kamēr ievadu 0
#    no skaitļiem izveido masīvu

# a = []
# x = int(input('ievadi sk: '))
# while x != 0:
#     a.append(x)
#     x = int(input('ievadi sk: '))

# print(a) # basic izvade

# for elem in a:
#     print(elem, end=" ") # labaka izvade
# print()

# 2. izvada masīva elementu summu un
# vid vērtību

# sum = 0
# for elem in a:
#     sum += elem

# print(sum, sum/len(a))

# 3. no masīva izņem visus pāra skaitļus

# for elem in a:
#     if elem % 2 == 0:
#         a.remove(elem)

# for i in range(len(a)):
#     if a[i] % 2 == 0:
#         a.remove(a[i])


# 4. izvada masīvu

# for elem in a:
#     print(elem, end=" ") # labaka izvade
# print()


# 1. Programma pasaka, kur masīvā 
# atrodas lielākā vērtība

# masiva izveide
# n = int(input("ievadi n: "))
# m = []
# while n != 0:
#     m.append(n)
#     n = int(input("ievadi n: "))

# max = m[0]
# indekss = 0

# for i in range(len(m)):
#     if m[i] > max:
#         max = m[i]
#         indekss = i

# print('lielākā elementa', max, 'indekss ir', indekss)

# # 2. Programma izvada masīva amplitūdu
# # (lielakais - mazakais elements)

# # min
# min = m[0]
# for elem in m:
#     if elem < min:
#         min = elem

# # max
# max = m[0]
# for elem in m:
#     if elem > max:
#         max = elem

# print('amplituda =', max - min)

# 3. Noskaidrot, vai masīvā ir vairāk 
# pāra vai nepāra skaitļi

# para = 0
# nepara = 0

# for elem in m:
#     if elem % 2 == 0:
#         para += 1 # para = para + 1
#     else:
#         nepara += 1

# if para > nepara:
#     print('vairāk pāra skaitļi')
# elif nepara < para:
#     print('vairak nepara skaitli')
# else:
#     print('vienada skaita')


# 4. Dotajam masīvam izveidot spoguļskata
# veida masīvu. 1 4 6 3 -> 1 4 6 3 6 4 1

# # i  0  1  2  3  4  5  6
# m = [1, 4, 6, 3, 5]
# b = m

# for i in range(len(m) - 2, -1, -1):
#     b.append(m[i])

# print(b)

# 5. Programma pasaka, vai masīvs ir augošā
# secībā


# a = [1, 3, 7, 11, 20]
# sakartota = True

# for i in range(len(a) - 1):
#     if a[i] > a[i + 1]:
#         sakartota = False

# if sakartota:
#     print('ir')
# else:
#     print('nav')

# Ievada n. Izņemt no masīva visus n.

# m = [1, 2, 3, 5, 3, 5, 7, 3, 5, 2, 1]

# n = int(input('ievadi n: '))
# skaits = 0
# for elem in m:
#     if elem == n:
#         skaits += 1

# for i in range(skaits):
#     m.remove(n)
# print(m)

# Ja masīvs garāks par 10, tad izvada lielāko 
# elementu un tā biežumu. Citādi izvada vid
# vērtību un to, cik elementi mazāki par vid.

# m = [1, 4, 2, 6, 1]

# if len(m) > 10:
#     max = m[0]
#     for elem in m:
#         if elem > max:
#             max = elem
#     print(max, m.count(max))
# else:
#     sum = 0
#     for elem in m:
#         sum += elem
#     vid = sum/len(m)
#     skaits = 0
#     for elem in m:
#         if elem < vid:
#             skaits += 1
#     print(vid, skaits)

##########################################################################

m = [1, 2, 3, 4]

dd = [[1, 2, 3, 4], 
      [5, 6, 7, 8],
      [9, 10, 11, 12]]

# for row in dd:
#     for elem in row:
#         print(elem, end=" ")
#     print()

for i in range(len(dd)): # rindu skaits
    for j in range(len(dd[i])): # elementu skaits i-tajā rindā
        if (i == 1 and j == 2):
            print(' ', end = " ")
        else:
            print(dd[i][j], end = " ")
    print()