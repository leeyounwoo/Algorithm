import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1):
    n, m = map(int, input().split())
    check_box = [input() for _ in range(n)]
    print(check_box)

    for i in range(n):
        for j in range(n-m+1):
            a = check_box[i][j:j+m+1]
            b = check_box[i][j+m-1: (j-1) :-1]
            if check_box[i][j:j+m+1] == check_box[i][j+m:i-1:-1]:
                print(check_box[i][j:j+m+1])

