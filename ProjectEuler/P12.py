import math
import time

start = time.time()

an = 0
for i in range(1, 100000):
    count = 0
    an = i * (i+1)/2

    for k in range(1, int(math.sqrt(an)+1)):
        if an % k == 0:
            count += 2
    if count > 300:
        print(count)
    if count > 500:
        print(an)
        break

end = time.time()

print(f"Time taken {end-start}")