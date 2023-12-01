# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]

# Sk = []
# n = int(input("n: "))

# while n != 0:
#   v = n % 10 
#   Sk.append(v)  
#   n = n // 10

# Sk.reverse()
# print(Sk)

# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.    ________________

# SA = []
# n = int(input("n: "))

# while n != 0: 
#   SA.append(n)    
#   n = int(input("n: "))

# SS = []

# for element in SA :      
#     if element % 2 != 0 :
#         SS.append(element)

 
# print(min(SS)[0:3])

# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

# import random
# list = []

# while len(list) < 11 :
#     list.append(random.randint(1, 12))  

# print(list)  


# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

a = [1, 5, 2, 3]
b = [1, 2, 3, 0]
c = []
carry = 0

for i in range(3, -1, -1):  
    sta = a[i] - b[i]
    if a[i] - b[i]:
        carry = -1

    p = sta % 10
    c.insert(0, p - carry)
    carry = sta // 10

if carry:
    c.insert(0, carry)

    print(c)