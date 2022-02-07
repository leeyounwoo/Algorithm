import sys
from copy import deepcopy


def input():
    return sys.stdin.readline().rstrip()


def getMax(a_i, a_j, b_i, b_j, n):
    new_candies = deepcopy(candies)
    new_candies[a_i][a_j], new_candies[b_i][b_j] = new_candies[b_i][b_j], new_candies[a_i][a_j]
    i = a_i
    ans_a_i = 0
    while new_candies[i][a_j] == new_candies[a_i][a_j] and i >= 0:
        ans_a_i += 1
        i -= 1
    i = a_i + 1
    while i < n and new_candies[i][a_j] == new_candies[a_i][a_j]:
        ans_a_i += 1
        i += 1

    i = b_i
    ans_b_i = 0
    while new_candies[i][b_j] == new_candies[b_i][b_j] and i >= 0:
        ans_b_i += 1
        i -= 1
    i = b_i + 1
    while i < n and new_candies[i][b_j] == new_candies[b_i][b_j]:
        ans_b_i += 1
        i += 1

    j = a_j
    ans_a_j = 0
    while new_candies[a_i][j] == new_candies[a_i][a_j] and j >= 0:
        ans_a_j += 1
        j -= 1
    j = a_j + 1
    while j < n and new_candies[a_i][j] == new_candies[a_i][a_j]:
        ans_a_j += 1
        j += 1

    j = b_j
    ans_b_j = 0
    while new_candies[b_i][j] == new_candies[b_i][b_j] and j >= 0:
        ans_b_j += 1
        j -= 1
    j = b_j + 1
    while j < n and new_candies[b_i][j] == new_candies[b_i][b_j]:
        ans_b_j += 1
        j += 1

    return max(ans_a_i, ans_b_i, ans_a_j, ans_b_j)


dx, dy = [0, 1], [1, 0]
sys.stdin = open('input.txt')
n = int(input())
indexs = [[j for j in range(n)] for i in range(n)]
candies = [list(input()) for _ in range(n)]
ans = 0

for i in range(n):
    for j in range(n):
        a_i = i
        a_j = j
        for k in range(2):
            b_i, b_j = a_i + dx[k], a_j + dy[k]
            if b_i < n and b_j < n:
                flag = getMax(a_i, a_j, b_i, b_j, n)
                if ans < flag:
                    ans = flag
print(ans)
