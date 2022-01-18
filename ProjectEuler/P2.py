an_2 = 1
an_1 = 2
an = 3
sum = 0

while True:
    an_2 = an_1
    an_1 = an
    an = an_2 + an_1
    print(an)
    if an % 2 == 0:
        sum += an
    if an > 4000000:
        break

print(sum+2)
