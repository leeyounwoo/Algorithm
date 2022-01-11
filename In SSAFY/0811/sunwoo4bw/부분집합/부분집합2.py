from itertools import combinations    # 순열(permutations), combinations -> 모든 경우의 수를 구할 때 씀

arr = [1,2,3,4]
n = len(arr)

for r in range(n+1):  # 0 1 2 3 4
    for combo in combinations(arr, r):
        print(combo)
    print()           #튜플 형태로 나옴