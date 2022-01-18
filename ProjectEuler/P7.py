import math
import time
start = time.time()

count = 0

def prime(num):
    for j in range(2, int(math.sqrt(num))+1):
        if num % j == 0:
            return False
    return True


for i in range(2, 1000000):
    if prime(i):
        count += 1
        if count == 10001:
            print(i)
            break

end = time.time()
print(end - start)
