dic = { # key: value
        "name": "Atis",
        10: 32
    }

dic["surname"] = "Ozols"

print(dic)

# Dots masīvs m. Izveidot vārdnīcu, kur glabājas
# key-value pāri: masīva elements - elementa biežums

# dic = {}

# m = [1, 3, 5, 3, 2, 8, 3, 1, 8, 5, 5, 4, 2]

# for elem in m:
#     dic[elem] = m.count(elem)
    
# print(dic) # {1: 2, 3: 3, 5: 3, 2: 2, 8: 2, 4: 1}

# Lietotājs ievada tekstu. Izveido vārdnīcu, kur glabājas
# teksta vārdi un tie garumi. (Piemēram, "skola": 5)

dic = {}

text = input("teksts: ")
text = text.split()

for word in text:
    dic[word] = len(word)
    
print(dic['gimnazija'])