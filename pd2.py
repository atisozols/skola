# Izmantojot for ciklu, dilstošā secībā izvadīt visus 
# skaitļus no 20 līdz 0.

# for i in range(20, 0, -1):
#     print(i, end=" ")

# Ievada n. Programma, kas izvada 
# visus pāra skaitļus no n līdz 50.

# n = int(input("ievadi n: "))
# for i in range(n, 51):
#     if i % 2 == 0:
#         print(i, end=" ")

# Ievada n. Programma pieprasa ievadīt n daudzuma skaitļus
# un izvada to vidējo vērtību. Piemēram, ievada 6. Programma
# liek ievadīt sešus skaitļus un izvada to vidējo aritmētisko.

# skaits = int(input("ievadi skaitu: "))
# sum = 0
# for i in range(skaits):
#     n = int(input("ievadi n: "))
#     sum += n
# print(sum/skaits)

# Programma, kas sadala skaitli pa cipariem, pie reizes 
# pasakot ciparu summu.
# Piemēram, tiek ievadīts 1432. Programma
#  izvada 2, 3, 4, 1 un summu 10.

# n = int(input("ievadi n: "))
# sum = 0
# while n > 0:
#     print(int(n % 10))
#     sum += (n % 10)
#     n = (n - (n % 10)) / 10

# print(sum)

# Tiek vadīti skaitļi līdz tiek ievadīta 0. Programma salīdzina
# ievadīto skaitli ar to, kas tika ievadīts pirms tam, pasakot 
# "lielaks par ieprieksejo", "mazaks par ieprieksejo"
# vai "vienadi". Neattiecas uz pirmo ievadīto skaitli.

n = int(input("ievadi n: "))
while n != 0:
    m = n
    n = int(input("ievadi n: "))
    if n == 0:
        break
    if n > m:
        print("lielaks")
    elif n < m:
        print("mazaks")
    else:
        print("vienadi")
    



