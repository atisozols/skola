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
