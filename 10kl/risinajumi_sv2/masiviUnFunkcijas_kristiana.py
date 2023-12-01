# arr = {1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3} #Array/List

#

# print('garums/elementu skaits' , len(arr))
# arr.append(7) #pievieno elementu saraksta galā

# arr.pop() #noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā


# sv = "Kristiana Zenina" # { 'A', 't', 'i', ..}
# for char in sv:
#     print(char)

# s = {1, 6, 3, 8, 3, 2, 5}

# skaits = s.count(3)
# for i in range(skaits):
#     s.remove(3)

# s.extend({1, 7, 3})
# s += {1, 7, 3}

# print(s)
# 46. Doti divi saraksti. Iegūt sarakstu šķēlumu.

# t = {7, 4, 8, 2, 9, 0}
# s = {1, 6, 3, 8, 3, 2, 5}
# skelums = {}

# for t_element in t:
#     for s_element in s: 
#         if t_element == s_element:
#             skelums.append(t_element)

# print(list(set(skelums)))

# 47. No tiem pašiem sarakstiem iegūt 
# starpbību jeb visus elementus no t, kas NAV iekš s. 

# for elem in skelums:
#     t.remove(elem)

# print(t)

# Dots saraksts, izvadīt to no otra gala.

#  0  1  2  3  4  5  6 
# s = {1, 6, 3, 8, 3, 2, 5}

# for elem in s:
#     print(elem)

# for i in range(6, -1, -1):
#     print(i, s[i])
# s.reverse()
# print(s)

# 50. Noteikt, vai saraksts ir palindroms.
#  (No abiem galiem lasās vienādi)
#  [1, 5, 6, 5, 1] - > Jā
#  [1, 2, 3, 4] - > Nē

# s = [1, 5, 6, 5, 1]
# s_copy = []

 # ejot caur sarakstu s pretejā virzienā, izveidoju apgrieztu kopiju
# for i in range(len(s) -1, -1, -1):
#     s_copy.append(s[i])
# s_copy = s.copy()
# s_copy .reverse()

# if s == s_copy:
#     print('ir palindroms')
# else:
#     print('nav')

# 51.    Dots saraksts nums. Lietotājs ievada skaitli, programma 
#       izvada to divu skaitļu _indeksus_, kas summā veido ievadīto skaitli.
#       Piemērs: 8 -> 0, 4; 1, 2;

#       0  1  2  3  4  5  6
# nums = [2, 7, 1, 4, 6, 8, 3]

# sum = int(input("ievadi skaitli: "))

# for i in range(7):
#     for j in range(7):
#         print(i, j)
#         if i != j:
#             if nums[i] + nums[j] == sum:
#                 print(i, j)


# 52. Dotam saraksta noskaidrot mediānu. 

#       0  1  2  3  4  5  6
# nums = [2, 7, 1, 4, 6, 8, 3]

# nums.sort()

# index = int(len(nums)/2)
# print('mediana', nums[index])

#       0  1  2  3  4  5  6  7
# nums = [2, 7, 1, 4, 6, 8, 3, 13]
# nums.sort()
# print(nums)

# if len(nums) % 2 == 0: 
#     index = int(len(nums)/2)
#     print('mediana:', (nums[index] + nums[index - 1])/2)
# else:
#     index = int(len(nums)/2)
#     print('mediana: ', nums[index])

#53. Ievada skaitli n. Izvadīt tos saraksta elementus, kas mazaki par n. 
# nums = [2, 7, 1, 9, 6, 8, 3, 5]

# n = int(input("n: "))
# print('mazaki par n: ')

# for elem in nums:
#     if elem < n:
#         print(elem)

# for i in range(len(nums)):
#     if nums[i] < n:
#         print(nums[i])

# vada skaitļus līdz ievada 0.
# 54.  Programma no ievadītajiem skaitļiem izveido sarakstu.

# arr = []
# while True:
#     n = int(input("n: "))
#     if n == 0:
#         break
#     arr.append(n)
#     print(arr)

# 55.  No 1. uzd saraksta izvadīt pēdējos piecus elementus. 

# [5, 6, 1, 2, 4, 3]
# while True:
#     n = int(input("n: "))
#     if n == 0:
#         break
#     arr.append(n)
# arr.reverse()
# print(arr[0:5])

# 56. Izvadīt no saraksta elementus, kas mazāki par 12 un dalās ar 3.
 
# for elem in s:
#     if elem < 12:
#         if elem % 3 == 0:
#             print(elem)

# 57. 

# a = [1, 3, 6, 2]
# b = [2, 4, 5, 1]
# c = []
# carry = 0 

# for i in range(3, -1, -1):
#     sum = a[i] + b[i]
#     p = sum % 10
#     c.insert(0, p + carry)
#     carry = sum // 10

# if carry > 0:
#     c.insert(0,  carry)

# print(c) 

#1P Saraksts par skaitli.

# [3, 9, 7, 4, 5] -> 39745 

# s = [3, 9, 7, 4, 5]
# print(s)

#2P.

# arr = []
# while True:
#      n = int(input("n: "))
#      if n == 0:
#          break
#      arr.append(n)
# print(arr)

# [3, 5, 7, 9, 2, 4]
# while True:
#     n = int(input("n: "))
#     if n == 0:
#          break
#     arr.append(n)
# arr.reverse()
# print(arr[0:2])

#3P.



#4 

a = [1, 5, 2, 3]
b = [1, 2, 3, 0]
c = []
carry = 0