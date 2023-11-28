with open("dalitaji.txt", "w") as f:
    for i in range (1, 101):
        f.write(str(i) + " | ")
        for x in range(1, i + 1):
            if i % x == 0:
                f.write(str(x) + " ")
        f.write("\n")
