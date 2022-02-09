N, target = list(map(int, input().split()))
num = list(map(int, input().split()))
num.sort()
 
rpointer = len(num)-1
lpointer = 0
found = False
 
while rpointer > lpointer:
    current = num[lpointer] + num[rpointer]
    if num[rpointer] + num[rpointer-1] < target:
        break
    if num[0] + num[1] > target:
        break
 
    if current == target:
        found = True
        break
    elif current > target:
        rpointer -= 1
    else:
        lpointer += 1
 
if found:
    print("YES")
else:
    print("NO")
