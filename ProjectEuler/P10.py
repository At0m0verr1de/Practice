import math

def prime(num):
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True

sum = 0

for i in range(2, 2000000):
    if prime(i):
        sum += i


print(sum)