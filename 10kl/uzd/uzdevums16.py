# Programma saskaita masīvus garumā 10 rakstos.

a = []

for i in range(10):
    x = int(input('ievadi skaitli: '))
    a.append(x)

b = []

for i in range(10):
    x = int(input('ievadi skaitli: '))
    b.append(x)

for i in range(len(a)):
    print(a[i], end='')
print()

for i in range(len(b)):
    print(b[i], end='')
print()

n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(9, -1, -1):
    n[i] = a[i] + b[i]
    if n[i] > 9:
        n[i] = n[i] % 10
        if i == 0:
            n.insert(0, 1)
        else:
            n[i-1] += 1

for i in range(len(n)):
    print(n[i], end='')
print()
