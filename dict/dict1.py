# Izveidot programmu, kas izveido vārdnīcu garumā 10;
# Key vērtības ir naturāli skaitļi 1-10, 
# katram key x pretī ir value x^2

# dic = {}

# for i in range(1, 11):
#     dic[i] = i**2
    
# Dots teksta fails 'dictionary1.txt', kur
# definēta vārdnīca garumā 6
# Ievaddatu katra rindiņa satur key-value pāri
# Nolasīt ievaddatus, izveidojot vārdnīcu

dic = {}
dic2 = {
        '3': '10',
        '6': '9',
        '9': '0'
    }

# # faila atvēršana
with open("dictionary1.txt") as f:
    # readlines izveido masīvu no rindiņām failā
    lines = f.readlines()
    # apstrādājam katru rindiņu masīvā
    for line in lines:
        # izdalām rindiņu uz pusēm, izmantojot atstarpi
        key_value = line.split()
        # print(key_value)
        # iegūtās vērtības izmantojam dictionary aizpildē
        dic[key_value[0]] = key_value[1]
  
dic3 = {}
print(dic,dic2)
for key in dic:
    if dic[key] in dic2:
        dic3[key] = dic2[dic[key]]

# with open("dictionary2.txt") as f:
#     line1 = f.readline()
#     vertibas = line1.split()
    
#     pSkaits = int(vertibas[0])
#     zPieturas = int(vertibas[1])
#     posmi = int(vertibas[2])
    
#     print(pSkaits, zPieturas, posmi)

#     pieturas = {i:[] for i in range(1, 12)}
    
#     print(pieturas)
#     for _ in range(posmi):
#         # nolasam vienu rindinu
#         line = f.readline()
#         # sadalam rindinu pa atstarpem, lai iegutu 
#         # atseviski katru vertibu rindina
#         line = line.split()
#         # iegustam katras vertibas skaitlisko vertibu
#         line[0] = int(line[0])
#         line[1] = int(line[1])
        
#         pieturas[line[0]].append(line[1])
#         pieturas[line[1]].append(line[0])
        
        
#     zalas = {}
#     sarkanas = {}
    
#     for key in pieturas:
#         if key > 7:
#             sarkanas[key] = pieturas[key]
#         else:
#             zalas[key] = pieturas[key]
            
#     print(zalas, sarkanas)

# Ievadītam tekstam izveidot dictionary, kurā glabājas simbols
# un tā skaits tekstā

# valsts gimnazija -> {'a':3, 'i':2, ...}

d = {}
sv = input("ievadi tekstu: ")
for char in sv:
    if char.isalpha():
        d[char] = sv.count(char)
        
# print(d) 
sorted_dic = sorted(d, key=d.get, reverse=True)
print(sorted_dic)
       



