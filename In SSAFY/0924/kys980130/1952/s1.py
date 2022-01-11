import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    day, month, three, year = map(int, input().split())
    schedule = list(map(int, input().split()))
    total1 = 0
    total2 = 0
    for i in range(12):
        if schedule[i] == 0:
            pass
        else:
            if schedule[i] * day > month:
                if i <= 9 and month + schedule[i+1] * day + schedule[i+2] * day < three:
                    total1 += month + schedule[i+1] * day + schedule[i+2] * day
                    schedule[i+1] = 0
                    schedule[i+2] = 0
                elif i <= 9 and month + month + schedule[i+2] * day < three:
                    total1 += month + month + schedule[i+2] * day
                    schedule[i + 1] = 0
                    schedule[i + 2] = 0
                elif i <= 9 and month + schedule[i+1] * day + month < three:
                    total1 += month + schedule[i+1] * day + month
                    schedule[i + 1] = 0
                    schedule[i + 2] = 0
                elif i <= 9 and (schedule[i]+schedule[i+1]+schedule[i+2])*day < three:
                    total1 += schedule[i]+schedule[i+1]+schedule[i+2]*day
                    schedule[i + 1] = 0
                    schedule[i + 2] = 0
                elif i <= 9:
                    total1 += three
                    schedule[i + 1] = 0
                    schedule[i + 2] = 0
                elif i == 10 and month * 2 > three:
                    total1 += three
                    schedule[i + 1] = 0
                elif i == 11 and month > three:
                    total1 += three
            else:
                total1 += day * schedule[i]
    for i in range(12):
        if schedule[i] == 0:
            pass
        else:
            if i <= 9 and month * 3 > three:
                total2 += three
                schedule[i+1] = 0
                schedule[i+2] = 0

            elif i == 10 and month * 2 > three:
                total2 += three
                schedule[i+1] = 0
            elif i == 11 and month > three:
                total2 += three
            else:
                if schedule[i] * day > month:
                    total2 += month
                else:
                    total2 += schedule[i] * day
    print(min(total1, year))
