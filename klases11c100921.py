# class Taisnturis:
#     def __init__(self, a, b):
#         self.mala1 = a
#         self.mala2 = b

#     def laukums(self):
#         return self.mala1 * self.mala2

#     def perimetrs(self):
#         return 2 * (self.mala1 + self.mala2)



# t = Taisnturis(3, 5)
# h = Taisnturis(6, 9)

# print(t.laukums())
# print(t.perimetrs())

# print(h.laukums())
# print(h.perimetrs())


# class Datums:
#     def __init__(self, d, m):
#         if d < 1 or d > 31:
#             print('diena nav pareiza')
#             self.day = 1
#         else:
#             self.day = d

#         if m < 1 or m > 12:
#             print('menesis nav pareizs')
#             self.month = 1
#         else:
#             self.month = m

#     def fullDate(self):
#         return str(self.day) + "/" + str(self.month)

#     def nextDay(self):
#         self.day += 1

# a = Datums(16, 3)
# print(a.fullDate())
# a.nextDay()
# print(a.fullDate())


class Laiks:
    def __init__(self, m, s):
        self.minutes = m
        if s < 1 or s > 59:
            print('sekundes nav pareizas')
            self.seconds = 1
        else:
            self.seconds = s
    
    def nextSecond(self):
        if self.seconds < 59:
            self.seconds += 1 # seconds = seconds + 1
        else:
            self.seconds = 0
            self.minutes += 1

    def printLaiks(self):
        if self.seconds < 10:
            print(str(self.minutes) + ":0" + str(self.seconds))
        else:
            print(str(self.minutes) + ":" + str(self.seconds))
        

l = Laiks(3, 58)
l.printLaiks()
l.nextSecond()
l.printLaiks()
l.nextSecond()
l.printLaiks()
l.nextSecond()
l.printLaiks()
l.nextSecond()
