import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    n, k = map(int, input().split())
    test = []
    for _ in range(n):
        test.append(list(map(int, input().split())))

    white_block = []
    for y_num in range(n):
        block_num = 0
        for x_num in range(n):
            if test[y_num][x_num] == 1:
                block_num += 1
            else:
                white_block.append(block_num)
                block_num = 0
        if test[y_num][-1] == 1:
            white_block.append(block_num)

    for x_num in range(n):
        block_num = 0
        for y_num in range(n):
            if test[y_num][x_num] == 1:
                block_num += 1
            else:
                white_block.append(block_num)
                block_num = 0
        if test[-1][x_num] == 1:
            white_block.append(block_num)

    results = 0
    for result in white_block:
        if result == k:
            results += 1
    print('#{0} {1}'.format(tc + 1, results))



