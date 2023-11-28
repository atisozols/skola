# class Minute, konstruktorā viena vērtība
# minūtes intervālā 0 - 59
# iekšējā funkcija next(), kas pārlec uz 
# nākošo minūti

class Datums:
    def __init__(self, d, m):
        self.d = d
        self.m = m

    def next(self):
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
                    self.m = 1
                    self.d = 1
                else:
                    self.d = 1
                    self.m += 1
            else:
                self.d += 1

datumins = Datums(16, 3)
datumins.next()
print(datumins.d, datumins.m)
        










