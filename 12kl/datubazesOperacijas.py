from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

def insert(n, s):
  if len(n) < 1 or len(s) < 1:
    messagebox.showwarning(message="One or both values are empty!")
  else:
    conn = sqlite3.connect("datubaze.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS People (id INTEGER PRIMARY KEY, name VARCHAR, surname VARCHAR)")
    cursor.execute("INSERT INTO People(name, surname) VALUES (?, ?)", (n, s))
    conn.commit()
    conn.close()
    messagebox.showinfo(message="Success! Data saved!")
    name.delete(0, END)
    surname.delete(0, END)
  display()
    
def display():
  tree.delete(*tree.get_children())
  conn = sqlite3.connect("datubaze.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM People")
  people = cursor.fetchall()
  for person in people:
    tree.insert('', 'end', values=(person[1], person[2]))
  conn.close()
    

# Window config
window = Tk()
window.geometry("500x400")
window.title("Datubaze")
window.resizable(False, False)

nameLabel = Label(text="Name")
nameLabel.place(x=30, y=30)

surnameLabel = Label(text="Surname")
surnameLabel.place(x=30, y=70)

name = Entry()
surname = Entry()

name.place(x=100, y=30)
surname.place(x=100, y=70)

butt = Button(text="Save", command= lambda: insert(name.get(), surname.get()))
butt.place(x=130, y=100)

tree = ttk.Treeview(window, column=("c1", "c2"), show='headings', height=8)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Surname")

tree.pack(side=BOTTOM)


display()
window.mainloop()