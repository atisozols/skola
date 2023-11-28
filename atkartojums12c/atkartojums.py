# Programma nosaka, vai ievadītais skaitlis lielāks par 10

# s = int(input('ievadi skaitli: '))
# if s > 10:
#     print("lielaks")
# elif s == 10:
#     print("vienads")
# else:
#     print("mazaks")

# Programma, kas ļauj ievadīt skaitļus līdz tiek ievadīta 0

# x = int(input("ievadi skaitli: "))
# while x != 0:
#     print(x)
#     x = int(input("ievadi skaitli: "))
    
# Programma, kas izvada visus pozitīvus nepāra skaitļus,
# kas mazāki par 20

# for i in range(1, 21, 2): #  (sakums, beigas, solis)
#     print(i)

# for i in range(21):
#     if i % 2 != 0:
#         print(i)

# Masīvi
# i  0  1  2  3  4
m = [1, 4, 2, 7, 3]

# for i in range(len(m)):
#     print(i, m[i])

# Divdimensiju masīvs

# dd = [[1, 4, 2, 7, 3], 
#       [1, 4, 2, 7, 3],
#       [1, 4, 2, 7, 3],
#       [1, 4, 6, 7, 3],
#       [1, 4, 2, 7, 3]]

# print(dd[3][2])

# Simbolu virknes

# teikums = "Labrīt,  Deivid!  "
# print(len(teikums))
# print(teikums.count(' ') + 1)

# vardi = teikums.split(' ')
# print(vardi)
# ['Labrīt,', '', '', 'Deivid!', '', '']

# jauns = []
# for vards in vardi:
#     if len(vards) > 0:
#         jauns.append(vards)

# print(jauns)

# ['Labrīt,', '', '', 'Deivid!', '', '']
# ['Labrīt,', 'Deivid!']

# Tukuma Raina Valsts Gimnazija

# text = "TukumaRainaValstsGimnazija"

# for char in text:
#     if ord(char) > 64 and ord(char) < 91:
#         print(" ", end='')
#         print(char, end='')
#     else:
#         print(char, end='')

text = "tukuma raina valsts gimnazija"
# Tukuma Raina Valsts Gimnazija

c = chr(ord(text[0]) - 32)
i = 0
temp = 0
new = ""
while i < len(text):
    if temp == i:
        new += chr(ord(text[i]) - 32)
    elif text[i] == " ":
        temp = i + 1
        new += " "
    else:
        new += text[i]
    i += 1
print(new)


