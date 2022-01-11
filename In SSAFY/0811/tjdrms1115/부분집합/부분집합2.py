from itertools import combinations

arr  = [1, 2, 3, 4]
n = len(arr)

for r in range(n+1): # r : 뽑을 원소의 개수, 0~4
    for combo in combinations(arr, r):
        print(combo)
    print()
