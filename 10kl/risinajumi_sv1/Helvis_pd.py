#1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37. 


# for i in range(20, 37):
#     if i % 2 == 0:
#         print(i)


#2N. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība







#3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.

# sum = 0

# while True:
#     n = int(input('n: '))
#     if n == 0:
#         break
#     if n % 2 != 0:
#         sum += n

# print(sum)

# 4 Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.

# n = int(input('n: '))

# n = abs(n)

# skaitlis_str = str(n)

# if len(skaitlis_str) < 3:
#     print("nevar izvadīt")
# else:

#     pirmie_tris_cipari = skaitlis_str[:3]
#     sum_vid = sum(int(cipars) for cipars in pirmie_tris_cipari) / 3
#     print("vid:", sum_vid)

# 5 Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

# def ir_pirmskaitlis(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
# n = int(input('n: '))
# if ir_pirmskaitlis(n):

#     sum = sum(int(c) for c in str(n))
#     print("summa:", sum)
# else:

#     skaitlis_str = str(n)
#     max_sk = max(skaitlis_str)
#     print("Lielākais cipars:", max_sk)

