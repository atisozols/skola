
# # i  0  1  2  3  4
# m = [1, 2, 4, 2, 7]

# print(m[2])
# print(m[-2])
# print(m[1:3])
# print(m[3:])
# print(m[:3])

# print(len(m))
# m.append(4)
# m.insert(0, 6)
# m.pop()
# m.pop(3)
# m.remove(2)
# print(m.count(2))

# x = [3, 5, 9]
# print(m) 
# m = m + x
# print(m)
# m = [1, 7, 3, 6]

# for i in range(len(m)): 
#     print(m[i], end=" ")
# print()

# for masivaElements in m:
#     print(masivaElements, end=" ")

# 1. Dots tukšs masīvs. Cikliski ievadīt piecus elementus tajā.

# m = []
# for _ in range(5):
#     sk = int(input("sk: "))
#     m.append(sk)
    
# 2. Vada skaitļus, kamēr ievada 0. No skaitļiem izveidots masīvs.

# m = []
# sk = int(input("sk: "))
# while sk != 0:
#     m.append(sk)
#     sk = int(input("sk: "))
# print(m)
    
    
# 3. Iepriekšējā uzdevuma masīvam aprēķināt vidējo vērtību.

# sum = 0
# for el in m:
#     sum += el
    
# print(sum/len(m))

# 4. Skaitlis par masīvu. 673 -> [6, 7, 3]

# m = []
# n = int(input("n: "))
# while n > 0:
#     p = n % 10
#     m.insert(0, p)
#     n = n // 10
# print(m)

# 5. Masīvs par skaitli. [2, 8, 4] -> 284

# m = []
# sk = int(input("sk: "))
# while sk != 0:
#     m.append(sk)
#     sk = int(input("sk: "))
# print(m)

# sk = 0

# for el in m:
#     sk *= 10
#     sk += el
    
# print(sk)

# 6. Atrast masīva lielāko elementu. ( *amplitūdu )

# m = [3, 7, 4, 2, 1, 4, 8, 3, 5]

# max = m[0]
# for el in m:
#     if el > max:
#         max = el
# print(max)
        
# FV

# i  0  1  2  3 ..
# m = [2, 6, 3, 7, 1, 3, 9]

# 7. Dots masīvs m. Izvadīt masīva pirmā un piektā elementa summu.

# print(m[0] + m[4])

# 8. Izvadīt visus masīva elementus, izmantojot ciklu.
    
# for elem in m:
#     print(elem)

# 9. Izvadīt visu elementu summu.

# sum = 0
# for elem in m:
#     sum += elem

# sum += 1 -> sum = sum + 1

# 10. Izņemt no masīva visus pieciniekus.

# m = [2, 5, 6, 3, 5, 2, 7, 1, 3, 5, 9]

# skaits = m.count(5)

# for i in range(skaits):
#     m.remove(5)
    
# print(m)

# 11. Atrast masīvā visbiežāk sastopamo elementu

# max_sk = 0
# skaitlis = 0
# m = [2, 5, 6, 3, 5, 2, 7, 1, 3, 5, 9]
# for el in m:
#     if m.count(el) > max_sk:
#         max_sk = m.count(el)
#         skaitlis = el
#     print(el, m.count(el), max_sk)
        
# print(skaitlis, "paradas", max_sk, "reizes")

# 12. Izvadīt katru otro masīva elementu.

# # i  0  1  2  3  4  5
# m = [1, 6, 3, 7, 2, 3]

# for i in range(len(m)):
#     if i % 2 != 0:
#         print(m[i])



# 13. Atrast top 3 vērtības masīvā.

# m = [2, 5, 6, 3, 5, 2, 7, 1, 3, 5, 9]
# top = []

# for _ in range(len(m)):
#     max = m[0]
#     for el in m:
#         if el > max:
#             max = el
#     top.append(max)
#     m.remove(max)
    
# print(top)


# 14. Dots masīvs. Noņemt no masīva visus duplikātus

# m = [2, 5, 6, 3, 5, 2, 7, 1, 3, 5, 9]

# for elem in m:
#     skaits = m.count(elem)
#     if skaits > 1:
#         for _ in range(skaits - 1):
#             m.remove(elem)
# print(m)

sv = "Atis" # ["A", "t", "i", "s"]
# print(sv.count("t"))

# s1 = "tukuma raina valsts gimnazija"
# print(s1.count(" ") + 1)

