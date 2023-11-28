stacijas = {}
with open("stacijas.txt") as f:
  first = f.readline().split()
  staciju_count = int(first[0])
  savien_count = int(first[1])
  for i in range(staciju_count):
    stacijas[i + 1] = []
    
  for _ in range(savien_count):
    savien = f.readline().split()
    pietura0 = int(savien[0])
    pietura1 = int(savien[1])
    stacijas[pietura0].append(pietura1)
    stacijas[pietura1].append(pietura0)
    
  print(stacijas)
  
a = int(input("a: "))
b = int(input("b: "))

soli = 1
kaimini = stacijas[a]

# while apstājas, kad sasniedz galamērķi vai kad vairs netiek dziļāk 

while kaimini.count(b) < 1:
  print(kaimini)
  soli += 1
  nakamieKaimini = []
  
  for kaimins in kaimini:
    nakamieKaimini += stacijas[kaimins]
  
  if set(kaimini) == set(nakamieKaimini):
    break
  
  kaimini = list(set(nakamieKaimini))

print(kaimini)
print(soli)

