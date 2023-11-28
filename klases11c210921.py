class TPrizma:
    def __init__(self, a, b, c, h):
        self.a = a
        self.b = b
        self.c = c
        self.h = h

    def pamataLaukums(self):
        p = (self.a + self.b + self.c) / 2
        a = p*(p-self.a)*(p-self.b)*(p-self.c)
        return a**0.5

    def tilpums(self):
        return self.pamataLaukums() * self.h

    def sanuVirsma(self):
        return (self.h*self.a) + (self.h*self.b) + (self.h*self.c)

    def pilnaVirsma(self):
        return 2*self.pamataLaukums() + self.sanuVirsma()


prizma = TPrizma(3, 4, 5, 6)
print(prizma.pamataLaukums())
print(prizma.tilpums())
print(prizma.sanuVirsma())
print(prizma.pilnaVirsma())

