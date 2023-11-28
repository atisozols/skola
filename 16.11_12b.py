# w - write
# r - read
# with open('failanosaukums.txt') as f:

# f.write() - rakstīšana
# f.readlines() - faila saturs par masīvu
# f.readline() - nolasīšana pa rindiņai
# f.seek() - nokļūšana uz konkrētu punktu failā
# f.read() - visa faila satura iegūšana
# s.replace() - aizvietot x ar y failā


# Lietotājs ievada skaitli, programma ieraksta
# failā rindiņas tādā skaitā.

# n = int(input('ievadi: '))
# with open('failins.txt', 'w') as f:
#     for i in range(n):
#         f.write(str(i+1) + ". rindina\n")


# Programma izvada faila katru otro rindiņu.

# with open('failanosaukums.txt','r') as f:
#     m = f.readlines()
#     print(m)
#     for i in range(1, len(m), 2):
#         print(m[i])


# Programma trīs reizes izvada pirmo rindiņu.

# with open('failanosaukums.txt') as f:
#     m = f.readlines()
#     for i in range(3):
#         print(m[0])

#     for i in range(3):
#         print(f.readline())
#         f.seek(0)
        

# Programma izvada faila garāko rindiņu.

# with open('failanosaukums.txt') as f:
#     m = f.readlines()
#     garaka = m[0]
#     for i in range(len(m)):
#         if len(m[i]) > len(garaka):
#             garaka = m[i]
#     print(garaka, len(garaka))

# Programma nolasa tekstu no viena faila un
# ieraksta to otrā, a burtus nomainot ar x

# with open('failanosaukums.txt') as f:
#     text = f.read()
#     with open('fails2.txt', 'w') as g:
#         g.write(text.replace('a', 'x'))

# not writable/not readable



# Ievada n, programma failā izveido 
# skujiņu augstumā n.
# Piemēram, n = 4
# *
# **
# ***
# ****
x = int(input())
y = int(input())
for i in range(8):
    for j in range(8):
        if j + i == x + y - 2:
            print(1, end=" ") 
        elif i - j == x - y:
            print(1, end=" ")
        else:
            print(0, end=" ") 
    print()

# n = int(input('n: '))
# with open('g.txt', 'w') as f:
#     for i in range(n):
#         for j in range(n):
#             if j % 2 == 0:
#                 f.write("0 ")
#             elif i + j == n - 1:
#                 f.write("0 ")
#             else:
#                 f.write("* ")
#         f.write("\n")



# with open('eglite.txt', 'w') as f:
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if j % 2 == 0:
#                 f.write("x")
#             else:
#                 f.write('0')
#         f.write("\n")

# with open('eglite.txt', 'w') as f:
#     for i in range(1, 10):
#         for j in range(1, 10):
#             if i == j:
#                 f.write("0")
#             else:
#                 f.write("x")
#         f.write("\n")

# 1. Izmantojot Python, izveidot jaunu failu,
#  kurā ierakstīt “faili ar python”.
# 2. Izveidot programmu, kura failā ieraksta 
# 10 rindiņas, numurējot tās.

# with open('failins.txt', 'w') as f:
#     f.write('faili ar python\n')
#     for i in range(10):
#         f.write(str(i+1) + '. rindina\n')

# 3. Izdrukāt šī paša faila garāko rindiņu,
#  pie reizes pasakot, cik simbolus gara tā ir.


# with open('failins.txt') as f:
#     a = f.readlines()
#     gar = a[0]
#     for i in range(len(a)):
#         if len(a[i]) > len(gar):
#             gar = a[i]
            
#     print(gar)


# 4. Izvadīt iepriekšējā uzdevuma faila saturu
#  uz ekrāna, samainot vietām 3. un 7. rindiņu.

# with open('failstris.txt') as f:
#     saturs = f.readlines()
#     temp = saturs[2]
#     saturs[2] = saturs[6]
#     saturs[6] = temp
#     for i in range(len(saturs)):
#         print(saturs[i], end="")
#     for line in saturs:
#         print(line, end="")
    


