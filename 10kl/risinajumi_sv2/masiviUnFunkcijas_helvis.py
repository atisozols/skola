# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print(arr[2])

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

# resurss: https://www.programiz.com/python-programming/list

# Uzdevums: Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 
#3) lielāko elementu; 4) visu elementu summu

# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for skaitlis in arr:
#     if skaitlis % 2 == 0:
#         print(skaitlis)
    

# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for skaitlis in arr:
#     if skaitlis % 2 != 0:
#         print(skaitlis)


# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for skaitlis in arr:
#     lielākais = max(arr)
# print(lielākais)


# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# summa = sum(arr)
# print(summa)


# sv = 'Pelmenis'    # [P; e; l; m; ...]
# for char in sv:
#     print(char)


# s = [1, 6, 3, 2, 8, 9, 5, 3]

 # skaits = s.count(3)
 # for i in range(skaits):
 #     s.remove(3)

# s.extend([1, 7, 3])

# print(s)


# 46. doti divi saraksti. iegūt sarakstu sķēlumu

# t = [7, 4, 8, 2, 9, 0]
# s = [1, 6, 3, 8, 3, 2, 5]
# skelums = []
# for t_element in t:
#    for s_element in s:
#       if t_element == s_element:
#              print(t_element)

#  47. no tiem pašiem sarakstiem iegūt starpību
#  jeb visus elementus no T kas NAV iekš s

# t = [7, 4, 8, 8, 2, 9, 0] 
# s = [1, 6, 3, 8, 3, 2, 5]

# for elem in skelums:
#     t.remove(t)
# print(t)


# 48. dots saraksts izvadīt to no otra gala

# s = [1, 6, 3, 8, 3, 2, 5]

# # for i in range (6, -1, -1):
# #     print(i, s[i])

# s.reverse()
# print(s)

# 50. noteikt vai saraksts ir palindroms. 
#        (no abiem galiem lasās vienādi)
#[1, 5, 6, 5, 1] -> jā
#[1, 2, 3, 4,] -> nē

# s = [1, 5, 6, 5, 1]
# s_copy = []

# for i in range(len(s)-1, -1, -1):
#     s_copy.append(s[i])

# if s == s_copy:
#     print('ir polindroms')

# else:
#     print('nav polindroms')



# 51. dots saraksts nums. lielotājs ievada skaitli, programma 
# izvada to divu skaitļu _indeksus_ kas summā veido ievadīto skaitli.

# nums = [2, 7, 2, 4, 6, 8, 3]

# sum = int(input('skaitlis: '))

# for i in range(7):
#     for j  in range(7):
#         if j != i:
#             if nums[i] + nums[j] == sum:
#                 print(i, j)
    
# 52. dotam sarakstam noskaidrot mediānu
            

# nums = [2, 7, 2, 4, 6, 8, 3]
# nums.sort()

# index = (int(len(nums)/2))
# print('mediana: ', nums[index])


# nums = [2, 7, 1, 9, 6, 8, 3, 13]
# nums.sort()

# if len(nums) % 2 == 0:
#     index = int(len(nums)/2)
#     print('mediana: ', (nums[index] + nums[index - 1])/2) 
# else:
#     index = (int(len(nums)/2))
#     print('mediana: ', nums[index])


# 53. ievadi skaitli n. izvadīt tos saraksta elementus, 
# kas mazāki par n


# nums = [2, 7, 1, 9, 6, 8, 3, 5]

# n = int(input('n: '))
# print('mazāki par n: ')

# for elem in nums:
#     if elem < n:
#         print(elem)

# for i in range(len(nums)):
#     if nums[i] < n:
        
#         print(nums[i])


#Formatīvais vertējums

#1. Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.


# masivs = []

# while True:
#     

# 2. No 1. uzd saraksta izvadīt pēdējos piecus elementus.[2, 3, 4, 5, 3, 2, 1, 12, 3]

# masivs = []

# while True:
#      n = int(input('skaitlis: '))
#      if n == 0:
#          break
#      masivs.append(n)
# masivs.reverse()

# print(masivs[0:5])

# 3. Izvadīt no saraksta tos elementus, kas mazāki par 12 un dalās ar 3.

# nums = [2, 6, 4, 9, 3, 2, 1, 12,]

# for elem in nums:
#     if elem < 12 and elem % 3 == 0:
#         print(elem)
        
 
# 4. Ievada vai sagatavo divus sarakstus garumā 4, kas satur tikai ciparus (0 - 9).
#    Uzrakstīt programmu, kas sarakstus saskaita rakstos

# a = [1, 3, 6, 2]
# b = [2, 4, 1, 1]
# c = []

# for i in range (3, -1, -1):
#     sum = a[i] + b[i]
#     if sum > 9:
#         p = sum % 10
#         c.insert(0,p)
#         carry = 1
#     else:
#         c.insert(0, sum + carry)
#         carry = 0
       
# print(c)


#Pārbaudes darbs

#1.Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]


# n = int(input("n: "))

# skaitli = [int(skaitlis) for skaitlis in str(n)]
# print(skaitli)


#2. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.
    
 
# skaitli = []

# while True:
#     n = int(input('n: '))
#     if n == 0:
#         break
#     skaitli.append(n)
# nepāra_sk = [num for num in skaitli if num % 2 != 0]
# sakartoti_nepara = sorted(nepāra_sk)[:3]
# print([sakartoti_nepara])

#3. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

# import random

# skaitli = []

# while len(skaitli) < 10:
#     random_number = random.randint(1, 12)
#     if random_number not in skaitli:
#          skaitli.append(random_number)

# print(skaitli)

#4.Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c = []
# carry = 0

# for i in range (-3, 1, 1):
#      sum = a[i] - b[i]
#      p = sum % 10
#      c.insert(0, p + carry)
#      carry = sum // 10

# if carry:
#      c.insert(0, carry)
         
#      print(c)