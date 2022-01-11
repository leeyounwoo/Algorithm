from itertools import combinations

arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]
n = len(arr)

for r in range(n+1):
    for combo in combinations(arr, r):
        if sum(combo) == 5:
            print(combo)