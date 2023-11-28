# 1.Ievada divus skaitļus, programma izvada skaitļu summu.

x = int(input("Ievadi 1 Skailti:"))
y = int(input("Ievadi 2 Skaitli:"))

a = x + y

print(a)


# 2.Ievada divus skaitļus, ja skaitļi nav vienādi, izvada lielāko, citādi izvada "vienādi".

b = int(input("Ievadi skailti:"))
a = int(input("Ievadi skailti:"))

if a == b:
    print("vienādi")
elif a > b:
    print(a)
else:
    print(b)


# 3.Tiek ievadīts mēneša numurs(1-12). Programma izvada šī mēneša gadalaiku.

g = int(input("Ievadi skaitli 1 - 12:"))

if g > 0 and g < 13:
    if g >= 3 and g <= 5:
        print("Pavasaris")
    elif g >= 6 and g <= 8:
        print("Vasara")
    elif g >= 9 and g <= 11:
        print("Rudens")
    else:
        print("Ziema")
else:
    print("Ievadīts nepareizs skaitlis")


# 4.Tiek ievadīts divciparu skaitlis, programma izvada ciparu summu šim skaitlim, piemēram, skaitļa 23 ciparu summa būtu 5.

s = int(input("Ievadi divciparu skaitli:"))

if s > 9 and s < 100:
    vieni = s % 10
    desmiti = (s % 100 - vieni ) / 10
    sum = vieni + desmiti
    print(sum)
else:
    print("Netika ievadīts divciparu skaitlis")
