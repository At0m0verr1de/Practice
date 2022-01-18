import itertools

nums = list(itertools.permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
nums.sort()

answer = "".join(list(map(str, nums[999999])))

print(answer)

