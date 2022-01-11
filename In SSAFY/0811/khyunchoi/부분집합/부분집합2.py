from itertools import permutations

arr = [1, 2, 3, 4]
n = len(arr)

for r in range(n+1):
    for combo in permutations(arr, r):
        print(combo)
    print()