import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    N, Q = map(int, input().split())
    first_box = [0]*N

    lr_box = []
    for box in range(Q):
        lr_box.append(list(map(int, input().split())))

    change_num = 1
    for num in range(Q):
        for number in range(lr_box[num][0], lr_box[num][1]+1):
            first_box[number-1] = change_num
        change_num += 1

    print('#{0}'.format(tc+1), end=' ')
    print(*first_box)


