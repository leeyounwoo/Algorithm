from itertools import combinations

arr = [1, 2, 3, 4]
n = len(arr)

result = 0
for r in range(n+1):
    for combo in combinations(arr, r):
        if sum(combo) == 5:
            print('5가 되는 경우가 있습니다')