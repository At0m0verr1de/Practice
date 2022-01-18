import time

start = time.time()


highestCount = 0

for n in range(1, 1000000):
    count = 0
    number = n
    while number != 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = number*3 + 1
        count += 1

    if count > highestCount:
        highestCount = count
        maxNum = n

print(maxNum)

end = time.time()

print(f"Time: {end-start}")
