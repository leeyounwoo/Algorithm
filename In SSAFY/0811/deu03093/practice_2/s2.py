from itertools import combinations

arr = [-1, 5, 10, 7, -5, 9, 2, 3, 0, 15]

n = len(arr)
ans = 0
flag = 1
for i in range(n + 1):
    if not flag:
        break
    for combo in combinations(arr, i):
        if sum(combo) == 3:
            ans = 1
            flag = 0
            break
print(ans)