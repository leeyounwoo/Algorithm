import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(T):
    N, Q = map(int, input().split())

    box = [0] * N                               # N개의 '0' 상자를 생성. Q번의 상자의 값을 변환.

    for i in range(1, Q+1):
        L, R = map(int, input().split())        # 상자와 리스트의 인덱스를 조심// 상자는 1부터, 리스트는 0부터
        for j in range(L-1, R):
            box[j] = int(i)                     # j번째 박스에 i를 넣어줌


    print('#{0}'.format(tc+1), *box)