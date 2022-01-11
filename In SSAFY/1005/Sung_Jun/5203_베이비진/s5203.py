import sys
sys.stdin = open('input.txt')


def babygin(arr):
    list_num = [0] * 10

    for number in arr:
        list_num[number] += 1

    for idx in range(10):
        if list_num[idx]:
            if idx + 2 < 10 and list_num[idx+1] and list_num[idx+2]:
                return 1
            elif list_num[idx] >= 3:
                return 1
    return 0


T = int(input())
for tc in range(T):
    case = list(map(int, input().split()))
    result = 0
    player1 = []
    player2 = []
    for num in range(len(case)):
        if num % 2:
            player2.append(case[num])
        else:
            player1.append(case[num])

        if num >= 4:
            win1 = babygin(player1)
            win2 = babygin(player2)
            if win1 or win2:
                break

    if win1 == win2:
        result = 0
    elif win1 == 1:
        result = 1
    else:
        result = 2
    print('#{} {}'.format(tc + 1, result))
