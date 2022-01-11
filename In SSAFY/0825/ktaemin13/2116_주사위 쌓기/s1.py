import sys
sys.stdin = open('input.txt')


def dice():  # A-F, B-D, C-E # A B C D E F
    dice_dict = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
    total = N*6
    sum_list = []
    dice_num = 1
    while dice_num < 7:
        cnt = 0
        serch = dice_num
        for i in range(N):
            for j in range(6):
                if i == 0 and arr[i][j] == serch:
                    if arr[i][dice_dict[j]] == 6:
                        cnt += 1
                        break
                    if serch == 5 and arr[i][dice_dict[j]] == 6:
                        cnt += 2
                        break
                    if serch == 6:
                        cnt += 1
                        if arr[i][dice_dict[j]] == 5:
                            cnt += 1
                            break
                        break
                if i > 0 and arr[i][j] == serch:
                    if serch == 6:
                        cnt += 1
                        serch = arr[i][dice_dict[j]]
                        if serch == 5:
                            cnt += 1
                        break
                    if serch == 5 and arr[i][dice_dict[j]] == 6:
                        cnt += 2
                        serch = arr[i][dice_dict[j]]
                        break
                    serch = arr[i][dice_dict[j]]
                    if serch == 6:
                        cnt += 1
                        break
                    elif serch != 6:
                        break
        sum_list.append(total - cnt)
        dice_num += 1
    return print(max(sum_list))



N = int(input())
arr = [list(map(int, (input().split()))) for _ in range(N)]
dice()