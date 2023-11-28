

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
                    self.d = 1
                    self.m = 1
                else:
                    self.d = 1
                    self.m += 1
            else: 
                self.d += 1

    def print_date(self):
        print(self.d, '/', self.m)

datumins = Datums(27, 12)
datumins.print_date()
for i in range(31):
    datumins.next()
datumins.print_date()

