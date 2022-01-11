import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())
    arr = [0] * N

    for i in range(1, Q + 1):
        L, R = map(int, input().split())

        for j in range(L - 1, R):
            arr[j] = i

    print("#{} {}".format(tc + 1, ' '.join(map(str, arr))))