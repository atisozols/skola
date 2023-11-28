# 1P. Programma, kas izvada visus skaitļus no -1 līdz -10 dilstošā secībā
# 1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37. 

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no šiem skaitļiem ir lielāka ciparu summa.
# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība

# 3P. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. No ir ievadītajiem skaitļiem atrast lielāko pāra skaitli.
# 3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.

# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.
# Piemērs: 1326569 -> 132 -> 2.0

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

#1
result1 = []
for i in range(-1, -11, -1):
    result1.append(i)
print(result1)

#2
num1 = int(input("ievadīt pirmo skaitli: "))
num2 = int(input("ievadīt otro skaitli: "))
sum1 = 0
sum2 = 0
while num1 > 0 or num2 > 0:
    if num1 > 0:
        sum1 += num1 % 10
        num1 //= 10
    if num2 > 0:
        sum2 += num2 % 10
        num2 //= 10
if(sum1 > sum2):
    print(sum1)
elif(sum2 > sum1):
    print(sum2)
else:
    print("vienādi:", sum1)

#3
num = 1
result2 = []
while num != 0:
    num = int(input("ievadīt skaitli: "))
    if num % 2 == 0:
        result2.append(num)
result2.sort()
print(result2[len(result2) - 1])

#4
num = int(input("ievadīt skaitli: "))
sum = 0
sum1 = [0,0,0]
while num > 1000:
    sum += num % 10
    num //= 10
for i in range(3):
    sum1[i] += num % 10
    num //= 10
sum1.sort()
print(sum1[1])

#5 
pirmskaitlis = False
num = int(input("ievadīt skaitli: "))
for i in range(2, num):
    if(num % i == 0):
        pirmskaitlis = True
        break
if pirmskaitlis:
    # izvada lielāko, ja nav pirmskaitlis
    lielakais = 0
    while num > 0:
        if(num % 10 > lielakais):
            lielakais = num % 10
        num //= 10
    print("skaitlis nav pirmskaitlis, lielākais cipars ir:", lielakais)
else:
    # izvada ciparu summu, ja ir pirmskaitlis
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print("skaitlis ir pirmskaitlis, to ciparu summa ir:", sum)



