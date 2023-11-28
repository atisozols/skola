# Funkcija - koda fragments, kurš var tikt atkārtoti izsaukts

# 1. Funkcija, kas atgriež vārdu skaitu tekstā

# text1 = "tukuma raina valsts gimnazija"
# text2 = "torentu pavelnieks"

# def wordCount(text):
#   vardu_skaits = text.count(" ") + 1
#   return vardu_skaits

# print(wordCount(text1))
# print(wordCount(text2))

# 2. Funkcija, kas atgriež True vai False atkarībā
# no tā, vai padotais vecums ir vismaz 18

# def pilngadigs(vecums):
#   if vecums < 18:
#     return False
#   else:
#     return True


# gadi = int(input("cik tev gadu? "))
# if pilngadigs(gadi):
#   print('pilngadigs')

# 3. Funkcija, kas nosaka, vai padotais gads ir garais vai nē.

# def isLeapYear(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return False
#       else:
#         return True
#     else:
#       return True
#   else:
#     return False

# 4. Funkcija, kas aprēķina masīva amplitūda

def amplituda(masivs):
  max = masivs[0]
  min = masivs[0]
  
  for elem in masivs:
    if elem > max:
      max = elem
      
    if elem < min:
      min = elem
  
  return max - min

# 5. Funkcija, kurai padod masīva garumu. 
# Tiek atgriezts masīvs ar nejauši ģenerētiem skaitļiem tādā garumā

import random

def randArray(length):
  arr = []
  
  for _ in range(length):
    val = random.randint(1, length)
    while arr.count(val) > 0:
      val = random.randint(1, length)
    arr.append(val)
    
  return arr

# 6. Funkcija, kas pārbauda, vai masīvs ir augošā secībā

def augoss(m):
  i = 0
  while i + 1 < len(m):
    if m[i] > m[i + 1]:
      return False
    i += 1
  return True

# 7. Funkcija, kas sakārto masīvu dilstošā secībā.

def sortedArray(m):
  sorted = []

  for i in range(len(m)):
      poz = 0
      if len(sorted) == 0:
          sorted.insert(poz, m[i])
      else:
          while len(sorted) > poz and m[i] < sorted[poz]:
              poz += 1
          sorted.insert(poz, m[i])
          
  return sorted

# print(sortedArray([1, 5, 2, 6, 3]))

# 8. Funkcija, kas padotai simbolu virknei atgriež garāko vārdu.

def longestWord(txt):
  words = txt.split(" ")
  longest = words[0]
  
  for word in words:
    if len(word) > len(longest):
      longest = word
      
  return longest

# print(longestWord("tukuma raina valsts gimnazijas dargie skoleni"))
  
# 9. Rekursija.

def f(n):
  if n == 1:
    return 1
  elif n == 0:
    return 0
  else:
    return f(n - 1) + f(n - 2)
    
# print(f(25))


# Klase - šablons (blueprint) pēc kura strukturējas dati un metodes.
# Objekts - viena klases instance
# Konstruktors - klases iekšējā funkcija, kas piešķir objektam sākotnējos datus

# 10. Klase Paralelskaldnis, kura konstruktorā saņem trīs vērtības - šķautņu garumus.
#     Iekšējās metodes/funkcijas - tilpums(), virsmasLaukums().

class Paralelskaldnis:
  def __init__(self, x, y, z): # Konstruktors __init__
    self.a = x # Konstruktoram padotā x vērtība tiek ierakstīta objekta iekšējā mainīgajā a
    self.b = y
    self.c = z
    
  def tilpums(self):
    return self.a * self.b * self.c
    
  def virsmasLaukums(self):
    return (self.a * self.b + self.a * self.c + self.b * self.c) * 2
    
paralel1 = Paralelskaldnis(2, 4, 5) # Klases instances jeb objekta izveide

# print(paralel1.a) # iekšējā mainīgā a izvade

# print(paralel1.virsmasLaukums()) # iekšējās funkcijas virsmasLaukums() izsaukums

# 11. Klase Cilindrs

class Cilindrs:
  def __init__(self, rad, augst):
    self.r = rad
    self.h = augst
    
  def pamataLauk(self):
    return self.r ** 2 * 3.14159265
  
  def tilpums(self):
    return self.pamataLauk() * self.h
  
  def virsmasLauk(self):
    return 2 * self.pamataLauk() + 2 * 3.14159265 * self.r
  
# cil1 = Cilindrs(3, 6)
# print(cil1.tilpums())
# print(cil1.virsmasLauk())

# 12. Klase Kvadratvienadojums

