# 1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37. 

for skaitlis in range (20, 37):
  if skaitlis % 2 == 0:
      print(skaitlis)
    
# 2N. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība

int(input("ievadi pirmo skaitli: "))
int(input("ievadi otro skaitli: "))

def videja_ciparu_summa(skaitlis):
    summa = 0
    summa = 0
    while skaitlis > 0:
        cipars = skaitlis % 10
        summa += cipars
        skaitlis += 1
        skaitlis = skaitlis // 10
    return summa / skaitlis if skaitlis > 0 else 0 
vid_summa1 = videja_ciparu_summa(skaitlis1)
vid_summa2 = videja_ciparu_summa(skaitlis2)

if vid_summa1 < vid_summa2:
    print("Pirmā skaitļa vidējā ciparu summas vērtība ir mazāka: vid_summa1 ")
elif vid_summa2 < vid_summa1:
    print("Pirmā skaitļa vidējā ciparu summas vērtība ir mazāka: vid_summa2 ")
else: 
    print("Ja abiem skaitļiem ir vienāda ciparu vidējā summas vērtība")


# 3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.

nepāru_skaitli = 0
while True:
    ievade = int(input("ievadiet skaitli(0 lai beigtu)"))
    if ievade == 0:
        break
    if ievade % 2 != 0:
        nepāru_skaitli += ievade

print("nepāru skaitļu summa ir:", nepāru_skaitli)


# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

