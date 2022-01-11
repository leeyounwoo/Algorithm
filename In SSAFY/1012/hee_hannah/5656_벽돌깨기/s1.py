import sys
sys.stdin = open('input.txt')


t = int(input())
for tc in range(1, t+1):
    print('#{}'.format(tc), end=" ")
    attack, width, height = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(height)]
