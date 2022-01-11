import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    box = ['0' for _ in range(5)]

    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = str(i)

    box = " ".join(box)
    print('#{} {}'.format(tc + 1, box))
