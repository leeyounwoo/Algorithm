import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    word_list = [list(input()) for _ in range(N)]

    print(word_list)
