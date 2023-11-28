from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


# --------------------------    Telefonu gramatas lietotne   ------------------------------ #


# Funkcija - paradit tabulu
def display(type='all'):
    tree.delete(*tree.get_children())
    conn = sqlite3.connect("kontaktuSaraksts.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS ContactList (id INTEGER PRIMARY KEY, name VARCHAR, info VARCHAR, family VARCHAR, bros VARCHAR, hoes, VARCHAR)")
    if type == 'all':
        cursor.execute("SELECT * FROM ContactList ORDER BY family DESC") #FAMILY COMES FIRST
    elif type == 'family':
        cursor.execute("SELECT * FROM ContactList WHERE family = 'Yes'")
    elif type == 'hoes':
        cursor.execute("SELECT * FROM ContactList WHERE hoes = 'Yes'")
    elif type == 'bros':        
        cursor.execute("SELECT * FROM ContactList WHERE bros = 'Yes'")
    # Patiesi parada datubazi ari aplikacijaa
    contacts1 = cursor.fetchall()
    for contact in contacts1:
        tree.insert('', 'end',values=(contact[1], contact[2], contact[3], contact[4], contact[5]))
    conn.close()


# Funkicja - ievadit personas kontaktinfo, ka ari vai tas ir gimenes loceklis
def new_contact():
    global contact_window
    contact_window = Tk()
    contact_window.geometry("400x400")
    contact_window.config(background="Black")
    contact_window.title("New Contact")
    global contact_status    
    contact_status = []

    def on_select(event):
        if var.get() not in contact_status:
            contact_status.append(var.get())
        print(var.get())

    def ok(name, info):
        if "Family" in contact_status:
            fam = "Yes"
        else:
            fam = "-"
        if "Bro" in contact_status:
            bro = "Yes"
        else:
            bro = "-"
        if "Hoe" in contact_status:
            hoe = "Yes"
        else:
            hoe = "-"

        
        if len(name) < 1 or len(info) < 1:
            messagebox.showerror("Error", "One or both input fields are empty.")
        elif len(info) < 1:
            messagebox.showerror("Error", "Save a valid contact spot.")
        else:
            conn = sqlite3.connect("kontaktuSaraksts.db")
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ContactList (id INTEGER PRIMARY KEY, name VARCHAR, info VARCHAR, family VARCHAR, hoes, VARCHAR)")
            cursor.execute("INSERT INTO ContactList (name, info, family, bros, hoes) VALUES (?, ?, ?, ?, ?)", (name, info, fam, bro, hoe))
            conn.commit()
            conn.close()
            display()
            contact_window.destroy()

    l11 = Label(contact_window,
                text="Name & Surname: ",
                fg="#FDB915",
                bg="Black",
                font=("Visby",15)
                )
    l12 = Label(contact_window,
                text="Contact info: ",
                fg="#FDB915",
                bg="Black",
                font=("Visby",15)
                )
    l13 = Label(contact_window,
                text="Type: ",
                fg="#FDB915",
                bg="Black",
                font=("Visby",15)
                )
    
    b11 = Button(contact_window,
           text="New contact",
           fg="#FDB915",
           bg="Grey",
           font=("Visby",15),
           border=3,
           command=lambda: ok(e1.get(), e2.get())
           )

    
    e1 = Entry(contact_window,
                fg="#FDB915",
                bg="Grey",
                font=("Visby",15),
                border=3)
    e2 = Entry(contact_window,
                fg="#FDB915",
                bg="Grey",
                font=("Visby",15),
                border=3
                )
    

    var = StringVar()
    var.set("Family")

    option = OptionMenu(contact_window, var, "Family", "Hoe", "Bro", command=on_select,)
    

    l11.place(x=30, y=30)
    l12.place(x=30, y=130)
    l13.place(x=30, y=230)
    e1.place(x=30, y=80)
    e2.place(x=30, y=180)
    b11.place(x=200, y=350)
    option.place(x=130, y=230)

    contact_window.mainloop()



#  Visu ivadioto info (DB) ir iespejams redzet Vizualaja dala
window = Tk()
window.geometry("600x600")
window.config(background="Black")
window.title("Contact book")


l1 = Label(window,
           text="Your contacts",
           fg="#FDB915",
           bg="Black",
           font=("Visby",40))
b1 = Button(window,
           text="New contact",
           fg="#FDB915",
           bg="Grey",
           font=("Visby",15),
           border=3,
           command=lambda: new_contact())
b2 = Button(window,
            text="Family",
            fg="#FDB915",
            bg="Grey",
            font=("Visby",15),
            border=3,
            command=lambda: display('family'))
b3= Button(window,
            text="Bros",
            fg="#FDB915",
            bg="Grey",
            font=("Visby",15),
            border=3,
            command=lambda: display('bros'))

b4 = Button(window,
            text="Hoes",
            fg="#FDB915",
            bg="Grey",
            font=("Visby",15),
            border=3,
            command=lambda: display('hoes'))
b5 =  Button(window,
            text="All",
            fg="#FDB915",
            bg="Grey",
            font=("Visby",15),
            border=3,
            command=lambda: display())

l1.place(x=120, y=30)
b1.place(x=200, y=150)
b2.place(x=300, y=360)
b3.place(x=380, y=360)
b4.place(x=445, y=360)
b5.place(x=510, y=360)

tree = ttk.Treeview(window,column = ("c1", "c2", "c3", "c4", "c5"), show='headings', height=8)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="Name:")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="contact info:")
tree.column("# 3", anchor=CENTER, width=40)
tree.heading("# 3", text="Family")
tree.column("# 4", anchor=CENTER,width=70)
tree.heading("# 4",text="Bro")
tree.column("# 5", anchor=CENTER, width=40)
tree.heading("# 5", text="Hoe")


tree.pack(side=BOTTOM)

display()

window.mainloop()