class Kvadratvienadojums:
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
    
  def diskriminants(self):
    return self.b ** 2 - 4 * self.a * self.c
  
  def saknes(self):
    if self.diskriminants() > 0:
      x1 = (-self.b + self.diskriminants() ** 0.5) / (2 * self.a)
      x2 = (-self.b - self.diskriminants() ** 0.5) / (2 * self.a)
      return [x1, x2]
    elif self.diskriminants() == 0:
      x = (-self.b) / (2 * self.a)
      return [x]
    else:
      return []
    
  def virsotne(self):
    x = (-self.b) / (2 * self.a)
    y = self.a * x ** 2 + self.b * x + self.c
    return [x, y]
  
# kvd = Kvadratvienadojums(0.5, 2, 8)
# print(kvd.saknes(), kvd.virsotne())

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  def distanceTo(self, point):
    deltaX = abs(self.x - point.x)
    deltaY = abs(self.y - point.y)
    return (deltaX ** 2 + deltaY ** 2) ** 0.5
  


class Trijsturis:
  def __init__(self, p1, p2, p3):
    self.m1 = p1.distanceTo(p2) 
    self.m2 = p2.distanceTo(p3) 
    self.m3 = p1.distanceTo(p3)
    
  def perimetrs(self):
    return self.m1 + self.m2 + self.m3
    
  def laukums(self):   
    p = self.perimetrs() / 2
    s = (p * (p - self.m1) * (p - self.m2) * (p - self.m3)) ** 0.5
    return s
 
p1 = Point(4, 4)
p2 = Point(8, 4)
p3 = Point(4, 7)
  
mansTrijsturs = Trijsturis(p1, p2, p3)
# print(mansTrijsturs.laukums())

class Circle:
  def __init__(self, point, radius):
    self.centre = point
    self.r = radius
    
  def overlaps(self, anotherCircle):
    if self.centre.distanceTo(anotherCircle.centre) > self.r + anotherCircle.r:
      return False
    else:
      return True
  
c1 = Circle(p2, 2)
c2 = Circle(p3, 1)

# print(c1.overlaps(c2))
    
# BankAccount klase, kurai konstruktorā padod sākotnējo 
# bilanci un eksistē metodes deposit(amount) un withdraw(amount)
# getBalance()

class BankAccount:
  def __init__(self, pin):
    self.pin = pin
    self.balance = 0
    
  def getBalance(self):
    print("getting balance")
    pinKods = int(input("PIN: "))
    if pinKods == self.pin:
      return self.balance
    else:
      print("Wrong PIN")
  
  def withdraw(self, amount):
    if amount > self.getBalance():
      print("insufficient funds")
    else:
      self.balance -= amount # self.balance = self.balance - amount
      print("withdraw", amount)
      
  def deposit(self, amount):
    print("deposited", amount)
    self.balance += amount

# myAccount = BankAccount(1111)

# myAccount.deposit(100)

# print(myAccount.getBalance())

# myAccount.withdraw(200)

# Pievieno PIN funkcionalitāti - konstruktorā padod PIN kodu un
# darbības tiek veiktas pēc PIN ievades

# Klase Datums, kur konstruktorā ir divas vērtības - diena un mēnesis.
# Iekšējā funkcija next(), kas nomaina šīs divas vērtības atbilstoši kalendāram

class Date:
  def __init__(self, day, month):
    self.d = day
    self.m = month
    
  def next(self):
    if self.m == 2:
      if self.d == 28:
        self.m += 1
        self.d = 1
      else:
        self.d += 1
    elif [4, 6, 9, 11].count(self.m) > 0:
      if self.d == 30:
        self.m += 1
        self.d = 1
      else:
        self.d += 1
    else:
      if self.d == 31:
        if self.m == 12:
          self.m = 1
          self.d = 1
        else:
          self.m += 1
          self.d = 1
      else:
        self.d += 1
  
  def __str__(self):
      return "{0}/{1}".format(self.d, self.m)
    
d = Date(31, 12)
d.next()
print(d)
      

# Klase Vektors

class Vektors:
    def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

    def __str__(self):
      return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
      x = self.x + other.x
      y = self.y + other.y
      return Vektors(x, y)
      
    def __sub__(self, other):
      x = self.x - other.x
      y = self.y - other.y
      return Vektors(x, y)
          
    def __mul__(self, n):
      x = self.x * n
      y = self.y * n
      return Vektors(x, y)
    
v1 = Vektors(4, 3)
v2 = Vektors(1, 1)

v3 = v1 * 2

# print(v3)
    
    
  
    