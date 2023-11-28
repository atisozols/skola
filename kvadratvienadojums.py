class Kvadratvienadojums:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def diskriminants(self):
        d = self.b**2 - 4 * self.a * self.c
        return d

    def sakne1(self):
        return (-self.b + self.diskriminants()**0.5) / (2 * self.a)

    def sakne2(self):
        return (-self.b - self.diskriminants()**0.5) / (2 * self.a)

vienadojums = Kvadratvienadojums(4, 6, 2) 
print(vienadojums.sakne1())   
print(vienadojums.sakne2())  
