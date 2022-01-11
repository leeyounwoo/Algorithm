
# 치트키 ( 순열, 조합 등의 모든 경우의 수 구하는 것)
from itertools import combinations


arr = [1, 2, 3, 4]
n = len(arr)

for r in range(n+1):
    for combo in combinations(arr, r):
        print(combo)
    print()