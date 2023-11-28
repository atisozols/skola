# for / while

# Ievada n, izvadīt visus skaitļus no 0 līdz n.

# n = int(input('ievadi n: '))
# for i in range(n+1):
#     print(i)

# i = 0
# while i <= n:
#     print(i)
#     i += 1

# Ievada n, aprēķināt n faktoriālu.

# n = int(input('n: '))
# faktorials = 1
# for i in range(1, n+1):
#     faktorials *= i # faktorials = faktorials * i
# print(faktorials)

# faktorials = 1
# while n > 0:
#     faktorials *= n
#     n -= 1
# print(faktorials)

# Programma liek ievadīt piecus skaitļus un izvada 
# vidējo aritmētisko. Izmantot ciklu.

# sum = 0
# for i in range(5):
#     x = int(input('ievadi ' + str(i + 1) + '. skaitli '))
#     sum += x
# print(sum/5)

# Vada skaitļus līdz tiek ievadīta 0. Programma 
# izvada ievadīto skaitļu vidējo aritmētisko.

# i = 0
# x = int(input('ievadi ' + str(i + 1) + '. skaitli '))
# sum = 0

# while x != 0:
#     i += 1
#     sum += x
#     x = int(input('ievadi ' + str(i + 1) + '. skaitli '))

# print('videja vertiba no', i, 'skaitliem =', sum/i)

# import math
# print(int(sum/i))
# print(round(sum/i))
# print(math.floor(sum/i)) # int(sum/i)
# print(math.ceil(sum/i))

# Lietotājs ievada n. Izveidot n x n reizināšanas tabulu.\

n = int(input('n: '))
for i in range(n):
    for j in range(i):
        print("0", end=" ")
    print()