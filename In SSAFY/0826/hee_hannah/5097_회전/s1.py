import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    i = 0
    while i < M: # M번만큼 돌리면 종료
        a = queue.pop(0) # 뽑고
        queue.append(a) #넣고 반복
        i += 1

    print('#{} {}'.format(tc, queue[0])) # 큐의 첫번째 자리 프린트
