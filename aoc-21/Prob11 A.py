dataset = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".split("\n")

octopus = []
for j in dataset:
    octopus.append(list(map(int, list(j))))

print(octopus)


def incrementer(data):
    for k in range(len(octopus)):
        for i in range(len(octopus[0])):
            data[k][i] += 1


indexes = []


def network(data):
    flash = 0
    for k in range(10):
        for i in range(10):
            if data[k][i] > 9 and [k, i] not in indexes:
                flash += 1
                indexes.append([k, i])

                if i == 0 and k == 0:
                    data[k+1][i] += 1
                    data[k][i+1] += 1
                elif i == 0 and k == 9:
                    data[k-1][i] += 1
                    data[k][i+1] += 1
                elif i == 9 and k == 0:
                    data[k+1][i] += 1
                    data[k][i-1] += 1
                elif i == 9 and k == 9:
                    data[k-1][i] += 1
                    data[k][i-1] += 1
                elif i == 0:
                    data[k+1][i] += 1
                    data[k][i+1] += 1
                    data[k-1][i] += 1
                elif i == 9:
                    data[k-1][i] += 1
                    data[k][i-1] += 1
                    data[k+1][i] += 1
                elif k == 0:
                    data[k][i-1] += 1
                    data[k][i+1] += 1
                    data[k+1][i] += 1
                elif k == 9:
                    data[k][i-1] += 1
                    data[k][i+1] += 1
                    data[k-1][i] += 1
                else:
                    data[k+1][i+1] += 1
                    data[k][i+1] += 1
                    data[k+1][i] += 1

                    data[k-1][i-1] += 1
                    data[k-1][i] += 1
                    data[k][i-1] += 1

                    data[k-1][i+1] += 1
                    data[k+1][i-1] += 1
    return flash


def zeroer(data):
    for j in indexes:
        data[j[0]][j[1]] = 0


total = 0
for _ in range(100):
    count = 0
    temp = []
    indexes = []
    for j in octopus:
        temp.append("".join(list(map(str, j))))

    print("\n".join(temp) + "\n")

    while True:
        count += 1
        if count == 1:
            incrementer(octopus)

        flashed = network(octopus)
        zeroer(octopus)

        if flashed == 0:
            break

        total += flashed
