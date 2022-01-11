import sys
sys.stdin = open('input.txt')

def find_set(x):
    while p[x] != x :
        x = p[x]
    return x

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N: 사람 수, M: 신청서 수
    edges = list(map(int, input().split()))

    # p = [i for i in range(N+1)] # 대표 원소를 각자 자신으로 초기화
    p = list(range(N+1)) # 위랑 똑같음

    for i in range(M):
        a = edges[2 *i]
        b = edges[2 *i +1]

        p[find_set(b)] = find_set(a)
    ans = 0
    for i in range(1, N+1):
        if p[i] == i:
            ans += 1
    print('#{} {}'.format(tc, ans))

