# 1P. Saraksts par skaitli. Piemēram, [2, 8, 4] -> 284


# arr = [2, 8, 4]
# sum = 0
# for elem in arr:
#     sum += elem
#     sum = sum * 10
# print(sum // 10)
 




# 2P. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 lielākos pāra skaitļus.


# list = []

# max = 0
# max2 = 0
# max3 = 0

# n = int(input('n: '))
# while n !=0 :
#     list.append(n)
#     n = int(input('n: '))

# list.sort()
# list.reverse()
# print(list)
# print('Lielākie skaitļi ir:', list[0:3])


# 3P. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).

# import random
# sar = []
# for i in range(10):
#   a = random.randint(1, 30)
#   while a % 2 == 0:
#    a = random.randint(1, 30)
#   sar.append(a)
#   print(sar)


# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.
# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c = []
# carry = 0

# for i in range(3, -1, -1):    
#     sum = a[i] - b[i]         
#     p = sum % 10
#     c.insert(0, p - carry)     
#     carry = sum // 10   
# if carry > 0:
#     c.insert(0, carry)
# print(c)


    