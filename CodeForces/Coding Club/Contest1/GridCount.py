import math
 
n, k = list(map(int, input().split()))
 
factors = 0
 
for i in range(int(math.sqrt(k)), 0, -1):
    if int(k/i) > n:
        break
    if k % i == 0:
        factors += 2
 
if int(math.sqrt(k)) == math.sqrt(k):
    factors -= 1
 
if factors> 0:
    print(factors)
else:
    print(0)
