# 1. Teksts par Title Case (sodien ara saulains laiks - Sodien Ara Saulains Laiks)

# with open("atkartojums.txt") as f:
#   text = f.read()
#   words = text.split(" ")
#   for word in words:
#     for i in range(len(word)):
#       if i == 0:
#         print(word[i].upper(), end="")
#       else:
#         print(word[i].lower(), end="")
#     print(" ", end="")
    
# 2. Teksta fails, kur katrā rindiņā 
# glabājas 3 skaitļi - taisnstūra paralēlskaldņa
# šķautņu garumi. Aprēķināt kopējo tilpumu.

# big_volume = 0
# with open("paralelskaldni.txt") as f:
#   lines = f.readlines()
#   for line in lines:
#     values = line.split()
#     volume = 1
#     for value in values:
#       volume *= int(value) # volume = volume * int(value)
#     big_volume += volume
    
# print(big_volume)

# 3. [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# arr = []
# with open("masivs.txt") as f:
#   first = f.readline() # "3 3\n"
#   size = [int(first[0]), int(first[2])]
#   for i in range(size[0]):
#     row = f.readline().split()
#     arr.append(row)
# print(arr)

# 4. Noteikt spraugu skaitu masīvā. [0, 0, 1, 0, 2, 0, 0, 3, 4, 0, 0] -> 2