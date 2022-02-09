number = input()
sum = 0
for j in number:
    sum += int(j)

if int(number) % 10 == 0:
    print(10)
else:
    print(sum)
