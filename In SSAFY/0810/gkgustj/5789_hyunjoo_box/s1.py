import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1) :
    '''
    N : 박스 개수
    Q : 숫자 변경 횟수
    '''
    N, Q = map(int, input().split())
    box = [0]*N

    for i in range(1, Q+1) :
        # 변경하려는 범위 인덱스
        L, R = map(int, input().split())

        for j in range(L-1, R) :
            box[j] = i

    print(f'#{t}', end=' ')
    for k in range(len(box)) :
        if k == len(box)-1 :
            print(box[k])
        else:
            print(box[k], end=' ')
