with open("text.txt") as f:
    file = f.read()
    file = file.split()
    words = {}
    lowercase = []
    for word in file:
        lowercase.append(word.lower())
    for word in lowercase:
        if len(word) >= 4 and word not in words:
            words[word] = 1
        elif len(word) >= 4:
            words[word] += 1
print(words)
