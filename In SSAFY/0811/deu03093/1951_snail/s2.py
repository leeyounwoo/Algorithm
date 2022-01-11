from pprint import pprint
import sys

sys.stdin = open('input.txt')
for T in range(1, int(input()) + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    flag_even = 0
    if n % 2:
        circle_num = n // 2 + 1
    else:
        circle_num = n // 2
        flag_even = 1

    count = 1
    for circle in range(circle_num):
        # circle 마다 시작값 달라짐.
        start_count = count
        for i in range(circle, n - circle):
            # 첫째 줄
            if i == circle:
                for j in range(circle, n - circle):
                    snail[i][j] = count
                    count += 1

            # 둘째 줄
            elif i == circle + 1:
                # 둘째 줄의 왼쪽이 n과 circle에 의한 규칙이 있음.
                # start_count + 이번 circle에서 더해지는 count
                snail[i][circle] = start_count + (4 * (n - circle * 2) - 5)
                # 둘째 줄의 오른쪽은 첫째 줄의 오른쪽 값보다 1 큼
                snail[i][n - circle - 1] = snail[i - 1][n - circle - 1] + 1
                # 한 줄에 2개씩 증가
                count += 2
            # 마지막 줄
            elif i == n - circle - 1:
                # 마지막 줄의 가장 오른쪽 숫자는 start_count + (첫째 줄의 증가한 개수) + (세로로 증가한 개수)
                snail[i][n - circle - 1] = start_count + (2 * (n - circle * 2) - 2)
                # 가장 오른쪽부터 왼쪽으로 가면서 1씩 증가
                for j in range(n - circle -2, circle - 1, -1):
                    snail[i][j] = snail[i][j + 1] + 1
                    count += 1
                # 다음 circle의 첫 할당을 위해 1 증가
                count += 1
            # 나머지
            else:
                # 왼쪽은 이전 값에서 감소, 오른쪽은 이전 값에서 증가
                snail[i][circle] = snail[i - 1][circle] - 1
                snail[i][n - circle - 1] = snail[i - 1][n - circle - 1] + 1
                count += 2

    print(f'#{T}')
    for i in range(len(snail)):
        for j in range(len(snail[i])):
            print(snail[i][j], end=' ')
        print()
