import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(T):
    drive, goal, stop_num = map(int, input().split())
    stops = [0] * (goal + 1)
    charge_stops = list(map(int, input().split()))
    for i in charge_stops:
        stops[i] = 1
    now = 0
    count = 0
    flag = 1
    while flag and now < goal:
        for i in range(now + drive, now, -1):
            if stops[i] == 1:
                now = i
                count += 1
                if i + drive + 1 > goal:
                    flag = 0
                break
        else:
            count = 0
            break
    print('#{} {}'.format(T, count))


