# 1P. Programma, kas izvada visus skaitļus no -1 līdz -10 dilstošā secībā

# for i in range(-1, -11, -1):
#     print(i)

# 2P. Lietotājs ievada divus skaitļus, programma izvada, kuram no šiem skaitļiem ir lielāka ciparu summa.

# x = int(input("skaitlis 1: "))
# y = int(input("skaitlis 2: "))

# 3P. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. No ir ievadītajiem skaitļiem atrast lielāko pāra skaitli.

# n = int(input('n:'))
# max = n
# while n != 0:
#     if n > max:
#         max = n
#     n = int(input('n:'))

# print(max)

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

def ir_pirmskaitlis(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
        return True
    n = int(input('n:'))
    if ir_pirmskaitlis(n):

        sum = sum(int(c) for c in str(n))
        print('summa:', sum)
else:

        skaitlis_str =str(n)
max_sk = max(skaitlis_str)
print('Lielákais cipars:' , max_sk)

