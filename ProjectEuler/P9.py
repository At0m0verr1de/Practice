import time

s = time.time()

for i in range(1, 500): # for optimisation
    for j in range(1, 1000-i):
        k = 1000-i-j
        if i**2 == j**2 + k**2:
            print(i*j*k)
            break

e = time.time()

print(e-s)