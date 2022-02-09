length, target = list(map(int, input().split()))
array = list(map(int, input().split()))

array.sort()

rpointer = 0
lpointer = 1
total = 0

while lpointer < length:
    if array[lpointer] - array[rpointer] >= target:
        total += length-lpointer
        rpointer += 1
    else:
        lpointer += 1

print(total)
