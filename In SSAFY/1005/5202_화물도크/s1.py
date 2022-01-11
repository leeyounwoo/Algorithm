import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    temp = []
    n = int(input())
    for _ in range(n):
        s, e = map(int, input().split())
        temp.append((s, e))

    temp.sort(key = lambda x : x[1])
    print(temp)

    work_end = 0
    result = 0

    for start, end in temp:
        if start >= work_end:
            result += 1
            work_end = end

    print('#{} {}'.format(tc, result))