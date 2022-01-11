from itertools import combinations

arr = [1, 2, 3, 4]

n = len(arr)

# Q. 부분집합을 더해서 5가 되는 경우가 있는지?

for r in range(n+1):
    for combo in combinations(arr, r):
        # 여기서 하고싶은일..
        # combo : (1,),(1,3)... 튜플형태로 나옴
        if sum(combo) == 5:
            print('5가되는 경우가 있습니다')

