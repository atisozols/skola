
# 1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37. 
# for i in range(19,38):
#     if i % 2 == 0:
#         print(i)

# 2N. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība
# iev= int(input("Ievadi pirmo skatili="))
# sum1=0
# sum2=0
# k = 0
# k1 = 0
# while iev > 0:
#     p = iev % 10
#     sum1 += p
#     iev = iev//10
#     k += 1
# iev2 = int(input("Ievadi otro skaitli="))
# while iev2 > 0:
#     p = iev2 % 10
#     sum2 += p
#     iev2 = iev2//10
#     k1 += 1
# if sum1 / k < sum2 / k1:
#     print("pirmajam skaitlim ir mazāka ciparu summas vidējā vērtība")
# elif sum1 / k > sum2 / k1:
#     print("=otrajam skaitlim ir mazāka ciparu summas vidējā vērtība")
# else:
#     print("abiem ir vienada ciparu summas vidējā vērtība")
# 3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.
# x = int(input("ievadi skaitli"))
# sum = 0
# while x != 0:
#     if x % 2 != 0:
#         sum += x
#     x = int(input("ievadi skaitli"))
# print("summa=",sum)

# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.
# Piemērs: 1326569 -> 132 -> 2.0
# sum = 0
# n = int(input("write n ="))
# k = 0
# while k !=3:
#     p = n % 10
#     sum += p
#     n = n//10
#     k += 1
# c = sum / k
# print(c)
# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu
n = int(input("ieraksti n="))
if n > 0 and n % 1 == 0 and n % n:
    print("pirmskaitlis") 
skaits = 0
n = int(input())
for i in range (1,n + 1):
    if n % i == 0:
        skaits = skaits + 1

if skaits == 2:
    print()
for i in range (0, 33):
    print(i)