#  1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]
# c = []
# n = 637
# while n > 0:
#     p = n % 10
#     n = n//10
#     c.append(p)
# c.reverse
# print(c)
# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.
# s = []
# c=[]
# a = int(input("input number="))
# while a != 0:
#     s.append(a)
#     a = int(input("input number="))

# for i in s:
#     if i % 2 != 0:
#         c.append(i)
# c.sort
# print(c[0],c[1],c[2])
# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).
# import random
# c = []
# d=0
# for i in range(0,10):
#     d = random.randint(0,13)
#     c.append(d)
# print(c)
# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c=[]
# carry=0

# for i in range(3, -1, -1):
#     sum = a[i] - b[i]

#     c.insert(0,sum+carry)
# print(c)

