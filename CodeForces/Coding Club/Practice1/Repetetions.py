dna = input()
j = 0
highest = 0
 
 
while j < len(dna):
    temp = 0
    for k in range(j, len(dna)):
        if dna[j] == dna[k]:
            temp += 1
        else:
            break
    j += temp
    if highest < temp:
        highest = temp
 
print(highest)
