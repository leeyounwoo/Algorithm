from itertools import combinations

arr = [1, 2, 3, 4]

n = len(arr)

for r in range(n+1): # r 몇개뽑을지
    for combo in combinations(arr, r):
        print(combo)
    print()
