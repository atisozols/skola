# arr = [1, 6, 4, 8, 5, 12, 2, 9, 1, 10, 4, 3] # Array/List

# print(arr[2])

# print('garums/elementu skaits: ', len(arr))

# arr.append(7) # pievieno elementu saraksta galā

# arr.pop() # noņem pēdējo elementu | arr.pop(3) nonems elementu trešajā pozīcijā

# resurss: https://www.programiz.com/python-programming/list

# Uzdevums: Izvadīt no arr masīva visus 1)pāra skaitļus; 2) nepāra; 3) lielāko elementu; 4) visu elementu summu

# arr1=[]
# arr2=[]
# sum=0

# for i in arr:
#     if i %2==0:
#         arr.append(i)
#     elif i!=0:
#         arr2.append(i)
#     sum+=1

# arr.sort()

# print(arr1)
# print(arr2)
# print(arr[len(arr)-1])
# print(sum)
    
# sv="rinkevics"
# for char in sv:
#     print(char)

# s=[1,6,3,8,3,2,5]

# skaits=s.count(3)
# for i in range(skaits):
#     s.remove(3)

# s.extend([1,7,3])
# s+=[1,7,3]

# print(s)


#46. doti divi sarkasti, iegut sarakstu skelumu
# t=[7,4,8,2,9,0]
# s=[1,6,3,8,3,2,5]
# skelums=[]

# for t_element in t:
#     for s_element in s:
#         if t_element==s_element:
#             skelums.append(t_element)

# print(list(set(skelums)))

#47. doti divi saraksti, iegut starpibu. 
#starpibu jeb visus elementus no t kas nav ieks s. 
# t=[7,4,8,8,2,9,0]
# s=[1,6,3,8,3,2,5]
# skelums=[]

# for elem in skelums:
#     t.remove(elem)

# print(t)

#48. dots saraksts, izvadit no otra gala. 

# s=[1,6,3,8,3,2,5]
# # for i in range(6, -1,-1):
# #     print(i, s[i])

# s.reverse()
# print(s)

#50.noteikt vai saraksts ir palindroms.
# (no abiem galiem lasaams vienadi)

# s=[1,5,6,5,1]
# s_copy=[]
# for i in range(len(s)-1,-1,-1):
#     s_copy.append(s[i])
# print(s, s_copy)


# if s==s_copy:
#     print("palindroms")
# else:
#     ("nav")

#51. dots sarksts nums. lietotajs ievada skaitli, programma ievada to divu skaitlu indeksus, kas summa veido ievadito skaitli.

# nums=[1,5,6,3,8,7,2]
# sum=int(input("ievadi skaitli"))
# result=[]
# for i in range(7):
#     for j in range(7):
#         if j!=i:
#             if nums[i] + nums[j]==sum:
#                 print(nums[i], nums[j])

#52. dotam saraksta noskaidrot medianu.<------------------------
#       0 1 2 3 4 5 6 7 
# nums=[1,5,6,9,8,7,3,2]
# nums.sort()

# if len(nums)%2==0:
#  index=(int(len(nums)/2))
#  print("mediana:",nums[index]+nums[index-1]/2)#<------nepara skaitliem
# else:
#  index=int(len(nums)/2)
#  print("mediana:",nums[index])#<-------para sakitliem

#53. ievad askaitli n, izvadit tos sarksta elementus kas ir mazaki par n. 
# nums=[1,5,6,9,8,7,3,2]
# n=int(input("sakitlis"))
# for elem in nums:
#     if n>elem:
#      print(elem)

# 1. Vada skaitļus līdz ievada 0. Programma no ievadītajiem skaitļiem izveido sarakstu.
# arr=[]
# n=int(input("n:"))
# while n!=0:
#   n=int(input("n:"))
#   arr.append(n)
# print(arr)

# 2. No 1. uzd saraksta izvadīt pēdējos piecus elementus.<--------------------------------!!!!!!!!
# arr=[]
# n=int(input("n:"))
# while n!=0:
#   n=int(input("n:"))
#   arr.append(n)
# arr.reverse()<--------- apgriez sarakstu un izalsa pedejos 5 elementus
# for i in range(5):
#   print(arr[i])

# 3. Izvadīt no saraksta tos elementus, kas mazāki par 12 un dalās ar 3.
# arr=[]
# n=int(input("n:"))
# while n!=0:
#   n=int(input("n:"))
#   if n<12 and n%3==0:
#     arr.append(n)
# print(arr)

# 4. Ievada vai sagatavo divus sarakstus garumā 4, kas satur tikai ciparus (0 - 9).
#    Uzrakstīt programmu, kas sarakstus saskaita rakstos

# a=[1,3,6,2]
# b=[1,8,4,9]
# c=[]
# carry=0
# for i in range(3,-1,-1):
#  sum=a[i]+b[i]
#  p=sum%10
#  c.insert(0,p=carry)
#  carry=sum//10
# if carry:
#    c.insert(0,carry)
# print(c)



# $PARBAUDES DARBS




# 1N. Skaitlis par sarakstu. Piemēram, 673 -> [6, 7, 3]

# n=int(input("n:"))
# s=[]
# s.append(n)
# print(s)

# 2N. Vada skaitļus, kamēr ievada 0. No skaitļiem izveido sarakstu; sarakstā atrod 3 mazākos nepāra skaitļus.
# arr=[]
# n=int(input("n:"))
# while n!=0:
#   n=int(input("n:"))
#   arr.append(n)
# print(arr)






# 3N. Programma, kas izveido sarakstu garumā 10 no unikāliem nejauši izvēlētiem skaitļiem intervālā (1, 12).
import random
a=random.randint(1,12)
arr=[]
for i in range(10):
   arr.append(a)
print(arr)






# 4. Programma, kas atņem rakstos dotos sarakstus a un b, iegūstot sarakstu c.

# a = [1, 5, 2, 3]
# b = [1, 2, 3, 0]
# c=[]
# carry=0
# for i in range:
#  sum=a[i]-b[i]
#  c.insert(0,p=carry)
#  carry=sum
# if carry:
#    c.insert(0,carry)
# print(c)







