arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print(arr[2])

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

# resurss: https://www.programiz.com/python-programming/list

# Uzdevums: Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 3) lielāko elementu; 4) visu elementu summu

# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for element in arr:
#     print(element)

# for element in arr:
#     if element % 2 != 0:
#         print(element) 

# sv = "Lizete Oseniece"
# for char in sv:
#     print(char)


# s = [1, 6, 3, 8, 3, 2, 5]

# skaits = s.count(3)
# for i in range(skaits):
#   s.remove(3)


# print(s)

# s.extend([1, 7, 3])

# print(s)

# t = [7, 4, 8, 2, 9, 0]
# s = [1, 6, 3, 8, 3, 2, 5]
# skelums = []

# for t_element in t:
#     for s_element in s: 
#         if t_element == s_element:
#             skelums.append(t_element)

# print(list(set(skelums)))

# t = [7, 4, 8, 2, 9, 0]
# s = [1, 6, 3, 8, 3, 2, 5]
# skelums = []

# s = [1, 6, 3, 8, 3, 2, 5]

# for i in range(6, -1, -1):
#   print(i,s[i])

# s = [1, 5, 6, 5, 1]
# s_copy = []

# for i in range(len(s)-1, -1, -1):
#     s_copy.append(s[i])

# if s == s_copy:
#     print("ir palinoms")
# else:
#     print("nav")

# print(s, s_copy)


# nums = [2, 7, 1, 4, 6, 8, 3]

# sum = int(input("ievadi skaitli: "))

# for i in range(7):
#     for j in range(7):
#          if i != j:   
#              if nums[i] + nums[j] == sum:
#                  print(i, j)


# nums = [2, 7, 1, 4, 9, 6, 8, 3]
# nums.sort()


# index = int(len(nums)/2)
# print("mediana: ", (nums[index] + nums [index - 1])/ 2)



# Ievada skaitli n. Izvadīt tos saraksta elementus, kas mazāki pat n.
# nums = [2, 7, 1, 9, 6, 8, 3, 5]

# n= int(input("n: "))
# print("mazāki par n: ")

# for elem in nums:
#     if elem < n:
#      print(elem)


# for i in range(len(nums)):
#    print(nums[i])


# Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.

# arr = []
# n = int(input("n: "))
# while n != 0:
#     arr. append(n)
#     n = int(input("n: "))
# print(arr)


# No 1. uzd saraksta izvadīt pēdējos piecus elementus.

# list = []
# n = int(input("n: "))
# while n != 0:
#     list. append(n)
#     n = int(input("n: "))
# list.reverse()
# print(list[0:5])


# for i in range 

# pd nepara

# 1.
# def create_list_func(number):
#     arr = []
#     for digit in str(number):
#         arr.append(int(digit))
# return arr

# print(create_list_func(456))

# 2
# n = int(input("n: "))
# while n != 0:
#     for elem in n:
#         if elem < n:
#             print(elem)

# 3

# import random
# a = random (1, 12)
# print

# import random


# def gen_random_numbers_in_range(low, high, n):

#      print(gen_random_numbers_in_range(1, 12, 10))



# 4

# lista =[1, 5, 2, 3]
# listb = [1, 2, 3, 0]

# seta = set(lista)
# setb = set(listb)

# sarakstsc = seta - setb
# print(sarakstsc)