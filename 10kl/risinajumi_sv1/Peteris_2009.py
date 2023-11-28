# a = int(input("ievadi a: "))
# print(a+5)
# print(a-1)
# print(a)
# print(a*3)
# print(a/2)
# print(a//2) # DALA BEZ ATLIKUMA
# print(a % 2)
# print(a**2) #kapinasana
# print(a**0.5) #kvadratsakne

# 15 tiek ievadits skaitlis, programma nosaka vai tas ir pozitivs
# a = int(input("ievadi a: "))

# if a > 0:
#     print("a ir pozitivs")
# else:
#     if a == 0:
#         print("a nav ne poz, ne neg")
#     else:
#         print("a ir negativs")


# if a > 0:
#     print("a ir pozitivs")
# elif: a == 0:
#         print("a nav ne poz, ne neg")
#     else:
#         print("a ir negativs")

# 16. ievada 3 vertibas, progr. nosaka trijst. eksistenci, vertibas ir trijstura malas
# a = int(input("ievadi a:"))
# b = int(input("ievadi b:"))
# c = int(input("ievadi c:"))

# if a+b>c:
#     if a+c>b:
#         if b+c>a:
#             print("eksistē")
# else: 
#     print("neeksistē")



# if a+b>c:
#     if a+c>b:
#         if b+c>a:
#             print("eksistē")
#         else: 
#             print("neeksistē")        
#     else: 
#         print("neeksistē")    
# else: 
#     print("neeksistē")

# if a+b>c and a+c>b and b+c>a:
#     print("eksistē")
# else:
#     print("neeksistē")

# 17. ievadi dienas nr. (1-7). progrmm. pasaka:
# 1) darbadienas vai brivdiena
# 2)pasaka dienas  nosaukumu

#1)
# a= int(input("diena:"))

# if a<8:
#     print("brivdiena")
# elif a>5:
#     print("darbadiena")
# if a>8:
#     print("neeksistē")

#18. noteikt, vai ievaditais skaitlis ir para vai nepara 

# a= int(input("ievadīt a "))

# if a%2 == 0:
#     print("para")
# else: 
#     print ("nepara")

#19.ievaditi divi skaitli, izvadit ielako

# a=int(input("skaitlis a"))
# b=int(input("skaitlis b"))

# if a>b:
#     print("a")
# elif a==b:
#     print("vienadi")
# else:
#     print("b")

#20.ievaditi tris skaitli, izvadit lielako

# x=int(input("skaitlis x"))
# y=int(input("skaitlis Y"))
# z=int(input("skaitlis z"))

# if x>y and x>= z:
#     print(x)

#21.

# x=int(input("skaitlis x"))
# y=int(input("skaitlis Y"))
# z=int(input("skaitlis z"))

# d= (y**2) - (4*x*z)
# if d<0:
#     print("nav saknes")

# elif d==0:
#     print(-y/(2*x))

# else:
#     print((-y+d**0.5)/(2*x))
#     print((-y-d**0.5)/(2*x))

# if x>0:
#     print("zari uz augšu")
# else:
#     print("zari uz leju")

# x0 = -y/(2*x)
# y0 = x*x0**2+y*x0+z

# print(x0,y0)

#22.ievada skaitli. noteikt mazako iespejamo nominalo skaitli un vērtibu, lai iegutu skaitli.

# n=int(input("summa"))

# b500= n//500
# print(b500)
# if b500>0:
#     print(500, b500)
#     n=n-b500*500

# print(n)

# b200= n//200
# print(b200)
# if b200>0:
#     print(200, b200)
#     n=n-b200*200

# print(n)

# b100= n//100
# print(b100)
# if b100>0:
#     print(100, b100)
#     n=n-b100*100

# print(n)

# b50= n//50
# print(b50)
# if b50>0:
#     print(50, b50)
#     n=n-b50*50

# print(n)

# b20= n//20
# print(b20)
# if b20>0:
#     print(20, b20)
#     n=n-b20*20

# print(n)

# b10= n//10
# print(b10)
# if b10>0:
#     print(10, b10)
#     n=n-b10*10

# print(n)

# b5= n//5
# print(b5)
# if b5>0:
#     print(5, b5)
#     n=n-b5*5

# print(n)

#Cikls ar skaititaju- for

# for i in range(10):
#     print(i, "sveiki")
    
# for i in range(10,-1,-1): #(sakuma, beigu, solis)
#     print(i)

#23. tiek ievadits n. programma izvada visus skaitlus no 1 lidz n ieskaitot

# n =int(input("n:"))

# for i in range(1,1+n): 
#     print(i)

#24. tiek ievadits n. programma izvada visus skaitlus no 1 lidz n kvadrati.

#4-. 1 4 9 16

# n =int(input("n:"))

