import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            boxes[j-1] = i
    boxes = ' '.join(map(str, boxes))
    print('#{} {}'.format(tc+1, boxes))
