import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    guests = list(map(int, input().split()))
    result = 'Possible'

    bread = [0] * (max(guests) + 1)

    # 정해진 시간(인덱스)마다 만들어진 빵 개수를 리스트 값을 넣어줌
    for i in range(M, len(bread), M):
        bread[i] = K

    # 손님이 온 시간보다 전에 만들어진 빵이 있다면
    for guest in guests:
        for i in range(guest, -1, -1):
            if bread[i]:
                bread[i] -= 1
                break
        # break 하지 못하고 반복문이 끝나면(빵이 없다면)
        else:
            result = 'Impossible'

    print('#{} {}'.format(tc, result))

