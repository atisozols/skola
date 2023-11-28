# d = {'atslega': 'vertiba'} # key:value

# d.update({'key':'value'})

# print(d)

# d['key'] = 'value2'
# d[4] = 5


# biezhumi = {}
# m = [1, 2, 2, 4, 1, 2, 5, 3, 5, 4, 2, 1, 2]

# for elem in m:
#   biezhumi[elem] = m.count(elem) # biezhumi.update({elem: m.count(elem)})
  
# print(biezhumi) # {1: 3, 2: 5, 4: 2, 5: 2, 3: 1}

# for key in biezhumi:
#   print(key, biezhumi[key])
  
  
# footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

# sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda item:item[1])
# converted_dict = dict(sorted_footballers_by_goals)

# print(sorted_footballers_by_goals)

# print(converted_dict)

# Izvadīt visus skaitļus no 1 līdz 100 ar vārdiem

desmiti = {0:'',
           2:'divdesmit',
           3:'trīsdesmit',
           4:'četrdesmit',
           5:'piecdesmit',
           6:'sešdesmit',
           7:'septiņdesmit',
           8:'astoņdesmit',
           9:'deviņdesmit'
           }

vieni = {0:'',
         1:'viens',
         2:'divi',
         3:'trīs',
         4:'četri',
         5:'pieci',
         6:'seši',
         7:'septiņi',
         8:'astoņi',
         9:'deviņi'
        }

padsmiti = {0:'desmit',
            1:'vienpadsmit',
            2:'divpadsmit',
            3:'trīspadsmit',
            4:'četrpadsmit',
            5:'piecpadsmit',
            6:'sešpadsmit',
            7:'septiņpadsmit',
            8:'astoņpadsmit',
            9:'deviņpadsmit'
            }

# for i in range(1, 100):
#   cipars2 = i % 10
#   cipars1 = (i - cipars2) // 10
  
#   if cipars1 == 1:
#     print(padsmiti[cipars2])
#   else:
#     print(desmiti[cipars1] + vieni[cipars2])
    
    
# for i in range(1, 100):
#   cipars2 = i % 10
#   cipars1 = (i - cipars2) // 10
  
#   if i < 10:
#     print(vieni[i])
#   elif i == 10:
#     print('desmit')
#   elif i < 20:
#     print(vieni[cipars2] + 'padsmit') if cipars2 == 3 else print(vieni[cipars2][:-1] + 'padsmit')
#   else:
#     print(vieni[cipars1][:-1] + "desmit " + vieni[cipars2]) if cipars1 != 3 else print(vieni[cipars1] + "desmit " + vieni[cipars2])



a = {
     'b':'e',
     'f':'r',
     't':'l',
     'u':'c'
     }

b = {
     'e':'s',
     'r':'w',
     'c':'g',
     'l':'a'
     }

c = {}

for key in a:
  print(key, a[key], b[a[key]])
  c[key] = b[a[key]]
  
# print(c)