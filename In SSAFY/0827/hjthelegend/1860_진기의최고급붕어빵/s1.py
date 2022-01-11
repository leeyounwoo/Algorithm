import sys
sys.stdin = open('input.txt')

def bubble_sort(time):
    for i in range(len(time)-1, 0, -1):
        for j in range(i):
            if time[j] > time[j+1]:
                time[j], time[j+1] = time[j+1], time[j]

    return time

def bread_king(n, m, k, time):
    bread = 0
    count = 0 # 빵 제조기
    flow_time = 0 # 시간은 흐른다.
    bubble_sort(time)
    while True:
        if count == m:
            bread += k # 이만큼 빵을 제조
            while len(time) > 0 and bread > 0:
                time.pop(0)
                bread -= 1
            count = 0
            if len(time) == 0:
                return 'Possible'
        if flow_time >= time[0]:
            return 'Impossible'
        flow_time += 1
        count += 1
        # print(bread, 'bread')
        # print(time, 'time')
        # print(count, 'count')
        # print(flow_time, 'flow_time')

t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))
    # n명의 사람에게 m초의 시간 k개의 붕어빵
    # time : 손님들 도착시간
    # possible or impossible
    #
    # 1. m초마다 k개의 bread 더하기 : bread += k
    # 2. 손님들은 1명당 1개의 빵만 가져간다.

    answer = bread_king(n, m, k, time)
    print('#{} {}'.format(tc, answer))