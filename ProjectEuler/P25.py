a1 = 1
a2 = 1
an = 0
counter = 2

while len(str(an)) < 1000:
    an = a1 + a2
    a1 = a2
    a2 = an
    counter += 1

print(counter)