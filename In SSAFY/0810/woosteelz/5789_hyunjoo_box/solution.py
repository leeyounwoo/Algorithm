import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    N, Q = map(int, input().split())
    box = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i + 1

    print('#{} {}'.format(tc+1, ' '.join(str(k) for k in box)))

