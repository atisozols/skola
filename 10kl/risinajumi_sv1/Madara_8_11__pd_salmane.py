# 1. uzdevums 

# for i in range(-1, -11, -1):
#     print(i)

# 2. uzdevums

# sum = 0 
# x = int(input("pirmais skaitlis:"))
# while x > 0:
#     p = x % 10
#     sum += p
#     x = x // 10 

# sum1 = 0
# y = int(input("otrais skaitlis:"))
# while y > 0:
#     o = y % 10
#     sum1 += o
#     y = y // 10

# if sum > sum1:
#     print("pirmais")
# if sum1 > sum:
#     print("otrais")
# if sum == sum1:
#     print("vienadi")

# 3. uzdevums

# l = 0
# n = int(input("skaitlis:"))
# while(n!=0):
#     n = int(input("skaitlis:"))
#     if n % 2 == 0:
#         l += n
#     if l > n:
#         print(l)

# 4. uzdevums

# s = int(input("skaitlis"))

# 5. uzdevums

# sum = 0
# skaits = 0
# para = 0
# nepara = 0
# pedejais = 0
# q = int(input("q skaitlis: "))
# for i in range(1, q+1):
#     if q%i==0 : 
#        skaits = skaits +1
# if skaits == 2 :
#     para == q
#     print(q, "pirmskaitlis")
#     while q>0: 
#         p = q % 10
#         sum += p
#         q = q // 10 
#     print("skaitļa summa:", sum)
# else: 
#     nepara == q
#     print(q, "nav pirmskaitlis")
#     while q>0: 
#         p = q % 10
#         sum += p
#         q = q // 10 
#         print(sum)