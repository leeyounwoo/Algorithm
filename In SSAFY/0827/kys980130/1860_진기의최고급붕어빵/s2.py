import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    people_cnt, time, bread = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    result = 1
    timeline = [0] * 11112
    for i in range(time, 11112, time):
        timeline[i] = bread
    for m in people:
        count = 0
        if m == 0:
            result = 0
            break
        else:
            for n in range(m+1):
                if timeline[n] >= 1:
                    timeline[n] -= 1
                    result = 1
                    count += 1
                    break
            if count == 0:
                result = 0
                break
    if result == 0:
        print('#{} Impossible'.format(tc))
    else:
        print('#{} Possible'.format(tc))

