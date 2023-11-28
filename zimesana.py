from tkinter import *

root = Tk()
C = Canvas(root, bg="white", height=600, width=600)

# bezgaliba
# C.create_arc(20, 20, 200, 200, start=0, extent=270, style=ARC)
# C.create_arc(200, 200, 380, 380, start=180, extent=270, style=ARC)
# C.create_line(200, 110, 200, 290)
# C.create_line(110, 200, 290, 200)

# P
# C.create_line(10, 10, 10, 200)
# C.create_line(10, 200, 40, 200)
# C.create_line(10, 10, 40, 10)
# C.create_arc(-10, 10, 90, 110, start=-90, extent=180, style=ARC)
# C.create_line(40, 110, 40, 200)


# sveice
# C.create_rectangle(100, 180, 300, 220, fill="white", outline="white")
# C.create_rectangle(180, 100, 220, 300,  fill="white", outline="white")

# griekija
# for i in range(0, 401, 100):
#     C.create_rectangle(0, i, 800, i + 50, fill="blue", outline="")

# C.create_rectangle(0, 0, 250, 250, fill="blue", outline="")
# C.create_rectangle(0, 100, 250, 150, fill="white", outline="")
# C.create_rectangle(100, 0, 150, 250, fill="white", outline="")

# seishelu salas
# C.create_polygon(0, 450, 0, 0, 300, 0, fill="blue")
# C.create_polygon(0, 450, 300, 0, 600, 0, fill="yellow")
# C.create_polygon(0, 450, 800, 150, 800, 300, fill="white")
# C.create_polygon(0, 450, 800, 450, 800, 300, fill="green")

# # meness
# C.create_arc(20, 20, 200, 200, start=80, extent=200, style=ARC)
# C.create_arc(60, 20, 240, 200, start=105, extent=150, style=ARC)

# C.create_polygon(300, 10, 400, 200, 590, 300, 400, 400, 300, 590, 200, 400, 10, 300, 200, 200, fill="white")

# C.create_rectangle(0,0, 300, 600, fill="white")
# for i in range(0, 601, 50):
#     C.create_polygon(300, i, 400, i+25, 300, i+50, fill="white")

# for i in range(0, 601, 30):
#     C.create_polygon(300, i, 350 + i/5, i+50, 250 - i/5, i+50, fill="white")

# C.create_rectangle(0, 100, 600, 500, fill="blue")
# C.create_oval(150, 150, 450, 450, fill="white")

# C.create_polygon(300, 100, 350, 200, 500, 200, 400, 300, 500, 500, 300, 400, 100, 500, 200, 300, 100, 200, 250, 200, fill="white")


# C.create_rectangle(0, 0, 300, 600, fill="white")
# for i in range(0, 601, 100):
#     C.create_polygon(300, i, 350, i+50, 300, i + 100, fill="white")


# range(sakuma punkts, beigu punkts neieskaitot, solis)
# for i in range(0, 601, 20): 
#     C.create_line(i, 0, i, 600)

# colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# index = 0
# for i in range(0, 600, 100):
#     C.create_rectangle(i, 0, i + 100, 600, fill=colors[index])
#     index = index + 1

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
index = 0
start = 0
end = 600
for i in range(6):
    C.create_rectangle(start, start, end, end, fill=colors[i], outline="")
    start += 50
    end -= 50


C.pack()
mainloop()
