N = int(input())
for tc in range(N):
    M = int(input())
    numbers = list(map(int, input().split()))
    max_num = 0
    min_num = 0
    for number in numbers :
        if number > max_num:
            max_num = number
        if number < max_num:
            min_num = number
    print('#{} {}'.format(tc+1, max_num-min_num))


N = int(input())
for tc in range(N):
    M = int(input())
    numbers = list(map(int, input().split()))
    print('#{} {}'.format(tc+1, max_num-min_num))
