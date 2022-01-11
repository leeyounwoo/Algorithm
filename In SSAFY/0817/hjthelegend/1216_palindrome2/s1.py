import sys
sys.stdin = open('input.txt')

def check_row(words)

for _ in range(1, 11):
    tc = int(input())
    words = []
    for _ in range(100):
        words.append(list(input()))

    cnt = 0

    for i in range(100):
        for j in range(100):
            for k in range(100-j + 1):
                if ispal(table_row[i][j:j+k]):
                    ans.append(len(table_row[i][j:j+k]))
                if ispal(table_col[i][j:j+k]):
                    ans.append(len(table_col[i][j:j+k]))