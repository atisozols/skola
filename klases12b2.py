class Taisnsturis:
    def __init__(self, a, b):
        self.mala1 = a
        self.mala2 = b

    def laukums(self):
        return self.mala1 * self.mala2

    def perimetrs(self):
        return 2 * (self.mala1 + self.mala2)

x = Taisnsturis(4, 6)
print(x.laukums())
print(x.perimetrs())