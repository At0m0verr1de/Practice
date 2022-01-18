zone = {}

with open("input.txt") as f:
    y = 0
    for line in f.readlines():
        x = 0
        for char in line.strip():
            zone[(x, y, )] = int(char)
            x += 1
        y += 1

width, height = x, y
lows = []
candidates = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for i, ((x, y), value) in enumerate(zone.items()):
    ok = True
    for c_x, c_y in candidates:
        newx = x + c_x
        newy = y + c_y
        if newx < 0 or newx >= width or newy < 0 or newy >= height:
            continue  # off map
        newpoint = (newx, newy, )
        if zone[newpoint] <= value:
            ok = False
            break
    if ok:
        lows.append((x, y, ))

def find_basin(point, in_basin):
    # from the starting point, explore points around it recursing into each
    in_basin.update([point])
    for c_x, c_y in candidates:
        newx = point[0] + c_x
        newy = point[1] + c_y
        if newx < 0 or newx >= width or newy < 0 or newy >= height:
            continue  # off map
        newpoint = (newx, newy, )
        if newpoint in in_basin:
            continue  # already in basin, ignore
        if zone[newpoint] == 9:
            continue  # basin bountry
        find_basin(newpoint, in_basin)

    return in_basin

basin_sizes = []
for point in lows:
    basin_sizes.append(len(find_basin(point, set())))

basin_sizes.sort(reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])