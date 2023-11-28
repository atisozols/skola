# Dalitaju summa
def S(num): # funkcija dalitaju summas aprekinam
    sum = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum += i    
    return sum

# mainigo ielasisana
# a = int(input("a: "))
# b = int(input("b: "))

# grand_sum = 0
# for i in range(a, b + 1): 
#     grand_sum += S(i)
    
# print(grand_sum)

# Rekinasanas spele

m = []

def jaNegativs(n, sum): # -54, 1440
    n_simb = str(n) # '-54'
    sum_simb = str(sum) # '1440'
    
    for c in n_simb: # -, 5, 4
        sum_simb = sum_simb.replace(c, '') # '1440' -> '10'
        
    return int(sum_simb) # '10' -> 10

with open("file.txt") as f:
    for line in f.readlines():
        m.append(int(line))
        
print(m)
    
sum = 0
for elem in m:
    if elem > 0:
        sum += elem
    else:
        sum = jaNegativs(elem, sum)

print(sum)
        