# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print(arr[2])

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

# resurss: https://www.programiz.com/python-programming/list

# Uzdevums: Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 3) lielāko elementu; 4) visu elementu summu


# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for element in arr:
#     if elelemnt % 2 == 0:
#         print(el)



# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for element in arr:
#     if elelement % 2 != 0:
#         print(el)



# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# lielākais_skaitlis = max(arr)
# print(lielākais_skaitlis)



# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# summa = sum(arr)
# print(summa)


# sv = "Maksis Golomboši"     #( M; A ; K; S; I; S .....)
# for char in sv:
#     print(char)

# s = [1, 6, 3, 8, 3, 7]

# skaits = s.remove(3)
# for i in range(skaits):
#     s.remove

# s.extend([1, 7, 3])
# s += [1, 7, 3]

# 46.  Doti divi saraksti, Iegūt sarakstu šķēlumu

# t = [7, 4, 8, 2, 9, 0]
# s = [1, 6, 3, 8, 3, 2, 5]
# skelums = []
# for t_element in t:
#     for s_element in s:
#         if t_element == s_element:
#             skelums.append(t_element)

# print(list(sket(skelums)))

# 47. No tiem pāsiem sarakstiem iegūt
# starpību jeb visus elemntus no t, kas NAV iekš s.

# for elem in skelums:
#     t.remove(elem)


# s = [1, 6, 3, 8, 3, 2, 5]

# for elem in s:
#     print(elem)

# for i in range(6, -1, -1):
#     print(i, s[i])


# 50. Noteikt, vai saraksts ir palindroms.
#       (no abiem galiem lasās vienādi)
#       [1, 5, 6, 5, 1] --> JĀ
#       [1, 2, 3, 4] --> NĒ             []      []     []

# s = [1, 5, 6, 5, 1]
# s_copy = []

# ejot caur sarakstu s pretējā vierzienā, izveidoju apgriestu kopiju.

# for i in range(len(s) -1, -1, -1):
#     s_copy.append(s[i])

# if s == s_copy:
#     print("ir palindroms")
# else:
#     print("nav")



# 51. Dots saraksts nums. Lietotājs ievada skaitli,
#  programma izvada to divu skaitļu _indeksus_, kas summā veido
#  ievadīto skaitli.
#                                                []    []       []
#      piemērs  0 1 2 3 4 5

# nums = [2, 7, 1, 4, 6, 8, 3]

# sum = int(input(" ievadi skaitli: "))

# for i in range(7):
#     for j in range(7):
#         if j != i:
#             if nums [i] + nums [j] == sum:
#                 print(nums[i], nums[j])


# 52. Dotam sarakstam noskaidrot mediānu.

#      piemērs  0 1 2 3 4 5                       []    []       []

# nums = [2, 7, 1, 4, 6, 8, 3]
# nums.sort()

# index = (int(len(nums)/2))
# print("mediana: ", nums[index])
        
#       0  1  2  3  4  5  6  7
# nums = [2, 7, 1, 4, 6, 8, 3, 13]
# nums.sort()

# if len(nums) % 2 == 0
#     index = (int(len(nums)/2))
#     print("mediana: ", nums[index] + nums[index - 1]/2)
# else:
#     index = (int(len(nums)/2))
#     print("mediana: ", nums[index])


# 53. Ievada skaitlim. Izvada tos elementus, kas mazaāki par n.  []
# nums = [2, 7, 1, 4, 6, 8, 3, 5]

# n = int(input("n: "))
# print("mazaki par n")

# for elem in nums:
#     if elem < n:
#         print(elem)

# for i in range(len(nums)):
#     if nums[i] < n:
#         print(nums[i])

# 1. Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.      []

# arr = [] 

# while True:
#     n = int(input("n: "))
#     if n == 0:
#         break
#     arr.append(n)
#     print(arr)

# 2. No 1. uzd saraksta izvadīt pēdējos piecus elementus.

# [5, 6, 1, 2, 4, 3]

# while True:
#     n = int(input("n: "))
#     if n == 0:
#         break
#     arr.append(n)
# arr.reverse()
# print(arr[0:5])

# 3. Izvadīt no saraksta tos elementus, kas mazāki par 12 un dalās ar 3.

# for elem in s:
#     if elem < 12:
#         if elem % 3 == 0:
#             print(elem)


# 4. Ievada vai sagatavo divus sarakstus garumā 4, kas satur tikai ciparus (0 - 9).
#    Uzrakstīt programmu, kas sarakstus saskaita rakstos

# a =  [1, 3, 6, 2]
# b =  [2, 4, 1, 1]
# c =  []

# for i in range(3, -1, -1):
#     sum = a[i] + b[i]
#     c.insert(0, sum)

# print(c)

# -----------------------------------------------------PD

# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]


def create_list_func(number):
    array_list = []
    for digit in str(number):
        array_list.append(int(digit))
        return array_list
    print (create_list_func(456))




# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.

# skaitlu_saraksts = []

# while True:
#     ievade =int(input("Ievadi skaitli(0 lai pārtrauktu)"))
    
#     if ievade == 0:
#         break
#     skaitlu_saraksts.append(ievade)

#     nepari_skaitli = [skaitlis for skaitlis in skaitlu_saraksts if skaitlis % 2 != 0]

#     mazie_nepari = nepari_skaitli[: 3]
    
#     print("Sarakstā ir šādi 3 mazākie nepāra skaitļi:", mazie_nepari)


# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

arr = []
while len(arr) < 10:

# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c = []
# carry = 0

# for i in range(-3, 1, 1):
#     sum = a[1] - b[1]
#     p = sum % 10
#     c.insert(0, p + carry)
#     carry = sum // 10

# if carry:
#     c.insert(0, carry)

# print(c)







