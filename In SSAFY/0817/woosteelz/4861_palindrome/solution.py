import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    n, m = map(int, input().split())
    table_row = []
    table_col = []
    results = []
    result = ""

    for _ in range(n):  # 가로 배열
        table_row.append(input())

    for k in range(n):  # 세로 배열
        temp = ''
        for i in range(n):
            temp += table_row[i][k]
        table_col.append(temp)

    for i in range(n):
        for j in range(n):
            if m % 2 and table_row[i][j:j + m // 2] == table_row[i][j + m:j + m // 2:-1]:  # m의 길이가 홀수면
                results.append(table_row[i][j:j + m])

            elif table_row[i][j:j + m // 2] == table_row[i][j + m:j + m // 2 - 1:-1]:  # m의 길이가 짝수면
                    results.append(table_row[i][j:j + m])

    for j in range(n):
        for i in range(n):
            if m % 2 and table_col[i][j:j + m // 2] == table_col[i][j + m:j + m // 2:-1]:  # m의 길이가 홀수면
                results.append(table_col[i][j:j + m])

            elif table_col[i][j:j + m // 2] == table_col[i][j + m:j + m // 2 - 1:-1]:  # m의 길이가 짝수면
                results.append(table_col[i][j:j + m])

    print(f"#{tc+1} {''.join(results)}")