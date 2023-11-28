# 1P. Programma, kas izvada visus skaitļus no -1 līdz -10 dilstošā secībā
print("Skaitļi no -1 līdz -10 (neieskaitot):")
for i in range(-1, -10, -1):
    print(i)

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no šiem skaitļiem ir lielāka ciparu summa.
n = int(input("Skaitlis 1: "))
nsum = 0
o = int(input("Skaitlis 2: "))
osum = 0
while n > 0:
    nsum += n % 10
    n = n // 10
while o > 0:
    osum += o % 10
    o = o // 10
print("1. skaitlim ciparu summa ir:", nsum, "\n2. skaitlim ciparu summa ir:", osum)
if osum > nsum:
    print("2. skaitļa summa ir lielāka.")
else:
    print("1. skaitļa summa ir lielāka.")


# 3P. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. No ir ievadītajiem skaitļiem atrast lielāko pāra skaitli.
inp = int(input("Ievadi skaitli: "))
l = 0
if inp % 2 == 0:
    l = inp
while inp != 0:
    inp = int(input("Ievadi skaitli: "))
    if inp > l and inp % 2 == 0:
        l = inp
print("Lielākais pāra skaitlis:", l)
    
# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.
# # Piemērs: 1326569 -> 132 -> 2.0
n = int(input("Ievadi skaitli: "))
sum = 0 
while n > 0:
    while n > 1000:
        n = n // 10
    sum += n % 10
    n = n//10
print("Pirmo 3 ciparu vidējā vērtība ir:",sum/3)

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu
n = int(input("Ievadi skaitli: "))
d = 0
for i in range(1, n+1):
    s = n%i
    if not s:
        d += 1
if d != 2:
    l = 0
    while n > 0:
        if l < n % 10:
            l = n % 10
        n = n // 10
    print("Skaitlis nav pirmskaitlis. Tā lielākais cipars:", l)
else:
    sum = 0 
    while n > 0:
        sum += n % 10
        n = n // 10
    print("Skaitlis ir pirmskaitlis. Tā ciparu summa:", sum)
