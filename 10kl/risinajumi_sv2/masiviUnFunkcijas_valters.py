# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print(arr[2])

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

#  resurss: https://www.programiz.com/python-programming/list

# Uzdevums: Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 3) lielāko elementu; 4) visu elementu summu
#Izvada visus para skaitļus.
# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for i in arr:
#     if i % 2 == 0:
#         print("Para skaitlis",i)
#     elif i % 2 == 1:
#         print('Nepāra skatlis', i)
#     else:
#         print("Nav ne pāra, ne nepāra")

#Lielākais
# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# Lielākais_Skaitlis = max(arr)
# print(Lielākais_Skaitlis)

# Summa
# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# summa = sum(arr)
# print( summa)

# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3]
# for value in arr:
#     if value % 2 != 0:
#         print(value)

# print(sum(arr))
# print(max(arr))


# sv = "Valters Jotciks"
# print (sv[0])

# sv = "Valters Jotčiks"
# for char in sv:
#     print(char)

# s = [1, 2, 7, 9, 5, 4, 8, 4]

# skaits = s.count(4)
# for i in range(skaits):
#     s.remove(4)

# print(s)
# s = [1, 2, 7, 9, 5, 4, 8, 4]
# s.extend([1, 4, 7, 8])

# print(s)

# 46. Doti divi saraksti. Iegūt sarakstu sķēlumu.

# t = [3, 5, 4, 7, 2, 5]
# s = [9, 4, 6, 3, 6, 7, 5]
# skelums= []
# for t_element in t:
#     for s_element in s:
#         if t_element == s_element:
#             skelums.append( t_element)

# print(list(set(skelums)))

# 47. No tiem pašiem sarakstiem iegūt starpību.
# t = [3, 5, 4, 7, 2, 5]
# s = [9, 4, 6, 3, 6, 5]
# skelums= []
# for t_element in t:
#     for s_element in s:
#         if t_element == s_element:
#             skelums.append( t_element)


# for elem in skelums:
#     t.remove(elem)

# print(t)

# 48. Dots saraksts, izvadīt to no otra gala.

# s=[1, 5, 7, 9, 2, 4]

# for i in range(5, -1, -1):
#     print(s[i])

# s.reverse()
# print(s)

# 50. Noteikt, vai saraksts ir palindroms.
#  ( No abiem galiem lasās vienādi)
#  [1,5,6,5,1] -> jā
#  [1,2,3,4] -> nē


# s = [2, 1, 5, 6, 5, 1, 2]
# s_copy=[]

# for i in range(len(s)-1, -1, -1):
#     s_copy.append(s[i])

# print(s, s_copy)

# if s == s_copy:
#     print('ir palindroms')
# else:
#     print('nav') 


# 51. Dots saraksts nums. Lietotājs ievada skaitli,
# programma izvada to divu skaitļu _indeksus_,
# kas summā veido skaitli.
# piemērs 8 -> 0, 4 ,1 ,2

# nums = [2, 7, 1, 4, 6, 8, 3]

# n = int(input("n: "))
# for i in range(7):
#     for y in range(7):
#         if i != y:
#             if nums[i] + nums[y] == n:
#                 print(i, y)

# for i in range(7):
#     for y in range(7):
#          print(i, y)

# 52. Dotam sarakstam noskaidrot mediānu.

# nums = [2, 7, 1, 4, 6, 8, 3,]
# nums.sort()
# index = int(len(nums)/ 2)
# print('mediana', nums[index])

# nums = [2, 7, 1, 4, 6, 8, 3, 5,]
# nums.sort()
# if len(nums) % 2 == 0:
#     index = int(len(nums)/ 2)
#     print('mediana', nums[index] + nums[index - 1] / 2)
# else:
#     index = int(len(nums)/ 2)
#     print('mediana', nums[index])

# 53. Ievada skaitli n. IZvadīt tos saraksta elementus, kas mazākli par n.
# nums = [2, 7, 1, 4, 6, 8, 3, 5,]

# n = int(input("n: "))
# print('mazāki par n:')
# for elem in nums:
#     if elem < n:
#         print(elem)

# for i in range( len(nums)):
#     if nums[i] < n:
#         print(nums[i])

# 54. Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.

# list = []
# n = int(input("n: "))
# while n != 0:
#     list. append(n)
#     n = int(input("n: "))
# print(list)


# 55.  No 54. uzd saraksta izvadīt pēdējos piecus elementus.
# list = []
# n = int(input("n: "))
# while n != 0:
#     list. append(n)
#     n = int(input("n: "))
# list.reverse()
# print(list[0:5])

# 56. Izvadīt no saraksta tos elementus, kas mazāki par 12 un dalās ar 3.

# list = []
# n = int(input("n: "))
# while n != 0:
#     list. append(n)
#     n = int(input("n: "))

# for i in list:
#     if i < 12 and i % 3 == 0:
#         print(i)


# 57. Ievada vai sagatavo divus sarakstus garumā 4, kas satur tikai ciparus (0 - 9).
#    Uzrakstīt programmu, kas sarakstus saskaita rakstos

# a = [ 2, 5, 1, 7]
# b = [ 4, 6, 9, 3 ]
# c = []

# carry = 0
# for i in range(3, -1, -1):
#     sum = a[i] + b[i]
#     p = sum % 10
#     c.insert(0, p + carry)
#     carry = sum // 10
#     # c.insert(0, sum)
# if carry > 0:
#     c.insert(0, carry)
# print(c)


# PD. .......................................................
# Saraksts par skaitli. Piemēram, [2, 8, 4] -> 284

list = [2, 4, 5]
sum = 0
for elem in list:
    simti = elem[1] * 100
    desmiti = elem[2] * 10
    vieni = elem[3] * 1
    sum = simti + desmiti + vieni
    print(sum)





# Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 lielākos pāra skaitļus

# list = []
# n = int(input("n: "))
# while n != 0:
#     list. append(n)
#     n = int(input("n: "))
# list.sort()
# list.reverse()
# print(list[0:3])


# 3P. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).

# s = random.randint(1, 30)




# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.
# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c=[]
# carry = 0
# for i in range(-3, 1, 1):
#     starp = a[i] - b[i]
#     p = starp % 10
#     c.insert(0, p - carry)
#     carry = starp // 10
#     c.insert(0, starp)
# if carry > 0:
#     c.insert(0, carry)
# print(c)





# print(len(arr)) / saprot un pasaka saraksta garumu
# arr.sort()  / sakārtot visus skaitļus augošā secībā
# arr. append / sarakstā pievienot elementu vai atņemt elementu