simti = {
    0:'',
    1:'simts',
    2:'divsimt',
    3:'trissimt',
    4:'cetrsimt',
    5:'piecsimt',
    6:'sessimt',
    7:'septinsimt',
    8:'astonsimt',
    9:'devinsimt'
}

desmiti = {
    0:'',
    2:'divdesmit',
    3:'trisdesmit',
    4:'cetrdesmit',
    5:'piecdesmit',
    6:'sesdesmit',
    7:'septindesmit',
    8:'astondesmit',
    9:'devindesmit'
}

vieni = {
    0:'',
    1:'viens',
    2:'divi',
    3:'tris',
    4:'cetri',
    5:'pieci',
    6:'sesi',
    7:'septini',
    7:'astoni',
    9:'devini'
}

padsmiti = {
    0:'desmit', # 210 -> divsimt desmit
    1:'vienpadsmit',
    2:'divpadsmit',
    3:'trispadsmit',
    4:'cetrpadsmit',
    5:'piecpadsmit',
    6:'sespadsmit',
    7:'septinpadsmit',
    8:'astonpadsmit',
    9:'devinpadsmit'
}

num = int(input('ievadi skaitli: '))

s = []
while num > 0:
    p = num % 10
    s.insert(0, p)
    num //= 10 # num = num // 10 - dala bez atlikuma veseli
    
while len(s) < 3:
    s.insert(0,0)
    
print(s)
    
    
if s[1] == 1:
    print(simti[s[0]], padsmiti[s[2]])
else:
    print(simti[s[0]], desmiti[s[1]], vieni[s[2]])
