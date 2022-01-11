import sys
from itertools import combinations

sys.stdin = open('1005/woosteelz/1486_선반/input.txt')

for tc in range(int(input())):
    N, B = map(int, input().split())
    crew = list(map(int, input().split()))
    crew.sort()
    ans = float('inf')
    flag = False
    for i in range(1, len(crew) + 1):
        for combis in combinations(crew, i):
            if sum(combis) - B >= 0:
                ans = min(sum(combis) - B, ans)

    print(f'#{tc + 1} {ans}')
