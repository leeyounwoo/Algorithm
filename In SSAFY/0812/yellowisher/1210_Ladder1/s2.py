import sys
sys.stdin = open('input.txt')



for tc in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[99][i] == 2:
            y = i
    x = 99
    while x > 0:
        x -= 1  # 위로 한칸 이동
        if y > 0 and arr[x][y - 1] == 1:
            while y > 0 and arr[x][y - 1] == 1:
                y -= 1
        elif y < 99 and arr[x][y + 1] == 1:
            while y < 99 and arr[x][y + 1] == 1:
                y += 1

    print("#{} {}".format(tc+1, y))
