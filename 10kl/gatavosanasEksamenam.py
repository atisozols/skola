def printArray(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()

# 1. Ievada x un ievada y. No lielākā atņem mazāko un izvada starpību!

# 2. Ievada x. Programma nosaka, vai tas ir pāra vai nepāra.

# 3. x un y. Programma nosaka, kurā kvadrantā atrodas šis punkts.

# 4. Saskaitīt trīscipara skaitļa ciparus.

# x = 12345
# sum = 0

# while x > 0:
#   pedejaisCipars = x % 10
#   sum += pedejaisCipars
#   x = x // 10
  
# print(sum)

# 5. Trīs ievadīti skaitļi, programma izvada tos augošā secībā

# 6. Datuma validācija. Tiek ievadīts mēnesis un 
#    diena. Nosaka, vai šāds datums eksistē

# 7. Ievadīti trīs skaitļi. No šiem trim skaitļiem 
# saskaitīt tikai pāra skaitļus.

# 8. Divi skaitļi a, b. Programma aprēķina atbilstošā
#  taisnstūra perimetru un laukumu.

# 9. Divciparu skaitlis. Samainīt vietām skaitļa ciparus
# un saskaitīt ar sākotnējo skaitli. (ievada 15 -> 15 + 51 = 66)

# n = input('ievadi divciparu skaitli: ')
# n_reversed = n[::-1]
# print(int(n) + int(n_reversed))

# 10. Programma, kas izvada visus nenegatīvos skaitļus, kas mazāki par 10!

# 11. Ievada piecus skaitļus un izvada to summu un vidējo vērtību.

# 12. Lietotājs ievada, cik skaitļi tiks ievadīti,
#     skaitļus ievada, izvada vidējo vērtību.

# 13. Visi skaitļi no 1 līdz 100, izvada tikai tos, kas dalās ar 3 un 8.

# 14. Programma, kas izvada n x n kvadrātu no "*" simboliem.

# n = int(input('n: '))
# for i in range(n):
#   for j in range(n):
#     print("*", end=" ")
#   print()

# 15. Eglīte no simboliem "*" augstumā n.

# n = int(input('n: '))
# for i in range(n):
#   for j in range(i + 1):
#     print("*", end=" ")
#   print()

# 16. While cikls. Ievadīt skaitļus līdz ievada 0. Izvadīt skaitļu summu.

# 17. Izvadīt visus skaitļus no 1 līdz n. Izmantot while ciklu

# 18. Programma, kas izvada pirmos n kvadrātus! (1, 4, 9, 36...)

# 19. Programma, kas izvada visus kvadrātus, kas mazāki par n.

# sk = int(input("ievadi sk: "))
# i = 1
# while i * i < sk:
#   print(i * i)
#   i += 1

# 20. Ievada n. Programma, kas izvada visus skaitļus no n līdz 2n.

# 21. Programma, kas saskaita visus skaitļus no 1 līdz 100.

# 22. Izvadīt visus nepāra skaitļus dilstošā secībā no 25 līdz 1.

# 23. Izmantojot ciklu, izveidot programmu, kas liek ievadīt piecus skaitļus
# un izvada to summu.

# 24. Vada skaitļus, kamēr ievada nulli. izvadīta skaitļu summa.

# 25. Patvaļīga lieluma skaitlim aprēķināt ciparu summu.

# 26. Ievadītam skaitlim aprēķināt dalītāju skaitu. Noteikt, vai skaitlis ir pirmskaitlis.

# 27. Vadam skaitļus līdz ievadam nulli. 
#     Programma pasaka par katru nākošo, vai 
#     tas ir lielāks vai mazāks par iepriekšējo.

# n = int(input("sk: "))
# while n != 0:
#   m = int(input("sk: "))
#   if m > n:
#     print("lielaks")
#   else:
#     print("nav lielaks")
#   n = m

# 28. Vada skaitļus, kamēr ievada 0. Aprēķināt 
#     vidējo, maksimālo un minimālo vērtību.

# 29. Vada skaitļus, kamēr ievada 0. Atrast modu.

# 30. Klasē ir septiņi skolēni. Nepieciešams 
#     katram ievadīt atzīmes, kas var būt patvaļīgā skaitā.
#     Programma katram skolēnam izvada vidējo atzīmi.

# atzimes = []
# for i in range(3):
#   row = []
#   atz = int(input("ievadi atzimi " + str(i) + ". skolenam"))
#   while atz != 0:
#     row.append(atz)
#     atz = int(input("ievadi atzimi " + str(i) + ". skolenam"))
#   print(row)
#   atzimes.append(row)

# 31. Dots tukšs masīvs. Cikliski ievadīt piecus elementus tajā.

# 32. Vada skaitļus, kamēr ievada 0. No skaitļiem izveidots masīvs.

# 33. Iepriekšējā uzdevuma masīvam aprēķināt vidējo vērtību.

# 34. Skaitlis par masīvu. 673 -> [6, 7, 3]

# 35. Masīvs par skaitli. [2, 8, 4] -> 284

# 36. Atrast masīva lielāko elementu. ( *amplitūdu )

# 37. Dots masīvs m. Izvadīt masīva pirmā un piektā elementa summu.

# 38. Izvadīt visus masīva elementus, izmantojot ciklu.

# 39. Izvadīt visu elementu summu.

# 40. Izņemt no masīva visus pieciniekus.

# 41. Atrast masīvā visbiežāk sastopamo elementu

m = [1, 5, 3, 7, 2, 4, 2, 7, 9, 2, 5, 6]

diction = {}

for num in m:
  diction[num] = m.count(num) # skaitlis:skaits
  
print(diction) # {1: 1, 5: 2, 3: 1, 7: 2, 2: 3, 4: 1, 9: 1, 6: 1}

sorted_list = sorted(diction, key=diction.get) # [1, 3, 4, 9, 6, 5, 7, 2]

print(sorted_list[-1])

# 42. Izvadīt katru otro masīva elementu.

# 43. Atrast top 3 vērtības masīvā.

# 44. Dots masīvs. Noņemt no masīva visus duplikātus

m = [2, 4, 5, 2, 1, 1] # [2, 4, 5, 1]
print(list(set(m)))

# m_copy = []

# for elem in m:
#   if m_copy.count(elem) < 1:
#     m_copy.append(elem)
    
# print(m_copy)

# 45. Procentuālais svars katram burtam tekstā
text = "The Serbian tennis star was detained in January over his refusal to be vaccinated against Covid. He was deported from the country 10 days later, despite mounting a successful legal challenge. At times dubbed Fortress Australia, the country had some of the strictest pandemic restrictions in the world. When Djokovic arrived in Australia in January, Covid cases were skyrocketing and government rules required anyone entering the country be vaccinated, unless they had a valid medication exemption."
text = text.lower()
text = text.replace(".", "").replace("!", "").replace(",", "").replace(" ", "")

d = {}
import string
for char in string.ascii_lowercase:
  d[char] = text.count(char) / len(text) * 100
  
for key in d:
  print(key, d[key])


# 46. Katram burtam tekstā noteikt ASCII vērtību.

# 47. teksts par Title Case - pirmais lielais, pārējie mazie

# 48. Lietotājs ievada tekstu. Programma atrod garāko vārdu tekstā. (* top 3 garāko vārdus)

# 49. Lietotājs ievada divus vārdus, programma sakārto tos alfabēta secībā.
#     (* nevis divus vārdus, bet visu tekstu)

# 50. Programma, kas ievadīto tekstu izvada no otra gala. (alus -> sula)

# 51.** Programma, kas nosaka, vai ievadītais teksts ir palindroms.
#       Palindroms - virkne, kas no abiem galiem lasās vienādi
#       Piemēram: ala -> ir; 1238321 -> ir; 123421 -> nav

# 52. Ievada simbolu virkni - noteikt, vai tā uzrakstīta tikai ar lielajiem burtiem.

# 53. Ievada simbolu virkni - noteikt, vai tas ir pareizi uzrakstīts pasta indekss.

# 54. Ievada divus masīvus garumā 4, aizpildot tos ar cipariem!! (0 - 9)
#    Uzrakstīt programmu, kas masīvus saskaita rakstos. (vienu zem otra)
 
# 55. Izvadīt 2D masīva nepāra rindas

# divd = [[1, 2, 3, 0, 1],
#         [4, 5, 6, 4, 2],
#         [7, 8, 9, 9, 5],
#         [1, 6, 9, 2, 0],
#         [6, 1, 1, 3, 5]]

# 56. Otro kolonnu

# 57. Diagonāles elementus
 
# 58. Otru diagonāli

# 59. Izveidot 5x5 masīvu, aizpildot to ar 0
  
# 60. Programma, kas aizpilda masīvu ar 1 diagonālēs

# 61. Aizpilda rāmi ar 1

# 62. funkcija tilpums, kas ieejā saņem trīs parametrus 
#    un atgriež atbilstošā paralēlskaldņa tilpumu
#    nodemonstrēt funkcijas izsaukumu

# 63. funkcija max_value, kas ieejā saņem vienu parametru - patvaļīgi garu masīvu
#    funkcija atgriež masīva lielāko vērtību

# 64. Funkcija isEven, kas ieejā saņem skaitli un izejā atgriež vai nu 
#    True vai False atkarībā no tā, vai skaitlis ir pāra

# 65. Dots divdimensiju masīvs. Aprēķināt katras rindas vidējo vērtību;
#    katras kolonnas vid. vērtību

# 66. Dots 8x8 masīvs no nullēm

arr = [[0 for _ in range(8)] for _ in range(8)]


# 67. Ievadīt x, y. Masīvā ielikt 1 atbilstošajā pozīcijā.

# 68. Ievadīt šaha lauciņa pozīciju(e4).

# burts = "abcdefgh"
# poz = input("pozicija: ") # "e4" -> [0] = e, [1] = 4

# x = 8 - int(poz[1])
# y = burts.index(poz[0])

# arr[x][y] = 1


# 69. No ievadītās pozīcijas parādīt visus iespējamos gājienus:
#    a) tornim

# for i in range(8):
#   for j in range(8):
#     if i == x or j == y:
#       arr[i][j] += 1
    
#    b) laidnim

# for i in range(8):
#   for j in range(8):
#     if i + j == x + y or i - j == x - y:
#       arr[i][j] += 1

#    c) dāmai

# for i in range(8):
#   for j in range(8):
#     if i + j == x + y or i - j == x - y or i == x or j == y:
#       arr[i][j] += 1

#    d) karalim

# for i in range(8):
#   for j in range(8):
#     if abs(x-i) <= 1 and abs(y-j) <= 1:
#       arr[i][j] += 1

#    e) zirgam

# for i in range(8):
#   for j in range(8):
#     if (abs(x-i) == 1 and abs(y-j) == 2) or (abs(x-i) == 2 and abs(y-j) == 1):
#       arr[i][j] += 1


# printArray(arr)

# 70. Dots masīvs garumā 9. Izveidot no masīva 3x3 2D masīvu.
# mas = [2, 5, 7, 2, 7, 1, 4, 9, 2]
# mas2d = []

# index = 0
# for i in range(3):
#   row = []
#   for j in range(3):
#     row.append(mas[index])
#     index += 1
#   mas2d.append(row)
  
# printArray(mas2d)
  
# 71. Izvadīt masīva lielāko elementu un tā atrašanās vietu masīvā. (9 atrodas poz (3, 1))

# 72. Izvadīt katras rindas vidējo vērtību. (* katras kolonnas vidējo)

# 73. Izvadīt summu tiem elementiem, kas neatrodas uz nevienas no diagonālēm.

# 74. Funkcija numSum(n), kas skaitlim n atgriež ciparu summu.

# 75. Funkcija saknes(a, b, c), kas trīs padotiem parametriem 
# (kvadrātvienādojuma koeficientiem), atgriež masīvu ar saknēm.

# 76. Dots divdimensiju masīvs. Noteikt, vai tajā ir vairāk pāra skaitļi vai nepāra.  

# 77. Dots desu laukums. Noteikt, vai tajā ir uzvarētājs
# un kurš uzvarēja. (Spēlē vieninieki pret nullītēm)

tic_tac_toe = [[0, 1, 0],
               [0, 0, 1],
               [1, 0, 1]]


# 78. Dots šaha laukums kurā stāv divas dāmas. Uzrakstīt programmu, kas pasaka, vai dāmas viena otru "redz".


        
import random

chess = [[0 for _ in range(8)] for _ in range(8)]
chess[random.randint(0,7)][random.randint(0,7)] = 1
chess[random.randint(0,7)][random.randint(0,7)] = 1

# printArray(chess)

# 79. Funkcija, kas pārbauda, vai masīvs ir augošā secībā

# 80. Klase Paralelskaldnis, kura konstruktorā saņem trīs vērtības - šķautņu garumus.
#     Iekšējās metodes/funkcijas - tilpums(), virsmasLaukums().   

# 81. Klase Cilindrs    

# 82. Klase Kvadratvienadojums   

# 83. BankAccount klase, kurai konstruktorā padod sākotnējo 
#     bilanci un eksistē metodes deposit(amount) un withdraw(amount)
#     getBalance()

