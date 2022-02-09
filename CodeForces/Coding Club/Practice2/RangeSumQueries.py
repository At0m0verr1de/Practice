length = int(input())
nums = list(map(int, input().split()))
prefix = [nums[0], nums[0]+nums[1]]
 
for j in range(2, length):
    prefix.append(nums[j] + prefix[j-1])
 
for i in range(int(input())):
    start, end = list(map(int, input().split()))
    if start == end:
        print(nums[start-1])
    else:
        if start-1 == 0:
            print(prefix[end-1])
        else:
            print(prefix[end-1] - prefix[start-2])
