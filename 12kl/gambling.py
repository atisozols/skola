# Ievadlauks un poga. Mēģinām uzminēt skaitli no 1 līdz 10. Jebkurā situācijā parādās paziņojums

from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def guess():
  import random
  x = random.randint(1, 10)
  sk = int(a.get())
  
  if x == sk:
    result.config(text="True")
  else:
    result.config(text="False")
  

# Window config
window = Tk()
window.geometry("200x200")
window.title("Guess")
window.config(background="white")

a = Entry(window,width=30)

a.place(x=10, y=20)

hello = Button(window,
             font=("Comic Sans", 20),
             text="press",
             background="#8f5794",
             foreground="white",
             activebackground="white",
              activeforeground="#8f5794",
             command=guess
             )

hello.place(x=50, y=60)

result = Label(window,
             font=("Comic Sans", 20),
             text="False",
             background="#8f5794",
             foreground="white"
             )

result.place(x=60, y=120)

window.mainloop()