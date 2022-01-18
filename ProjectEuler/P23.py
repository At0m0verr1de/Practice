import math

abundant = []
sums = []

for i in range(1, 28124):
    sum = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            sum += j
            if i/j != j:
                sum += i / j

    if sum+1 > i:
        abundant.append(i)

for i in abundant:
    for j in abundant:
        if i+j <= 28123:
            sums.append(i+j)

sums = set(sums)

sumAbundant = 0

for i in sums:
    sumAbundant += i

print(28123*28124/2 - sumAbundant)

