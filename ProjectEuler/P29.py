sums = []

for i in range(2, 101):
    for j in range(2, 101):
        sums.append(i**j)

print(len(list(set(sums))))

