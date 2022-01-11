from itertools import combinations

nums = [1, 2, 3]

for i in range(len(nums)+1):
    for combo in combinations(nums, i):
        print(combo)