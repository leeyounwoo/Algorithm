import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    n, m = map(int, input().split())
    case_num = [[key] for key in range(1, m+1)]
    case = list(map(int, input().split()))
    for i in range(m):
        case_num[i].append(case[i])

    q = []
    for check in range(m):
        if len(q) < n:
            q.append(case_num.pop(0))
        else:
            break

    while len(q) != 1:
        if len(q) < n:
            if case_num:
                q.append(case_num.pop(0))
        now = q.pop(0)
        if now[1] // 2 == 0:
            pass
        else:
            now[1] = now[1] // 2
            q.append(now)
    print('#{} {}'.format(tc+1, q[0][0]))
