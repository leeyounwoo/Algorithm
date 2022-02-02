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
for com in combinations(players, team_num):
    start = set(com)
    link = list(players - start)
    start = list(start)
    sum_link = 0
    for i in range(len(link)):
        for j in range(i+1, len(link)):
            sum_link += ability[link[i]][link[j]] + ability[link[j]][link[i]]

    sum_start = 0
    for i in range(len(start)):
        for j in range(i+1, len(start)):
            sum_start += ability[start[i]][start[j]] + ability[start[j]][start[i]]
    dif = abs(sum_link - sum_start)
    if ans > dif:
        ans = dif
        if dif == 0:
            break

print(ans)
