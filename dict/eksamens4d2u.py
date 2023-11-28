# faila apstrade, teksta saglabasana
text = ''

with open('4d2u.txt') as f:
    text = f.read() # f.readlines(), f.readline()

# teksta sadalisana vardos
simboli = ".,?!;:()[]}{-_<>`~"
text = text.lower()
for simb in simboli:
    text = text.replace(simb, '')
    
text = text.split()

# izveidot vardnicu, kur uzskaitam vardu biezumu

dic = {}

for word in text:
    dic[word] = text.count(word)
    
sorted_dic = sorted(dic, key=dic.get, reverse=True)
print(sorted_dic[:5])
