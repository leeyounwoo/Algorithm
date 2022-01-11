from itertools import combinations

arr = [-1, 5, 10, 7 -5, 9, 2, 3, 0, 15]
n = len(arr)

for r in range(n+1):
    for combo in combinations(arr, r):
        if sum(combo) == 5:
            print('합이 5가 되는 경우가 있습니다!')
