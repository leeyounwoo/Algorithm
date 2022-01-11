import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    A, B = input().split()
    len_B = len(B)

    i = 0
    cnt = 0
    while i < len(A):
        # 슬라이싱에서는 인덱스에러가 안난다?
        if A[i:i+len_B] == B:
            i = i+len_B
            cnt += 1
        else:
            i += 1
            cnt += 1

    print('#{} {}'.format(t, cnt))