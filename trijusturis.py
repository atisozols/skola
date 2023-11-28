class TPrizma:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def pamS(self):
        p = (self.a + self.b + self.c)/2
        s = (p*(p-self.a)*(p-self.b)*(p-self.c))**0.5
        return s

    def tilpums(self):
        return self.pamS() * self.h

    def sanu_virsma(self):
        return (self.a*self.h + self.b*self.h + self.c*self.h)

    def pilna_virsma(self):
        return 2*self.pamS() + self.sanu_virsma()

prizma = TPrizma(3, 4, 5, 6)
print(prizma.pilna_virsma())