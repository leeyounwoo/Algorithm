import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, 1+T):
    lst = list(input())
    i = 0
    cnt = 0                 # 레이저로 자른 쇠막대기 개수
    pipe = 0                # 쇠막대기

    while i < len(lst):
        if lst[i] == '(' and lst[i + 1] == ')':
            cnt += pipe     # 쇠막대기 개수만큼 세주기
            i += 2
        elif lst[i] == '(':
            pipe += 1
            i += 1
        else:
            pipe -= 1
            cnt += 1
            i += 1
    print('#{} {}'.format(tc, cnt))
