f = open("alise.txt") # atver failu
gar = len(f.read())
f.seek(0)
parent = f.read(1)
mezgls = ""
mezgli = []
c = ""
for i in range(gar):
    c = f.read(1)
    if c == " ":
        if mezgls != "":
            mezgli.insert(0, mezgls)
        mezgls = ""
    elif c == "\n":
        mezgli.insert(0, mezgls)
        mezgls = ""
        print(parent, mezgli)
        parent = f.read(1)
        mezgli = []
    else:
        mezgls += c
        
    