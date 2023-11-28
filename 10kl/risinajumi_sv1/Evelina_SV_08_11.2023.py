# 1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37.

# for i in range (20, 37) :
#     if i % 2 == 0 :
#         print (i)

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība

# sum1 = 0
# sum2 = 0
# skaits1 = 0
# skaits2 = 0
# n = int(input("n: "))
# v = int(input("v: "))

# while n > 0:
#     p = n % 10
#     sum1 += p
#     skaits1 += 1
#     n = n // 10
#     a = sum1 / skaits1

#     o = v % 10
#     sum2 += o
#     skaits2 += 1
#     v = v // 10
#     b = sum2 / skaits2

#     if a > b :
#       print ('b', b)
#     else :
#        print ('a', a)

# 3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.

# sum = 0
# n = int(input("n: "))

# while n != 0 :
#     if n % 2 == 1 :
#        sum += n
#     n = int(input("n: "))
    
# print (sum)

# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.

sum = 0
skaits = 0
n = int(input("n: "))
while n != 0 :
   
   p = n % 10
   sum += p
   skaits += 1
   n = n // 10
   if skaits == 3 :
    a = sum // 3

    print (a)

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

# skaits = 0
# sum = 0
# n = int(input("n: "))

# for i in range(1, n + 1) :
#     if n % i == 0:
#         skaits = skaits + 1
#         if skaits == 2 :
#             p = n % 10
#             sum += p
#             n = n // 10
#             print (sum)


