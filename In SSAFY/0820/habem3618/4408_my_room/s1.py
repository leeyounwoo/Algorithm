import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room_list = [list(map(int, input().split())) for _ in range(N)]

    cnt = [0] * 201
    for room in room_list:
        if room[0] < room[1]:
            start = (room[0] + 1) // 2
            end = (room[1] + 1) // 2
        else:
            end = (room[0] + 1) // 2
            start = (room[1] + 1) // 2

        for i in range(start, end+1):
            cnt[i] += 1

    print('#{} {}'.format(tc, max(cnt)))
