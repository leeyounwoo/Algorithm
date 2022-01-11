from itertools import combinations # permutations 두개쓰면 끝!

arr = [1, 2, 3, 4]
n = len(arr)

for r in range(n+1):
    for combo in combinations(arr, r):
        print(combo)
    print()