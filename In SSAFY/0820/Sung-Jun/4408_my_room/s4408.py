import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    numbers = int(input())
    room_list = [list(map(int, input().split())) for _ in range(numbers)]

    check = [0]*402
    for i in room_list:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]

        for j in range(i[0], i[1]+1):
            check[j] += 1
            if i[1] % 2:
                check[i[1]+1] = 1
    print('#{} {}'.format(tc+1, max(check)))
