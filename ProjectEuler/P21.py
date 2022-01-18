import math
import time

s = time.time()

def checkAmicable(num):
    sum = 0
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            sum += j
            if num/j != j:
                sum += num / j
    return sum+1

totalsum = 0

for i in range(1, 10000):
    sum = 0
    for j in range(2, int(math.sqrt(i))+1):
        if i % j == 0:
            sum += j
            if i/j != j:
                sum += i / j
    if checkAmicable(sum+1) == i and i != sum+1:
        totalsum += i

print(totalsum)

e = time.time()

print(e-s)