phonebook = {
    'atis':'27804609',
    'deivids':'25450770'
}

for k, v in zip(phonebook.keys(), phonebook.values()):
    print(k, v)
    
for k in phonebook:
    print(k, phonebook[k])