t = (1, 2, 3, 2, 4, 3, 5)
unique = []
for item in t:
    if t.count(item) == 1:
        unique.append(item)
print(unique)
