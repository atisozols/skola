# klase - datu struktūra, blueprints,
# pēc kura tiek veidoti objekti

# objekts - datu struktūras viena instance
class ManaKlase:
    x = 10

instance1 = ManaKlase()
instance2 = ManaKlase()
instance2.x = 4
# print(instance1.x)
# print(instance2.x)

class Person:
    def __init__(self, n, s):
        self.name = n
        self.surname = s

    def fullName(self):
        return self.name + " " + self.surname

atis = Person("Atis", "Ozols")
janis = Person("Jānis", "Zariņš")


class Kvadratvienadojums:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.c = z

    def d(self):
        return self.b ** 2 - 4 * self.a * self.c

    def saknes(self):
        if self.d() > 0:
            x1 = (-self.b + (self.d()**0.5))/(2 * self.a)
            x2 = (-self.b - (self.d()**0.5))/(2 * self.a)
            return [x1, x2]
        elif self.d() == 0:
            x = (-self.b + self.d())/(2 * self.a)
            return [x]
        else:
            return []

    def zari(self):
        if self.a > 0:
            print("zari uz augšu")
        else:
            print("zari uz leju")

    def virsotne(self):
        xv = (-self.b)/(2 * self.a)
        yv = self.a * xv**2 + self.b * xv + self.c
        return [xv, yv]

        

# kv1 = Kvadratvienadojums(2, 4, 3)
# print(kv1.d())

# kv2 = Kvadratvienadojums(2, 4, 1)
# print(kv2.d())
# print(kv2.saknes())
# kv2.zari()
# print(kv2.virsotne())
# print(kv2.a)

class Paralelskaldnis:
    def __init__(self, x, y, z):
        self.a = x
        self.b = y
        self.h = z

    def pamataLaukums(self):
        return self.a * self.b
    
    def tilpums(self):
        return self.pamataLaukums() * self.h

    def pamataPerimetrs(self):
        return 2 * (self.a + self.b)

    def sanuVirsma(self):
        return self.pamataPerimetrs() * self.h

    def pilnaVirsma(self):
        return 2 * self.pamataLaukums() + self.sanuVirsma()

# Izveidot klasi Lode, kurai padod rādiusu. Uzrakstīt
# iekšējās funkcijas tilpums() un virsmasLaukums().

class Lode:
    def __init__(self, r):
        self.r = r

    def tilpums(self):
        return (4*3.14*self.r**3)/3

    def virsmasLaukums(self):
        import math
        return 4*math.pi*self.r**2


# Klase Cilindrs, kuram padod divus parametrus - pamata rādiusu un augstumu.
# Klasē ierakstīt sekojošas funkcijas - pamataLaukums(), sanuVirsma(),
# pilnaVirsma() un tilpums().

class Cilindrs:
    def __init__(self, a, b):
        self.r = a
        self.h = b
    
    def pamataLaukums(self):
        return 3.14 * self.r**2

    def tilpums(self):
        return self.pamataLaukums() * self.h

    def sanuVirsma(self):
        return 2 * 3.14 * self.r * self.h

    def pilnaVirsma(self):
        return 2 * self.pamataLaukums() + self.sanuVirsma()


# Nodemonstrēt abu klašu darbību, katrai izveidojot objektu, pielietojot visas
# iekšējās metodes jeb funkcijas

x = Lode(4)
print(x.tilpums())

y = Cilindrs(2, 5)
print(y.pilnaVirsma())

# Klase Datums, kas glabā dienu un mēnesi, kā arī divas
# iekšējās funkcijas - nextDay() un nextMonth()

class Datums:
    def __init__(self, day, month):
        if day > 0 and day < 32:
            if month > 0 and month < 13:
                if month == 2 and day < 29:
                    self.d = day
                    self.m = month
                elif month == 4 or month == 6 or month == 9 or month == 11:
                    if day < 31:
                        self.d = day
                        self.m = month
                    else:
                        self.d = 1
                        self.m = month
                else:
                    if day < 32:
                        self.d = day
                        self.m = month
                    else:
                        self.d = 1
                        self.m = month
            else:
                self.d = day
                self.m = 1
        else:
            self.d = 1
            self.m = 1

    def display(self):
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        print(months[self.m - 1], self.d)

    def nextDay(self):
        if self.m == 2:
            if self.d == 28:
                self.d = 1
                self.m += 1
            else:
                self.d += 1
            
        elif self.m == 4 or self.m == 6 or self.m == 9 or self.m == 11:
            if self.d == 30:
                self.d = 1
                self.m += 1
            else:
                self.d += 1
                
        else:
            if self.d == 31:
                if self.m == 12:
                    self.d = 1
                    self.m = 1
                else:
                    self.d = 1
                    self.m += 1
            else:
                self.d += 1

    def nextMonth(self):
        for i in range(30):
            self.nextDay()

dzimene = Datums(16, 3)
dzimene.nextMonth()
dzimene.display()


class Skolens:
    def __init__(self, v, u, matematika = [], latviesuValoda = [], programmesana = []):
        self.vards = v
        self.uzvards = u
        self.matematika = matematika
        self.latviesuValoda = latviesuValoda
        self.programmesana = programmesana

    def matvid(self):
        return sum(self.matematika)/len(self.matematika)

    def latvvid(self):
        return sum(self.latviesuValoda)/len(self.latviesuValoda)

    def progvid(self):
        return sum(self.programmesana)/len(self.programmesana)

    def vid(self):
        return (self.matvid() + self.progvid() + self.latvvid())/3

janis = Skolens("Jānis", "Pretkalniņš", [6, 8, 3], [10, 10], [5, 4, 4])
print(janis.vid())

class Skolens_v2: # šis ir labāks risinājums par v1
    def __init__(self, v, u, atzimes = []):
        self.vards = v
        self.uzvards = u
        self.atzimes = atzimes

    def addSubject(self):
        self.atzimes.append([])

    def addGrade(self, prieksmets, atzime):
        self.atzimes[prieksmets].append(atzime)

    def average(self, prieksmets):
        return sum(self.atzimes[prieksmets])/len(self.atzimes[prieksmets])
        
    def fullAverage(self):
        sum = 0
        len = 0
        for row in self.atzimes:
            for elem in row:
                sum += elem
                len += 1
        return sum / len

x = Skolens_v2("Jānis", "Zariņš")
x.addSubject()
x.addGrade(0, 8)
x.addSubject()
x.addGrade(0, 9)
x.addGrade(1, 7)
x.addGrade(1, 5)
x.addSubject()
print(x.atzimes)
print(x.average(1))
print("Average: ", x.fullAverage())



# Klase TrijsturaPrizma, kur konstruktorā padod
# masīvu ar malu garumiem un augstumu 
# (2 vērtības - masīvs un garums). 
# Iekšējās funkcijas pamata laukumam, 
# tilpumam, virsmas laukumam.

class TrijsturaPrizma:
    def __init__(self, augstums, malas = []):
        self.h = augstums
        self.malas = malas

    def pamataLaukums(self):
        p = (self.malas[0] + self.malas[1] + self.malas[2]) / 2
        for mala in self.malas:
            p *= (p - mala)

        s = p ** 0.5
        return s

    def tilpums(self):
        return self.pamataLaukums() * self.h

    def virsmasLaukums(self):
        perimetrs = 0
        for mala in self.malas:
            perimetrs += mala
        sanuVirsma = perimetrs * self.h
        return 2 * self.pamataLaukums() + sanuVirsma