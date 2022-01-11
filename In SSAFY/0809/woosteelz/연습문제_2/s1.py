import sys
# input 파일을 불러오기 위한 코드
sys.stdin = open('input.txt')

x, y = map(int, input().split())

arr_2D = [list(map(int, input().split())) for _ in range(x)]

for i in range(x):
    for j in range(y):
        print(arr_2D[i][j], end=' ')
    print()

for j in range(y):
    for i in range(x):
        print(arr_2D[i][j], end=' ')
    print()

for i in range(x):
    for j in range(y-1, -1, -1):
        print(arr_2D[i][j], end=' ')
    print()

for j in range(y-1, -1, -1):
    for i in range(x):
        print(arr_2D[i][j], end=' ')
    print()

for i in range(x):
    if not i % 2:
        for j in range(y):
            print(arr_2D[i][j], end=' ')
    else:
        for j in range(y-1, -1, -1):
            print(arr_2D[i][j], end=' ')

    print()
