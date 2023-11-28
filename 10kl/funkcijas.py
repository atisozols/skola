def print_list(m):
    for i in range(len(m)):
        print(m[i], end=" ")
    print()
        
def average(m):
    sum = 0
    for i in range(len(m)):
        sum += m[i]
    avg = sum / len(m)
    return avg

a = [1, 3, 6, 2]
b = [1, 3, 6, 8, 9, 0, 3]

print_list(a)
print_list(b)

# print(average(a))
# print(average(b))
# print(average(a) + average(b))

