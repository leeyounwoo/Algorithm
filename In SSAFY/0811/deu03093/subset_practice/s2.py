from itertools import combinations

arr = [1, 2, 3, 4]

n = len(arr)

# 몇개 뽑을지
for r in range(n + 1):
    # combinations()의 첫 번째 인자에 반복되는 리스트나 문자열..., 두 번째 인자는 몇 개를 뽑을 지
    for combo in combinations(arr, r):
        print(combo)
    print()
