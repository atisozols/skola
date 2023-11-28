class Taisnsturis:
    def __init__(self, a, b): # konstruktora funkcija iedod klases instancei(vienam taisnsturim) sakotnejas vertibas
        self.mala1 = a
        self.mala2 = b

    def laukums(self):
        return self.mala1 * self.mala2


x = Taisnsturis(4, 5)
y = Taisnsturis(6, 8)

print(x.mala1, y.laukums())

class Person:
    def __init__(self, n, s, age):
        self.name = n
        self.surname = s
        self.age = age

    def full_name(self):
        return self.name + ' ' + self.surname

atis = Person('Atis', 'Ozols', 21)
print(atis.surname)
print(atis.full_name())
print(atis.age)
atis.age += 1
print(atis.age)
        