import sys
sys.stdin = open('input.txt')


def ispal(string):
    l = len(string)
    if l % 2 and string[:l//2] == string[:l //2:-1]:
        return True
    elif string[:l//2] == string[:l//2-1:-1]:
        return True
    return False


for tc in range(10):
    num = int(input())
    table_row = []
    table_col = []
    ans = []

    for _ in range(100):  # 가로 배열
        table_row.append(input())

    for k in range(100):  # 세로 배열
        temp = ''
        for i in range(100):
            temp += table_row[i][k]
        table_col.append(temp)

    for i in range(100):
        for j in range(100):
            for k in range(100-j + 1):
                if ispal(table_row[i][j:j+k]):
                    ans.append(len(table_row[i][j:j+k]))
                if ispal(table_col[i][j:j+k]):
                    ans.append(len(table_col[i][j:j+k]))

    print('#{} {}'.format(tc+1, max(ans)))


