sv = "Their first stable line-up was comprised of vocalist Mick Jagger, multi-instrumentalist Brian Jones, guitarist Keith Richards, bassist Bill Wyman, and drummer Charlie Watts. During their formative years Jones was the primary leader: he assembled the band, named it, and drove their sound and image."
sv1 = "divdesmit pieci lati"

m1 = "atis" # ['a', 't', 'i', 's']
m2 = "ozols"

sv3 = m1 + m2

# 1. Izmantojot count() funkciju, noteikt vārdu skaitu simbolu virknē.

# print("simbolu virknē ir", sv.count(" ") + 1, "vārdi")

# 2. Tādā pašā veidā noteikt teikumu skaitu.

# print("simbolu virknē ir", sv.count(".") + sv.count("?") + sv.count("!"), "teikumi")

# 3. Veikt abus pirmos uzdevumus bez funkcijas pielietošanas.

wordCount = 1
sentenceCount = 0
for c in sv:
    if c == " ":
        wordCount += 1
    elif c == "." or c == "?" or c == "!":
        sentenceCount += 1


# 4. Izmantojot split() funkciju, izveidot masīvu no vārdiem simbolu virknē.

masivs = sv.split(" ")

# 5. To pašu veikt bez funkcijas.

m = []
word = ""
for c in sv:
    if c != " ":
        word += c
    else:
        m.append(word)
        word = ""
m.append(word)


# 6. izmantojot replace funkciju, aizvietot visus a ar x.

sv = "divas stundas"
sv_copy = sv.replace("a", "x")

# 7. izmantojot replace, parveidot simbolu virkni pupiņu valodā.
# a e i o u

m = "aeiou" 
sv = "divas stundas un tris minutes"
for c in m:
    sv = sv.replace(c, c + "p" + c) 

# 8. tekstā/simbolu virknē tikt vaļā no liekām atstarpēm
# (divas                stundas -> divas stundas)

sv = "divas       stundas   un             tris  minutes"
while sv.count("  ") > 0:
    sv = sv.replace("  ", " ")

m = sv.split(" ")
sv = ""
for word in m:
    sv += word + " "

# 9. izdrukā tekstu pa vienam simbolam.

sv = "divAs StuNDAs un Tris MINUtes"
# for c in sv:
#     print(c, end="_")
# print()

# 10. izdrukā teksta abreviatūru 
# (divas stundas un tris minutes -> dsutm)

abr = sv[0]
for i in range(len(sv)):
    if i != 0:
        if sv[i - 1] == " ":
            abr += sv[i]
# print(abr)

# 11. parveido tekstu capitalized formā
# (divAs STUndas un tRIS MINUTES -> Divas Stundas Un Tris Minutes)

cap = ""
for i in range(len(sv)):
    if i == 0:
        if ord(sv[i]) > 59 and ord(sv[i]) < 91:
            cap += sv[i]
        elif ord(sv[i]) > 64 and ord(sv[i]) < 123:
            cap += chr(ord(sv[i]) - 32)
    elif i != 0:
        if sv[i - 1] == " ":
            cap += " "
            if ord(sv[i]) > 59 and ord(sv[i]) < 91:
                cap += sv[i]
            elif ord(sv[i]) > 64 and ord(sv[i]) < 123:
                cap += chr(ord(sv[i]) - 32)
        else:
            if ord(sv[i]) > 59 and ord(sv[i]) < 91:
                cap += chr(ord(sv[i]) + 32)
            elif ord(sv[i]) > 64 and ord(sv[i]) < 123:
                cap += sv[i]

# 12. parveido tekstu atbilstoši teikuma noformejumam.
# ( divas  STUNDAS   ,  Tris minUTES . divi Celieni   . 
# -> Divas stundas, tris minutes. Divi celieni. )  

sv = "divas    STUNDAS   ,  Tris minUTES . divi Celieni   .   skola."
while sv.count("  ") > 0:
    sv = sv.replace("  ", " ")

pieturzimes = ".,?!:;"
for zime in pieturzimes:
    sv = sv.replace(" " + zime, zime)

cap = ""
for i in range(len(sv)):
    if i == 0:
        if ord(sv[i]) > 64 and ord(sv[i]) < 91:
            cap += sv[i]
        elif ord(sv[i]) > 64 and ord(sv[i]) < 123:
            cap += chr(ord(sv[i]) - 32)
        else:
            cap += sv[i]
    else:
        if ord(sv[i]) > 64 and ord(sv[i]) < 91:
                cap += chr(ord(sv[i]) + 32)
        elif ord(sv[i]) > 64 and ord(sv[i]) < 123:
            if i > 1:
                if sv[i - 2] == ".":
                    cap += chr(ord(sv[i]) - 32)
                else:
                   cap += sv[i] 
            else:
                cap += sv[i]
        else:
            cap += sv[i]
print(cap)

# teikumu skaits un vārdu skaits

