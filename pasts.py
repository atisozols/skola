sv = "suunuciems riiga ventspils daugavpils valmiera valka riiga vecteetinjam saldus valka roja riiga"

vietas = []
word = ""
for c in sv:
    if c != " ":
        word += c
    else:
        if len(vietas) == 0:
            vietas.append(word)
        else:
            poz = 0
            while poz < len(vietas)-1 and word[0] > vietas[poz][0]:
                poz += 1
            vietas.insert(poz, word)
        word = ""
        print(vietas)
poz = 0
while poz < len(vietas)-1 and word[0] > vietas[poz][0]:
    poz += 1
vietas.insert(poz, word)

print(vietas)

    