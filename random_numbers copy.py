import random

# a = []

# for i in range(10):
#     x = random.randint(1, 10)
#     while a.count(x) != 0:
#         x = random.randint(1, 10)
#     a.append(x)

# sum = 0
# for e in a:
#     sum += e
#     print(e, end=" ")
# print()
# print(sum)

x = random.randint(1, 100)
y = int(input('uzmini skaitli: '))
reizes = 1

while x != y:
    if x > y:
        print('lielaks')
    else:
        print('mazaks')
    y = int(input('uzmini skaitli: '))
    reizes += 1

print('uzmineji ar', reizes, 'reizem')