# for i in range(1,n+1): 
#     print(i**2)
     
#25. tiek ievadits n. iegut u izvadit visu skaitlu no 1 lidz nsummu.

# n =int(input("n:"))
# summa=0
# for i in range(1,n+1): 
#     summa += i#summa = summa+i
#     print(i,summa)

#26.tiek ievadits n. izvada visus n dalitajus

# n =int(input("n:"))
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

#27. ievada a un b. izvada visus skaitlus no b lidz a dilstosa seciba. 

#  a = int(input("a:"))
#  b = int(input("b:"))

#  for i in range(b, a-1, -1):
#      print(i)

#  while a < b:
#      print(b)
#      b-=1

#28. programma liek izvadit 7 skaitlus, izvada skaitlu summu.
# summa=0
# for i in range(7):
#     x=int(input("x:"))
#     summa= summa + x   #summa+=x

# print(summa)

# 29. ievadam 5 skaitlus, izvada lielako skaitli
# max=0
# for i in range(5):
#     x=int(input("x:"))
#     if x>max:
#         max=x
# print(max)

#30. 29 uzd tikai ar min. vertibu

# min=2147483647
# for i in range(5):
#     x=int(input("x:"))
#     if x<min:
#         min=x
# print(min)

#31. ievadam n. izvada n faktorialu 
# (n!)<------- faktorials n! ,piemram, 5!= 5*4*3*2*1

# n =int(input("n:"))
# fak=1
# for i in range(1,n+1): 
#     fak=fak*i
#     print(fak
#32. ievda n , notiekt vai n ir pirmskaitlis. #25, 26

# n =int(input("n:"))

# for i in range(1,n+1):
#     if n%i==0 and i !=1 and i!=n:

# skaits=0
# n =int(input("n:"))
# for i in range(1,n+1):
#     if n%i==0:
#         skaits=skaits+1
        
# if skaits==2:
#     print(n, "ir pirmskiatlis")
# else:
#     print(n, "nav pirmskaitlis")


#01. ievada n, izvada para skaitli
# a= int(input("ievadīt a "))
# for i in range(1,a+1):
#     if i%2 ==0:
#         print(i)


#02. ievada n , izvada nepara skaitli

# a= int(input("ievadīt a"))
# for i in range(1,a+1):
#     if i%2 !=0:
#        print(i)


# sum=0
# n =int(input("input number:"))
# while n!=0:
#     n =int(input("input number:"))
#     sum+=n
# print(sum)

#03. 
# n =int(input("input number:"))
# while n!=0:
#     n =int(input("input number:"))
#     sum-=1
# print(sum)


#33.programma kas neprasa neko ievadit un ievada naturalus skaitlus no 1-32
# for i in range(1,33):
#      if i%2 ==0:
#         print(i)

# #34.
# n =int(input("input number:"))
# for i in range(1, n+1):
#         if i%4 !=0:
#              print(i)
        
# #35.
# summa=0
# for i in range(1,10):
#      x=int(input("x:"))
#      summa+= x
#      print(summa)
     

#36.while cikls

# n=1
# while n<11:
#     print(n)
# n+=1

#ievadits skaitlis lidz tiek ievdita 0. ievaditos skaitlus saskaita un izvada summu.

# sum=0
# n =int(input("n :"))
# while n!=0:
#      sum+=n
# n =int(input("n :"))
# print(sum)

#37. ievada skaitli programma izvada skaitla ciparu summu. 

# n =int(input("n :"))
# sum=0
# while n>0:
#     p=n%10
#     sum+=p
#     n=n//10
#     print(sum)
    
#38. tiek vaditi skaitli lidz ievada 0. programma nemitigi izsaka vai skitlis ir lielaks par ieprieksejo

# x =int(input("sk :"))
# sum=0
# while x!=0:
#     y=int(input("sk :"))
#     print(x,y)
#     if x>y:
#        print("mazaks")
#     elif x==y:
#         print("vienads")
#     else:
#         print("lielaks")
#     x=y

#1*. eglite augstuma n.
# n =int(input("n:"))
# for i in range(1,n+1):
#    print(i)
# for j in range(1,i+1):
#     print("*", end="")
   
#39. vada skaitlus lidz tiek ievadita 0. programma izvada lielako no ievaditajiem.

# n= int(input("n:"))
# max=n
# while n !=0:
#     if n>max:
#         max=n
#     n= int(input("n:"))

# print(max)

#40. ievaditam skaitlim atrast lielako ciparu pec vertibas

# max=0
# n =int(input("n :"))
# while n>0:
#     pedejais_cipars=n%10
#     if pedejais_cipars>max:
#       max=pedejais_cipars
#     print(pedejais_cipars)
#     n=n//10
#print(max)