# 15. Procentuālais svars katram burtam tekstā
# text = "The Serbian tennis star was detained in January over his refusal to be vaccinated against Covid. He was deported from the country 10 days later, despite mounting a successful legal challenge. At times dubbed Fortress Australia, the country had some of the strictest pandemic restrictions in the world. When Djokovic arrived in Australia in January, Covid cases were skyrocketing and government rules required anyone entering the country be vaccinated, unless they had a valid medication exemption."

# text1 = text.replace(" ", "").replace(".", "").replace(",", "")

# mazie = "abcdefghijklmnopqrstuwxyz"
# lielie = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# for mazais, lielais in zip(mazie, lielie):
#     burta_skaits = text1.count(mazais) + text1.count(lielais)
#     svars = burta_skaits * 100 / len(text1)
#     print(mazais, round(svars, 2))

# ASCII tabula - simbolu kodējums ( katram simbolam ir decimāla vērtība )

# lielais A ir ar vērtību 65

# print(ord('t') - ord('T'))

# starp jebkuru lielo un mazo burtu, ascii tabulā
# starpība ir 32

# simbola vērtību iegūst ar ord
# vērtības simbolu ar chr (character)

# print(chr(97))

# 16. Katram burtam tekstā noteikt vērtību.

# sv = "atis, oZols GARSIGAS PANKUKAS"

# for char in sv:
#     # pārbaudam, vai simbols ir mazais burts
#     # if ord(char) > 96 and ord(char) < 123:
#     #     print(char, ord(char), ord(char) - 32, chr(ord(char) - 32))
#     # else:
#     #     print(char, ord(char))
#     if ord(char) > 96 and ord(char) < 123:
#         # mazais burts par lielo
#         print(chr(ord(char) - 32), end="") # end parametrs nodrošina to, ka print nepārlec jaunā rindā kattreiz
#     elif ord(char) > 64 and ord(char) < 91:
#         # lielais burts par mazo
#         print(chr(ord(char) + 32), end="")
#     else:
#         print(char, end="")

# 17. Teksta šifrēšana
sv = "tukuma raina valsts gimnazija"
# for char in sv:
#     print(chr(ord(char) + 3), end="") # wxnxpd#udlqd#ydovwv#jlpqd}lmd
# print()

# sv = "wxnxpd#udlqd#ydovwv#jlpqd}lmd"
# for char in sv:
#     print(chr(ord(char) - 3), end="")
# print()

# 18. teksts par Title Case - pirmais lielais, pārējie mazie
# sv = "aTiS ozoLS" # Atis Ozols
# for i in range(len(sv)):
#     # pārbaudām pirmo burtu vai burtu pēc neburta simbola
#     if i == 0 or ord(sv[i - 1]) < 65:
#         if ord(sv[i]) > 64 and ord(sv[i]) < 91: # pārbauda, vai ir lielais burts
#             print(sv[i], end="") # ja ir, tad atstāj
#         elif ord(sv[i]) > 96 and ord(sv[i]) < 123:
#             print(chr(ord(sv[i]) - 32), end="") # citādi nomaina uz lielo
#         else:
#             print(sv[i], end="")
#     # visi pārējie burti pēc pirmā
#     else:
#         if ord(sv[i]) > 64 and ord(sv[i]) < 91: # pārbauda, vai ir lielais burts
#             print(chr(ord(sv[i]) + 32), end="") # nomaina uz mazo
#         elif ord(sv[i]) > 96 and ord(sv[i]) < 123: 
#             print(sv[i], end="") # ja mazais, tad atstāj
#         else:
#             print(sv[i], end="")
            
# Noderīga funkcija = split() - simb virkne par masīvu, caur padoto sadalītāju

# sv = "tukuma raina valsts gimn"

# m = sv.split(" ")
# print(m)


# 19. Lietotājs ievada tekstu. Programma atrod garāko vārdu tekstā. (* top 3 garāko vārdus)

# text = input('ievadi tekstu: ')
# text = text.split(" ")
# print(text)

# for _ in range(3):
#     max = text[0]
#     for word in text:
#         if len(word) > len(max):
#             max = word
#     print(max)
#     text.remove(max)

# 20. Lietotājs ievada divus vārdus, programma sakārto tos alfabēta secībā.
#     (* nevis divus vārdus, bet visu tekstu)

# vardi = input("ievadi divus vardus: ")
# vardi = vardi.split(" ")
# # vardi[0], vardi[1]

# if vardi[0][0] > vardi[1][0]:
#     print(vardi[1], vardi[0])
# else:
#     print(vardi[0], vardi[1])


# 21. Programma, kas ievadīto tekstu izvada no otra gala. (alus -> sula)

