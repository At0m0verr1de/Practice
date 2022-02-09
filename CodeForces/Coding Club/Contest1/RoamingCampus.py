import itertools
 
hostels, k = list(map(int, input().split()))
 
numbers = [x for x in range(2, hostels+1)]
counter = 0
 
arrangement = []
 
for i in range(hostels):
    arrangement.append(list(map(int, input().split())))
 
perms = itertools.permutations(numbers)
 
for i in perms:
    sum = 0
    for j in range(len(i)-1):
        sum += arrangement[i[j]-1][i[j+1]-1]
 
    sum += arrangement[0][i[0]-1] + arrangement[0][i[-1]-1]
    if sum == k:
        counter += 1
 
print(counter)
