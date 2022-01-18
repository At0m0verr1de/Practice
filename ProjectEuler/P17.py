letterCountUnder20 = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3
               , 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8}

letterCountAfter20 = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}

sum = 0

for i in range(1, 20):
    sum += letterCountUnder20[int(str(i))]

for i in range(20, 100):
    sum += letterCountAfter20[int(str(i)[0])] + letterCountUnder20[int(str(i)[1])]

for i in range(100, 1000):
    if i % 100 == 0:
        sum += letterCountUnder20[int(str(i)[0])] + len('hundred')
    elif i % 100 < 20:
        sum += letterCountUnder20[int(str(i)[0])] + letterCountUnder20[int(str(i)[1:])]\
           + len('and') + len('hundred')
    elif i % 10 == 0:
        sum += letterCountUnder20[int(str(i)[0])] + letterCountAfter20[int(str(i)[1])]\
           + len('and') + len('hundred')
    else:
        sum += letterCountUnder20[int(str(i)[0])] + letterCountAfter20[int(str(i)[1])]\
            + letterCountUnder20[int(str(i)[2])] + len('and') + len('hundred')

print(sum+11)
