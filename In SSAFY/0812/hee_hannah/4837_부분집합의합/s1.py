import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    a = list(range(1, 13))
    total = []
    N, k = map(int, input().split())
    for i in range(1 << 12):
        for j in range(12):
            if i & (1 << j):

