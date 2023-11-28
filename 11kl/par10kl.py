# Ievada n. Izvadīt n-to nepāra skaitli

# h = int(input("h: "))
# w = -1

# for _ in range(h):
#     w += 2
    
# Simetriska simbolu eglīte augstumā h

# s = w - h
# b = s + 1
# for i in range(h):
#     for j in range(w):
#         if j >= s and j < b:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     s -= 1
#     b += 1
    
#     print()
    
# Rombs augstumā 2h - 1

# s = w - h
# b = s + 1
# apaksa = False
# for i in range(2 * h + 1):
#     for j in range(w):
#         if j >= s and j < b:
#             print("*", end="")
#         else:
#             print(" ", end="")
            
#     if s == 0:
#       apaksa = True
      
#     if apaksa: # sis izpildas, kad esam parsniegusi centru
#       s += 1
#       b -= 1
#     else: # sis notiek no augsas lidz centram
#       s -= 1
#       b += 1
    
#     print()
    

# FV

# Ievadīts a un b, kur b ir vismaz a.
# Abus galus ieskaitot, nepieciešams šī intervāla katram naturālam 
# skaitlim iegūt tā dalītāju summu un šīs summas saskaitīt kopsummā.

# Piemērs: a = 6, b = 10, rezultāts = 66

# 6 dalās ar 1, 2, 3, 6 - summā 12
# 7 dalās ar 1, 7 - summā 8
# 8 dalās ar 1, 2, 4, 8 - summā 15
# 9 dalās ar 1, 3, 9 - summā 13
# 10 dalās ar 1, 2, 5, 10 - summā 18

# 12 + 8 + 15 + 13 + 18 = 66

# a = int(input("a: "))
# b = int(input("b: "))
# sum = 0
# for i in range(a, b + 1):
#   for d in range(1, i + 1):
#     if i % d == 0:
#       sum += d 
# print(sum)

# Dots masīvs no skaitļiem dažādā izmērā. Programma izrēķina visu ciparu summu masīvā.

m = [12, 3, 652, 81, 0, 32] # 33
sum = 0
for elem in m:
  for dig in str(elem):
    sum += int(dig)
    
print(sum)


    
    