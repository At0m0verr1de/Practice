import math
factors = []

for i in range(1, int(math.sqrt(600851475143))):
    if 600851475143 % i == 0:
        factors.append(i)

for j in factors:
    prime = True
    for i in range(2, int(math.sqrt(j))):
        if j % i == 0:
            prime = False
            break
    if prime:
        print(j)

