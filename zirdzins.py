def coord(a):
    y = a % 10
    x = (a - y) // 10
    return [x, y]

def display(m):
    for row in m:
        for elem in row:
            print(elem, end=" ")
        print()

def knight(x1, y1, x2, y2):
    if abs(x1 - x2) == 2 and abs(y1 - y2) == 1:
        return True
    elif abs(x1 - x2) == 1 and abs(y1 - y2) == 2:
        return True
    else: 
        return False

def isPossible(c1, c2, m):
    x1 = coord(c1)[0] - 1
    y1 = coord(c1)[1] - 1
    x2 = coord(c2)[0] - 1
    y2 = coord(c2)[1] - 1
    if knight(x1, y1, x2, y2) and m[x1][y2] == 0:
        return True
    else:
        return False

def success(m):
    ok = True
    for row in m:
        for elem in row:
            if elem == 0:
                ok = False
    return ok
            

m = [[0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0], 
     [0, 0, 0, 0, 0, 0, 0, 0]]

c1 = int(input("ievadi sākumpunktu: "))
m[coord(c1)[0] - 1][coord(c1)[1] - 1] = 1

c2 = int(input("ievadi nākamo: "))

while isPossible(c1, c2, m):
    m[coord(c2)[1] - 1][coord(c2)[0] - 1] = 1
    display(m)
    c1 = c2
    c2 = int(input("ievadi nākamo: "))
display(m)

if success(m):
    print("uzvareji!")
else:
    print("zaudeji :(")

