import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
team_num = n // 2
players = set([i for i in range(n)])
ability = [list(map(int, input().split())) for _ in range(n)]

ans = 100 * team_num
for i in range(1, n):
    for com in combinations(players, i):
        start = set(com)
        link = list(players - start)
        start = list(start)
        sum_link = 0
        for k in range(len(link)):
            for j in range(k+1, len(link)):
                sum_link += ability[link[k]][link[j]] + ability[link[j]][link[k]]

        sum_start = 0
        for k in range(len(start)):
            for j in range(k+1, len(start)):
                sum_start += ability[start[k]][start[j]] + ability[start[j]][start[k]]
        dif = abs(sum_link - sum_start)
        if ans > dif:
            ans = dif
            if dif == 0:
                break

print(ans)
