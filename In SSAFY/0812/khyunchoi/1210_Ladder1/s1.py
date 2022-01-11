import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    # 처음 start 어디있는지 찾기
    start = 0
    for i in range(100):
        if ladders[99][i] == 2:
            start = i
            break

    for i in range(99, -1, -1):
        if start + 1 < 100 and ladders[i][start + 1] == 1:
            while start + 1 < 100 and ladders[i][start + 1] == 1:
                start += 1
        elif start - 1 >= 0 and ladders[i][start - 1] == 1:
            while start - 1 >= 0 and ladders[i][start - 1] == 1:
                start -= 1

    print('#{} {}'.format(tc, start))