# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

# resurss: https://www.programiz.com/python-programming/list

# 46. Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 3) lielāko elementu; 4) visu elementu summu

# for value in arr:
#   if value % 2 != 0:
#     print(value)

# print(sum(arr))
# print(max(arr))

# sv = "Atis Ozols" # ['A', 't', 'i', ..]
# for char in sv:
#   print(char)

# s = [1, 6, 3, 8, 3, 2, 5]

# skaits = s.count(3)
# for i in range(skaits):
#   s.remove(3)

# s.extend([1, 7, 3])
# s += [1, 7, 3]

# 47. Doti divi saraksti. Iegūt sarakstu šķēlumu.

# t = [7, 4, 8, 8, 2, 9, 0]
# s = [1, 6, 3, 8, 3, 2, 5]
# skelums = []

# for t_element in t:
#   for s_element in s:
#     if t_element == s_element:
#       skelums.append(t_element)

# 48. No tiem pašiem sarakstiem iegūt 
# starpību jeb visus elementus no t, kas NAV iekš s.

# for elem in skelums:
#   t.remove(elem)
  
# print(t)

# 49. Dots saraksts, izvadīt to no otra gala.

#    0  1  2  3  4  5  6
# s = [1, 6, 3, 8, 3, 2, 5]

# for elem in s:
#   print(elem)
  
# for i in range(6, -1, -1):
#   print(i, s[i])
# s.reverse()
# print(s)

# 50. Noteikt, vai saraksts ir palindroms. 
#     (No abiem galiem lasās vienādi) 
#     [1, 5, 6, 5, 1] -> Jā
#     [1, 2, 3, 4] -> Nē
#    0  1  2  3  4  5
# s = [1, 5, 6, 5, 1]
# s_copy = []

# ejot caur sarakstu s pretējā virzienā, izveidoju apgrieztu kopiju
# for i in range(len(s) - 1, -1, -1):
#   s_copy.append(s[i])
# s_copy = s.copy()
# s_copy.reverse()

# if s == s_copy:
#   print('ir palindroms') 
# else:
#   print('nav')

# 51. Dots saraksts nums. Lietotājs ievada skaitli, programma 
#     izvada to divu skaitļu _indeksus_, kas summā veido ievadīto skaitli.
#     Piemērs: 8 -> 0, 4; 1, 2;

# #       0  1  2  3  4  5  6 
# nums = [2, 7, 1, 4, 6, 8, 3]

# sum = int(input('ievadi skaitli: '))

# for i in range(7):
#   for j in range(7):
#     print(i, j)
#     if i != j:
#       if nums[i] + nums[j] == sum:
#         print(i, j)
        
# 52. Dotam saraksta noskaidrot mediānu.
    
# #       0  1  2  3  4  5  6 
# nums = [2, 7, 1, 9, 6, 8, 3, 5]
# nums.sort()
# print(nums)

# if len(nums) % 2 == 0:
#   index = int(len(nums)/2)
#   print('mediana: ', (nums[index] + nums[index - 1])/2)  
# else:
#   index = int(len(nums)/2)
#   print('mediana: ', nums[index])


# 53. Ievada skaitli n. Izvadīt tos saraksta elementus, kas mazāki par n.
# nums = [2, 7, 1, 9, 6, 8, 3, 5]

# n = int(input('n: '))
# print('mazaki par n:')

# for elem in nums:
#   print(elem)

# for i in range(len(nums)):
#   print(nums[i])

# for elem in nums:
#   if elem < n:
#     print(elem)

# for i in range(len(nums)):
#   if nums[i] < n:
#     print(nums[i])
    
# 54. Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.

# s = []
# n = int(input('n: '))
# while n != 0:
#   s.append(n) # s.extend([a]) # s += [a]
#   n = int(input('n: '))

# 55. No 1. uzd saraksta izvadīt pēdējos piecus elementus.
# # 1)
# for i in range(len(s) - 1, len(s) - 6, -1): # (sakums, beigas, solis)
#   print(s[i])
# # 2) 
# s.reverse()
# for i in range(5):
#   print(s[i])
# # 3)
# for i in range(1, 6):
#   print(s[-i])
# # 4)
# s.reverse()
# print(s[:5])
  
# 56. Izvadīt no saraksta tos elementus, kas mazāki par 12 un dalās ar 3.

# for elem in s:
#   if elem < 12:
#     if elem % 3 == 0:
#       print(elem)

# 57. Ievada vai sagatavo divus sarakstus garumā 4, kas satur tikai ciparus (0 - 9).
#    Uzrakstīt programmu, kas sarakstus saskaita rakstos

# a = [9, 3, 6, 2]
# b = [2, 4, 5, 1]
# c = []
# carry = 0

# for i in range(3, -1, -1):
#   sum = a[i] + b[i]
#   p = sum % 10
#   c.insert(0, p + carry)
#   carry = sum // 10
  
# if carry:
#   c.insert(0, carry)
  
# print(c)

# SV

# 1P. Saraksts par skaitli. Piemēram, [2, 8, 4] -> 284

# s = [2, 8, 4]
# sum = 0
# for elem in s:
#   sum = sum + elem
#   sum = sum * 10
  
# print(sum // 10)

# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]

# num = 673
# s = []
# while num > 0:
#   p = num % 10
#   num = num // 10

# 2P. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 lielākos pāra skaitļus.

# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.

# 3P. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).
# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

a = [1, 5, 2, 3]
b = [1, 2, 3, 0]

