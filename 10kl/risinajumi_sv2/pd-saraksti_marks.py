# 1P. Saraksts par skaitli. Piemēram, [2, 8, 4] -> 284
# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]

# 2P. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 lielākos pāra skaitļus.
# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.

# 3P. Programma, kas izveido sarakstu garumā 10 no nejauši ģenerētiem nepāra skaitļiem intervālā (1, 30).
# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).

# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.


#1
arr = [6, 2, 4]
result = 0
counter = 0
for i in range(len(arr)-1, -1, -1):
    result += (arr[counter]* (10 ** i))
    counter += 1
print(result)  

#2
input0 = 1
arr0 = []
arr1 = [0, 0, 0]
while input0 != 0:
    input0 = int(input("Ievadīt skaitli: "))
    arr0.append(input0)
arr0.sort()
for inte in arr0:
    if inte % 2 == 0 and inte > arr1[0]:
        arr1[0] = inte
    arr1.sort()
for inte in arr1:
   if(inte == 0):
    arr1.remove(0)
print(arr1)

#3
import random
arr2 = []
while len(arr2) < 10:
    a = random.randint(0, 30)
    if a % 2 != 0:
        arr2.append(a)
print(arr2)


#4
# a - b = c
a = [4, 3, 2, 6]
b = [7, 3, 4, 5]
c = []
sum1 = 0
sum2 = 0
counter = 0
for i in range(len(a)-1, -1, -1):
    sum1 += (a[counter]* (10 ** i))
    sum2 += (b[counter]* (10 ** i))
    counter += 1
sum = sum1 - sum2

sum5 = sum // 1000
c.append(sum5)
sum6 = sum // 100
sum6 = sum6 % 10
c.append(sum6)
sum7 = sum // 10
sum7 = sum7 % 10
c.append(sum7)
sum8 = sum % 10
c.append(sum8)
for inte in c:
    if(inte == 0):
        c.remove(0)
print(c)



    