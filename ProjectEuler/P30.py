count = 1
totalSum = 0

while True:
    sum = 0
    count += 1
    for j in str(count):
        sum += int(j)**5
    if sum == count:
        totalSum += sum
    print(f"count: {count} and totalSum: {totalSum}")
