# Klase ToDoList, kur konstruktora iedod 1 
# vertibu - daramo lietu skaitu.
# iekš funkcija Check, pēc kuras darāmo
#  lietu skaits paliek par vienu mazaks
# Kad darbu skaits ir 0, print 'done'

class ToDoList:
    def __init__(self, a):
        self.skaits = a

    def Check(self):
        self.skaits -= 1
        if self.skaits == 0:
            print('done')

x = ToDoList(3)
x.Check()
x.Check()
x.Check()
