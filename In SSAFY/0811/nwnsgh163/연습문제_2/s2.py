
# 치트키 ( 순열, 조합 등의 모든 경우의 수 구하는 것)
from itertools import combinations


arr = [1, 2, 3, 4]
n = len(arr)

# Q. 부분집합을 더해서 5가 되는 경우가 있는가?

for r in range(n+1):
    for combo in combinations(arr, r):

        # 여기서 하고싶은일 수행
        # combo : (1,), (1,3) ....
        if sum(combo) == 5:
            print('5가 되는 경우가 있습니다!')

