import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    money = int(input())
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change_number = [0] * len(change)

    for idx, bill in enumerate(change):
        change_number[idx] = money // bill
        money = money % bill

    result = ' '.join(list(map(str, change_number)))
    print(f'#{tc} ')
    print(result)