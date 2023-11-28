class Taisnsturis:
    def __init__(self, a, b): #konstruktora funkcija
        self.mala1 = a
        self.mala2 = b

    def laukums(self):
        return self.mala1 * self.mala2

    def perimetrs(self):
        return 2 * (self.mala1 + self.mala2)

    def diagonale(self):
        return (self.mala1**2 + self.mala2**2)**0.5

class Cilindrs:
    def __init__(self, a, b):
        self.radiuss = a
        self.augstums = b

    def Spam(self):
        import math
        return math.pi * self.radiuss ** 2

    def tilpums(self):
        return self.augstums * self.Spam()


x = Taisnsturis(3, 6)
print(x.mala1)
print(x.laukums())
print(x.perimetrs())

y = Cilindrs(3, 2)
print(y.Spam())
print(y.tilpums())