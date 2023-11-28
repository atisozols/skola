# funkcija, kas pārbauda, vai masīvs ir augošā secībā

from math import ceil, floor


def augoss(masivs):
    indikators = 0
    for i in range(len(masivs) - 1):
        if masivs[i] > masivs[i + 1]:
            indikators += 1
    if indikators == 0:
        return True
    else:
        return False

# funkcija, kas pārbauda, vai skaitlis ir pāra


# funkcija, kas atgriež skaitļa kvadratu

def squared(number):
    return number ** 2

# funkcija, kas atgriež skaitļa kvadratsakni

def sqrt(number):
    return number ** 0.5

# funkcija, kas aprēķina diskriminantu

def diskriminants(a, b, c):
    return b ** 2 - 4 * a * c

# izveidot programmu/funckiju, kas 
# pasaka, vai masīvs sakārtots augošā
# secībā

def sakartots(m):
    sakart = True 
    for i in range(len(m) - 1):
        if m[i] > m[i + 1]:
            sakart = False
    return sakart


def squared(number):
    return number ** 2

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False
        
c = [1, 2, 6, 7, 13]
b = [1, 2, 7, 6, 7, 13]
a = [3, 1, 2, 6, 7, 13]


def num_to_list(num):
    s = []
    while num > 0:
        p = num % 10
        num = round((num - p)/10)
        s.insert(0, p)
    return s
    
x = 34672
print(num_to_list(x))