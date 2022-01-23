import sys
from pprint import pprint

def input():
    return sys.stdin.readline().rstrip()


sys.stdin = open('input.txt')
n = int(input())
graph = [[0] * (n*2-1) for _ in range(n)]
start = n-1
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        graph[i][start+j*2] = temp[j]
    start -= 1

start = n-1
dp = [[0] * (n*2-1) for _ in range(n)]
dp[0][n-1] = graph[0][n-1]
for i in range(1, n):
    dp[i][0] = graph[i][0] + dp[i-1][1]
    for j in range(1, (n*2-2)):
        dp[i][j] = graph[i][j] + max(dp[i-1][j-1], dp[i-1][j+1])
    dp[i][-1] = graph[i][-1] + dp[i-1][-2]
print(max(dp[-1]))