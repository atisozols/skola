def summa(a, b):
    sum = a + b
    return sum

def display(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()

def average(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i]
    avg = sum / len(m)
    return avg

x = [3, 5, 8, 2, 6, 2, 1, 2]
y = [3, 5, 7, 6, 4]
a = [[1, 2], [3, 4]]
b = [[3, 2], [3, 7]]

display(a)


def sakartots(m):
    sakart = True 
    for i in range(len(m) - 1):
        if m[i] > m[i + 1]:
            sakart = False
    return sakart

x = [3, 5, 8, 2, 6, 2, 1, 2]

if sakartots(x):
    print("ok")

name = "Atis Ozols"
print(name[5])
m = name.split(' ')
print(m)


x = [3, 5, 8, 2, 6, 2, 1, 2, 5]

m = []
indekss = 0
for i in range(3):
    row = []
    for j in range(3):
        row.append(x[indekss])
        indekss += 1
    m.append(row)
print(m) # [[3, 5, 8], [2, 6, 2], [1, 2, 5]]


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

    