#41. vada skaitlus lidz tiek ievadita 0. programma izvada videjo vertibu.
# skaits=0
# sum = 0
# n =int(input("n :"))
# while n!=0:
#      sum+=n
#      skaits+=1
# n =int(input("n :"))

# print(sum/skaits)

#42. fibonaci virkne

# n =int(input("n :"))
# x1=1
# x2=1
# for i in range(n):
#     print(x1,x2,end="=")
#     next=x1+x2
#     x1=x2
#     x2=next
# print(next)

# import random
# # 1- akmens, 2-skeres, 3-papirs
# play=0
# while play==0:
#  streak=0

#  while True:
#     mansgajiens=n =int(input("n 1- akmens, 2-skeres, 3-papirs:"))
#     compgajiens=random.randint(1,3)

#     if mansgajiens - compgajiens==1:
#         break
#     elif compgajiens-mansgajiens==1:
#         streak+=1
#         print("bang")
#     elif mansgajiens==1 and compgajiens==3:
#         break
#     elif mansgajiens==3 and compgajiens==1:
#         streak+=1
#         print("bang")
#     elif mansgajiens==compgajiens:
#         print("neizskirts")
    
#  print("tu zaudeji, tavs streak:", streak)
#  play=int(input("ja velies spelet velreiz, ievadi 0:"))

# import random 

#43 programma, kas uzgenereee skaitli un lauj lietotajiem minēt, kamēr tas uzmin

# s=random.randint(1,10)
# n =int(input("n :"))

# while n!=s:
#     n =int(input("n :"))
    
# print("uzmineji",s)


#43.1 pievienot funkcionalitati kas uzskaita ar cik minejjumiem uzmineja

# import random
# minejumi=1
# s=random.randint(1,10)
# n =int(input("n :"))

# while n!=s:
#     n =int(input("n :"))
#     minejumi+=1
# print("uzmineji ar",minejumi,"meginajumiem")

#43.pec katra nepareiza minejuma programma iedod hint, kuraa virziena ir atbilde

# import random
# while True:
#     minejumi=1
#     s=random.randint(1,2)
#     n =int(input("n :"))

#     while n!=s:
#         if n>s:
#             print("mazak")
#         else:
#             print("vairak")
#         n =int(input("n :"))
#         minejumi+=1
#     print("uzmineji ar",minejumi,"meginajumiem")

#44. ievaditam skiatlim noteikt vai tam piemit vairak para skiatla dalitaji vai nepara
# n =int(input("n :"))
# neparadalsk=0
# paradalsk=0

# for i in range(1, n+1):
#     if n%i==0:
#         if i%2==0:
#             paradalsk+=1
#         else:
#             neparadalsk+=1

# if paradalsk>neparadalsk:
#         print("para dalitaji")
# elif paradalsk<neparadalsk:
#      print("nepara dalitaji ir vairak")
# else:
#      print("vienadi")

#45. izvadit visus skaitlus no 1 lidz 1000, kuriem nepara skaitla dalitaji ir vienadi ar para

# for n in range(1,1001):
#     neparadalsk=0
#     paradalsk=0

#     for i in range(1, n+1):
#         if n%i==0:
#             if i%2==0:
#                 paradalsk+=1
#             else:
#                 neparadalsk+=1
#     if paradalsk==neparadalsk:
#             print(n)





#PARBAUDES DARBS

# 1N. Programma, kas izvada visus pāra skaitļus no 20 līdz 37. 
# for i in range(20,37):
#      if i%2 ==0:
#         print(i)

# 2N. Lietotājs ievada divus skaitļus, programma izvada, kuram no skaitļiem ir mazāka ciparu summas vidējā vērtība


# sum = 0
# a =int(input("a :"))
# b =int(input("b :"))
# while a!=0:
#     sum+=0
# a =int(input("a :"))
# b =int(input("b :"))
# print(sum)


# 3N. Programma, kas pieprasa vadīt skaitļus, kamēr neievada 0. Tiek saskaitīti visi ievadītie nepāra skaitļi.

# sum=0
# n=1
# while n!=0:
#     n =int(input("n :"))
#     if n%2 !=0:
#         sum+=n
# print(sum)


# 4. Lietotājs ievada skaitli, programma nosaka šī skaitļa pirmo trīs ciparu vidējo vērtību.
# Piemērs: 1326569 -> 132 -> 2.0

# sum=0
# skaits=0
# a =int(input("a :"))
# if a%skaits==0:

#print(a)

# 5. Lietotājs ievada skaitli. Ja skaitlis ir pirmskaitlis, izvadīt tā ciparu summu, citādi izvadīt lielāko ciparu

sum=0
a =int(input("a :"))
while a==0:
    if a%a and a%1==0:
        sum+=0
    elif a<a:
            print()
print(sum)



















