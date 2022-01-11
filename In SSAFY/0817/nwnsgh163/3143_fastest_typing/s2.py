import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = input().split()
    len_N = len(N)
    len_M = len(M)