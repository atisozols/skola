from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def helloWorld():
  print(name["text"])
  name.config(text=a.get())
  
# Window config
window = Tk()
window.geometry("400x600")
window.title("Ievads")
window.config(background="#8f5794")

# Label
name = Label(window,
             font=("Comic Sans", 20),
             text="",
             background="#8f5794",
             foreground="white"
             )

name.place(x=10, y=10)

# Button
hello = Button(window,
             font=("Comic Sans", 20),
             text="press",
             background="#8f5794",
             foreground="white",
             activebackground="white",
              activeforeground="#8f5794",
             command=helloWorld
             )

hello.place(x=10, y=70)

# Entry
a = Entry(window,
          font=("Comic Sans", 20),
          fg="white",
          bg="#8f5794")

a.place(x=10, y=300)

# Run
window.mainloop()