# text = input('ievadi tekstu: ')
# for i in range(len(text) - 1, 0, -1): # (sakuma_i, beigu_i_neieskaitot, solis)
#     print(text[i], end="")

# 22.** Programma, kas nosaka, vai ievadītais teksts ir palindroms.
#       Palindroms - virkne, kas no abiem galiem lasās vienādi
#       Piemēram: ala -> ir; 1238321 -> ir; 123421 -> nav
#   text1 = "skola"
#   text2 = "tukums"
#   text1+text2 = "skolatukums"

sv = "alllla"
if len(sv) % 2 == 0:
    vidus = len(sv) // 2 
    reversed = ""
    pirma, otra = sv[:vidus], sv[vidus:]
    for i in range(len(otra) - 1, 0, -1): # (sakuma_i, beigu_i_neieskaitot, solis)
        reversed += otra[i]
        
    if reversed == pirma:
        print("ok")
else:
    vidus = len(sv) // 2 
    pirma, otra = sv[:vidus], sv[vidus + 1:]
    reversed = ""
    for i in range(len(otra) - 1, 0, -1): # (sakuma_i, beigu_i_neieskaitot, solis)
        reversed += otra[i]
        
    if reversed == pirma:
        print("ok")



# m = [3, 6, 2, 7, 2, 8, 1]
# print(len(m)//2)
# m = m[:3] + m[4:]
# print(m)
# sorted = []

# for i in range(len(m)):
#     poz = 0
#     if len(sorted) == 0:
#         sorted.insert(poz, m[i])
#     else:
#         while len(sorted) > poz and m[i] < sorted[poz]:
#             poz += 1
#         sorted.insert(poz, m[i])
        
# print(sorted)

# ASCII tabula

# no dec uz char
# print(chr(65))

# no char uz dec
# print(ord('A'))

# Katram simbolam tekstā izvadīt ascii vērtību

# text = "LedusSkaPiS"
    
# l_sk = 0
# m_sk = 0

# for char in text:
#     if 'A' >= char <= 'Z':
#         l_sk += 1
        
#     elif 123 > ord(char) > 96:
#         m_sk += 1
        
# print(m_sk, l_sk)


################# Atkārtojums #####################

# 1. Vada skaitļus kamēr ievada 0. No skaitļiem tiek izveidots masīvs.
#    Izvadīt to pa vienam elementam stabiņā

# m = []
# n = int(input("skaitlis: "))
# while n != 0:
#     m.append(n)
#     n = int(input("skaitlis: "))

# for elem in m:
#     print(elem)

# 2. Izveidotajam masīvam izvadīt: elementu summu, vidējo vērtību.

# sum = 0
# for elem in m:
#     sum = sum + elem # sum += elem
    
# print(sum, sum/len(m))

# 3. Vada skaitļus kamēr ievada 0. No skaitļiem tiek izveidots masīvs,
#    bet masīvā sākumā - nepāra elementi, beigās pāra. 
#    [3, 7, 1, 5, 2, 4, 6, 2]

## SV

# 1. Lietotājs vada skaitļus līdz ievada 0. Programma izveido masīvu no ievadītajiem skaitļiem.

# 2. Izvadīt 1. uzd. masīva pēdējos piecus elementus.

# 3. Izvadīt no masīva tos elementus, kas ir mazāki par 12 un dalās ar 3.

# 4. Ievada simbolu virkni - noteikt, vai tā uzrakstīta tikai ar lielajiem burtiem.

# 5. Ievada simbolu virkni - noteikt, vai tas ir pareizi uzrakstīts pasta indekss.

test1 = "LV-3139"
test2 = "L-3V139"

post = test2

ok = True

if post[2] != '-':
    ok = False
    
for char in post[:2]:
    if not ('A' <= char <= 'Z'):
        ok = False
        
for char in post[3:]:
    if not ('0' <= char <= '9'):
        ok = False
        
if len(post) != 7:
    ok = False
    
print(ok)

# 6. Ievada divus masīvus garumā 4, aizpildot tos ar cipariem!! (0 - 9)
#    Uzrakstīt programmu, kas masīvus saskaita rakstos. (vienu zem otra)

#    1
a = [3, 4, 3, 6]
b = [7, 6, 5, 1]

c = []
atlik = 0

for i in range(3, -1, -1): # sak, beigas_n, solis
    sum = a[i] + b[i] + atlik
    if sum > 9:
        atlik = 1
        c.insert(0, sum % 10)
    else:
        atlik = 0
        c.insert(0, sum)

if atlik == 1:
    c.insert(0, 1)

print(c)


