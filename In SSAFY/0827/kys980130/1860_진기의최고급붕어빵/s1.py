import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    people_cnt, time, bread = map(int, input().split())
    people = list(map(int, input().split()))
    people.sort()
    bread_cnt = 0
    result = 1
    time_curr = time
    for i in range(people_cnt):
        if time_curr <= people[i]:
            bread_cnt += bread
            bread_cnt -= 1
            time_curr += time
            result = 1
        elif people[i] == 0:
            result = 0
            break
        else:
            if bread_cnt >= 1:
                bread_cnt -= 1
                time_curr += time
                bread_cnt += bread
                result = 1
            else:
                result = 0
                break
    if result == 1:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))
