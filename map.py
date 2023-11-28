# funkcija, kas kāpina 
# skaitli kvadrātā

def kvadrats(x):
    return x * x


def plusDivi(x):
    return x + 2

# ar list(map()) iegūt jaunu
#  masīvu

a = [2, 5, 2, 6, 8, 2]

b = list(map(kvadrats, a))
c = list(map(plusDivi, a)) 
# masivs = list(map(funkcija, masivs))
# print(b)
# print(c)

# funkcija(programmu), kas iegūst
#  skaitļa ciparu summu

def ciparuSumma(x):
    sum = 0
    while x > 0:
        p = x % 10
        x = round((x - p) / 10)
        sum += p
    return sum

# print(ciparuSumma(152))
# print(ciparuSumma(624))
# print(ciparuSumma(1264))

def otradi(x):
    sk = 0
    while x > 0:
        p = x % 10
        x = round((x - p) / 10)
        sk = sk * 10 + p
    return sk

m = [123, 65482, 1243, 23]
n = list(map(ciparuSumma, m))
print(n)
