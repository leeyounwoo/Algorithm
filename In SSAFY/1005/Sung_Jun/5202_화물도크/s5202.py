import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    num = int(input())
    case = [list(map(int, input().split())) for _ in range(num)]
    work_time = list(range(25))

    for i in range(num-1):
        for j in range(i+1, num):
            if len(work_time[case[i][0]:case[i][1]+1]) > len(work_time[case[j][0]:case[j][1]+1]):
                case[i], case[j] = case[j], case[i]

    used_time = []
    cnt = 0
    for work in case:
        if 0 not in work_time[work[0]:work[1]+1] and work not in used_time:
            used_time.append(work)
            for num in range(work[0], work[1]+1):
                work_time[num] = 0
            work_time[work[0]], work_time[work[1]] = 1, 1
            cnt += 1
    print(used_time)
    print(work_time)
    print('#{} {}'.format(tc+1, cnt))

