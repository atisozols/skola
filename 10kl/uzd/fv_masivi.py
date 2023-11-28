# 1. uzdevums

a = []

x = int(input('ievadi skaitli: '))
while x != 0:
    a.append(x)
    x = int(input('ievadi skaitli: '))

# 2. uzdevums

for i in range(len(a)):
    print(a[i], end=' ')
print()

# 3. uzdevums

lielakais = a[0]
lielakaIndekss = 0
for i in range(1, len(a)):
    if a[i] > lielakais:
        lielakais = a[i]
        lielakaIndekss = i

mazakais = a[0]
mazakaIndekss = 0
for i in range(1, len(a)):
    if a[i] < mazakais:
        mazakais = a[i]
        mazakaIndekss = i

print('amplitūda: ', lielakais - mazakais)

# iebuvetas funkcijas min(a) un max(a) bija alternativs risinajums

# 4. uzdevums

a.pop(mazakaIndekss)
a.pop(lielakaIndekss)

lielakais = a[0]
lielakaIndekss = 0
for i in range(1, len(a)):
    if a[i] > lielakais:
        lielakais = a[i]
        lielakaIndekss = i

mazakais = a[0]
mazakaIndekss = 0
for i in range(1, len(a)):
    if a[i] < mazakais:
        mazakais = a[i]
        mazakaIndekss = i

print('amplitūda: ', lielakais - mazakais)



