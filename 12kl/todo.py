import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

conn = sqlite3.connect("todo.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Todo (id INTEGER PRIMARY KEY, name VARCHAR, date DATE)")
conn.commit()
conn.close()

def insert(n, s):
  if len(n) < 1 or len(s) < 1:
    messagebox.showwarning(message="One or both values are empty!")
  else:
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS Todo (id INTEGER PRIMARY KEY, name VARCHAR, date DATE)")
    cursor.execute("INSERT INTO Todo(name, date) VALUES (?, ?)", (n, s))
    conn.commit()
    conn.close()
    messagebox.showinfo(message="Success! Data saved!")
    task.delete(0, END)
    deadline.delete(0, END)
    print(n, s)
  display()
    
def display(favorites=False):
  tree.delete(*tree.get_children())
  conn = sqlite3.connect("todo.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Todo ORDER BY date")
  tasks = cursor.fetchall()
  for task in tasks:
    tree.insert('', 'end', values=(task[1], task[2]))
  conn.close()
      
def done():
  treeIndex = tree.focus()
  item = tree.item(treeIndex)
  taskName = item["values"][0]
  print([taskName])
  conn = sqlite3.connect("todo.db")
  cursor = conn.cursor()
  cursor.execute("DELETE FROM Todo WHERE name=?", [taskName])
  conn.commit()
  conn.close()
  display()
  
def accept(id, value):
  conn = sqlite3.connect("todo.db")
  cursor = conn.cursor()
  cursor.execute("UPDATE Todo SET name=? WHERE id=?", (value, id))
  conn.commit()
  conn.close()
  display()
  editWindow.destroy()
  window.deiconify() ######## atver logu
  
def edit():
  treeIndex = tree.focus()
  if treeIndex:
    window.withdraw() ####### paslēpj logu
    item = tree.item(treeIndex)
    taskName = item["values"][0]
    
    global editWindow
    editWindow = Tk()
    editWindow.geometry("250x100")
    editLabel = Label(editWindow, text="Task")
    editLabel.place(x=30, y=30)
    edit = Entry(editWindow)
    edit.place(x=70, y=30)
    edit.insert(0, taskName)
    editWindow.protocol("WM_DELETE_WINDOW", lambda: accept(id, edit.get()))
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM Todo WHERE name=?", [taskName])
    id = cursor.fetchone()[0]
    conn.close()
    
    okButt = Button(editWindow, text="Ok", command= lambda: accept(id, edit.get()))
    okButt.place(x=40, y=60)
    
    editWindow.mainloop()

def export():
  conn = sqlite3.connect("todo.db")
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM Todo")
  records = cursor.fetchall()
  with open("todo.csv", "w", encoding="UTF-8") as f:
    writer = csv.writer(f)
    for record in records:
      writer.writerow(record)
  conn.close()
  messagebox.showinfo(message="Data saved to todo.csv!")
  
def load():
  conn = sqlite3.connect("todo.db")
  cursor = conn.cursor()
  with open("todo.csv") as backup:
    reader = csv.reader(backup)
    
    for row in reader:
      if len(row) == 3:
        cursor.execute("INSERT INTO Todo(id, name, date) VALUES (?, ?, ?)", (int(row[0]), row[1], row[2]))
        conn.commit()
  conn.close()
  messagebox.showinfo(message="Success! Load successful!")
  display()

# Window config
window = Tk()
window.geometry("500x400")
window.title("Datubaze")
window.resizable(False, False)

taskLabel = Label(text="Task")
taskLabel.place(x=30, y=30)

deadlineLabel = Label(text="Deadline (YYYY-MM-DD)")
deadlineLabel.place(x=30, y=70)

task = Entry()
deadline = Entry()

task.place(x=100, y=30)
deadline.place(x=200, y=70)

butt = Button(text="Save", command= lambda: insert(task.get(), deadline.get()))
butt.place(x=130, y=100)

doneButt = Button(text="Done", command= lambda: done())
doneButt.place(x=200, y=180)

editButt = Button(text="Edit", command= lambda: edit())
editButt.place(x=160, y=180)

exportButt = Button(text="Export", command=export)
exportButt.place(x=250, y=180)

exportButt = Button(text="Load", command=load)
exportButt.place(x=300, y=180)

tree = ttk.Treeview(window, column=("c1", "c2"), show='headings', height=8)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Task")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Deadline")

tree.pack(side=BOTTOM)

display()
window.mainloop()