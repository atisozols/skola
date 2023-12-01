# 1P. [2, 8, 4] -> 284
# arr = [5,1,8]
# for i in arr:
#     print(i)

# 2P UZDEVUMS

# s = []
# n = int(input("skaitlis n:"))
# s.extend([n])
# while n != 0:
#      n = int(input("skaitlis n:"))
#      s.extend([n])
# print(s)

# p = []
# for i in s:
#     if i % 2 == 0:
#          p.insert(0,i)

# print(p)
# for i in range(1, 4):
#     print(p[i])

# 3P UZDEVUMS 

import random
i = random.randint(1, 30)
arr = []
a = 0
# for i in range(10):
#     if i % 2 != 0:
#         arr.extend([i])
while a == 0:
    if i % 2 != 0 :
        arr.extend([i])
        if len(arr) == 10:
            a = 1
print(arr)

# 4. UZDEVUMS 

# a = [8,9,6,4]
# b = [2,4,1,7]
# c = []
# for i in range(3, -1, -1):
#     sum = a[i] - b[i]
#     if sum < 0:
#         p = sum % 10
#         c.insert(0,p)
#         carry = -1
#     else:
#         c.insert(0, sum + carry)
#         carry = 0
# if carry > 0:
#     c.insert(0, carry)
# print(c)