# teik = input("ievadi tekstu: ")

# print(teik.count(" ") + 1)
# print(teik.count('.') + teik.count('!') + teik.count('?'))

# w = 1
# t = 0

# for c in teik:
#     if c == " ":
#         w += 1
#     elif c == "." or c == "!" or c == "?":
#         t += 1

# funkcija, true/false atkarībā no tā, vai simbols ir lielais burts

# def isCapital(c):
#     if ord(c) > 64 and ord(c) < 91:
#         return True
#     else:
#         return False

# no simbolu virknes izvadīt tikai lielos burtus

# sv = "AsRtUUUErwtv"
# for c in sv:
#     if isCapital(c):
#         print(c, end=" ")

# with open("simbolu_virkne1.txt") as file:
#     # print(file.read())
#     # print(file.readline())
#     m = file.readlines()
#     for line in m:
#         print(line, end="")

# with open("simbolu_virkne2.txt", "w") as file:
#     for i in range(10):
#         file.write(str(i))

# f = open("simbolu_virkne2.txt")
# f.close()

# programma, kas no faila izdrukā pa vienam vārdam

# with open("simbolu_virkne2.txt") as file:
#     text = file.read()
#     masivs = text.split(' ')
#     for vards in masivs:
#         print(vards)

# programma, kas failā atrod garāko vārdu

# with open("simbolu_virkne2.txt") as file:
#     text = file.read()
#     masivs = text.split(' ')
#     max_garums = 0
#     garakais_vards = ''
#     for vards in masivs:
#         if len(vards) >= max_garums:
#             max_garums = len(vards)
#             garakais_vards = vards
#     print(garakais_vards)

# programma, kas pieprasa trīs reizes ievadīt vārdu un uzvārdu
# un izveido trīs atsevišķus failus, kur tos ieraksta

# for i in range(3):
#     vu = input("ievadi: ")
#     with open(str(i) + ".txt", "w") as file:
#         file.write(vu)

# failā ir ierakstīts teksts
# pārbaudīt, vai failā ierakstītais ir epasts

with open("epasts.txt") as f:
    text = f.read()
    at = False
    pirma = ''
    otra = ''
    for c in text:
        if c == '@':
            at = True
        elif at:
            otra += c
        else:
            pirma += c
    print(pirma, otra)

    if len(pirma) < 66 and len(otra) < 256 and text[-1] != '.' and len(otra) > 0 and otra.count('.') > 0 and len(pirma) > 0 and text.count('@') == 1:
        print("DERIGS")
    else:
        print("NEDERIGS")

# Lietotājs ievada faila nosaukumu un rindiņas, 
# cik programmai jānolasa no faila

# nosaukums = input("faila nosaukums: ")
# skaits = int(input("cik rindinas nolasit: "))

# with open(nosaukums) as file:
#     for i in range(skaits):
#         print(file.readline())

# programma, kas pa vienam simbolam
# izdrukā faila saturu uz ekrāna

# with open("simbolu_virkne1.txt") as f:
#     # len = len(f.read())
#     # f.seek(0)
#     # for i in range(len):
#     #     print(f.read(1), end=" ")
#     for c in f.read():
#         print(c)


# programma, kas nokopē viena faila
# saturu jaunā failā

# with open("simbolu_virkne1.txt") as f:
#     saturs = f.read()
#     with open("copy.txt", "w") as copy:
#         copy.write(saturs)

# programma, kas otrā failā ieraksta
# tikai pirmā faila garāko vārdu

with open("simbolu_virkne1.txt") as f:
    saturs = f.read()
    saturs = saturs.replace("\n", " ")
    m = saturs.split(" ")
    print(m)
    gar = m[0]
    for vards in m:
        if len(vards) > len(gar):
            gar = vards

    with open("copy.txt", "w") as copy:
        copy.write(gar)

# paroles validācija - lielais, 
# cipars, simbols(.!?#$*@^&*), 
# min len = 8

def isCapital(c):
    if ord(c) > 64 and ord(c) < 91:
        return True
    else:
        return False

def isNumber(c):
    if ord(c) > 47 and ord(c) < 58:
        return True
    else:
        return False


# with open("jauns.txt") as f:
#     with open("jauns_copy.txt", "w") as b:
#         m = f.readlines()
#         for r in m:
#             r = r.replace("\n", "")
#             arr = r.split(" ")
#             b.write(arr[0] + " ")
#             for i in range(len(arr) - 1, 0, -1):
#                 b.write(arr[i] + " ")
#             b.write("\n")

# sv = "tukuma     raina     valsts      gimnazija"
# while sv.count("  ") > 0:
#     sv = sv.replace("  ", " ")

# print(sv)


neburtu = ".,!?:;()"
sv = "(pie!?kt.die,na)"

sv1 = ""
for c in sv:
    if neburtu.count(c) == 0:
        sv1 += c


print(sv1)