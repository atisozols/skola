# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]
s=[]
a=int(input('a:'))
b1000= a//1000
if b1000>0:
    if b1000<10:
         p=b1000%10
    s.append(p)
else:
    s.append(b1000)
b100= a//100
if b100>0:
    if b100<10:
         n=b100%10
         s.append(n)
else:
    s.append(b100)
b10= a//10
if b10>0:
    if b10<10:
         z=b10%10
         s.append(z)
else:
    s.append(b10)




# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.
s=[]
a=int(input('a:'))
while a !=0:
    s.extend([a])
    a=int(input('a:'))
print(s)
for elem in s:
  if elem>0:
    if elem%2==1:
        print(elem)
# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).
import random
a=random.randint(1,12)
s=[a,a,a,a,a,a,a,a,a,a,a]
if a != a:
    s.append(a)
else:
    s.remove(a)
if len(arr)>10:
    s.remove(a)

#4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.
a = [1, 5, 2, 3]
b = [1, 2, 3, 0]
c=[]
for i in range(3, -1, -1):
    sum=a[i] - b[i]
    if sum<0:
        p = sum%10
        carry=1
    else:
    c.insert(0,sum+carry)
    carry=0
if carry>0:
    c.insert(0, carry)
   print(c)