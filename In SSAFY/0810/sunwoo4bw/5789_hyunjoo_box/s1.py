import sys
sys.stdin = open('input.txt')

T = int(input())    #1
for tc in range(1, T + 1):
    n, q = map(int, input().split())
    box_default = [0] * n  # 1 ~ n개 까지 처음엔 모두 0으로

    for i in range(q):
        l, r = map(int, input().split())
        for j in range(l - 1, r):
            box_default[j] = i + 1

    box_default= ' '.join(map(str,box_default))   ##1 12220
    print("#{} {}".format(tc, box_default))
