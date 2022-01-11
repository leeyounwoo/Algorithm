from itertools import combinations

arr = [1, 2, 3, 4]
n = len(arr)

for r in range(n+1):
    for combo in combinations(arr, r):
        print(combo)
    print()