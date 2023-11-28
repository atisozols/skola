lloyd = {
  "name": "Lloyd",
  "homework": [90.0,97.0,75.0,92.0],
  "quizzes": [88.0,40.0,94.0],
  "tests": [75.0,90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

m = [lloyd, alice, tyler]
keys = ["homework", "quizzes", "tests"]
dic1 = {}

for personazs in m:
    dic1[personazs["name"]] = {}
    for key in keys:
        dic1[personazs["name"]][key] = personazs[key] # dic1['Lloyd']['quizzes'] = lloyd['quizzes']

# for students in m:
#     results = {}
#     for result in keys:
#         results[result] = students[result]
#     dic1[students["name"]] = results
        
        
print(dic1)

dic = {
    'Lloyd':{
        "homework": [90.0,97.0,75.0,92.0],
        "quizzes": [88.0,40.0,94.0],
        "tests": [75.0,90.0]
    },
    'Alice':{
        "homework": [100.0, 92.0, 98.0, 100.0],
        "quizzes": [82.0, 83.0, 91.0],
        "tests": [89.0, 97.0]
    },
    'Tyler':{
        "homework": [0.0, 87.0, 75.0, 22.0],
        "quizzes": [0.0, 75.0, 78.0],
        "tests": [100.0, 100.0]
    }
}

weights = [0.2, 0.3, 0.5]

for student_key in dic: # student_key = ['Lloyd', 'Alice', 'Tyler']
    atzime = 0
    for result_key, weight in zip(dic[student_key], weights): # result_key = ['homework', ..]
        atzime += sum(dic[student_key][result_key])/len(dic[student_key][result_key]) * weight
        
    print(student_key, round(atzime, 0))