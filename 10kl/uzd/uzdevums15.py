# Ievada masīvu. Programma pasaka, vai tas ir sakārtots augošā secībā.

a = []

x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))

for i in range(len(a)):
    print(a[i], end=' ')
print()

indikators = 0
for i in range(len(a)-1):
    if a[i] >= a[i+1]:
        indikators += 1
        break

if indikators == 0:
    print('masīvs ir sakārtots')
else:
    print('nav sakārtots')



