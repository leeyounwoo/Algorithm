import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    numbers = list(map(int, input()))

    result = [0, 0]  # run, triplet

    count = [0 for _ in range(0, 10)]
    for i in range(len(numbers)):
        count[numbers[i]] += 1

    # find triplet
    for i in range(len(count)):
        if count[i] >= 3:
            result[1] += count[i] // 3
            count[i] = 0

    # find run
    for i in range(0, len(count) - 2):
        if (count[i] == 1 and count[i + 1] == 1 and count[i + 2] == 1):
            result[0] += 1
            count[i] = 0
            count[i + 1] = 0
            count[i + 2] = 0

    if result[0] == 2 or result[1] == 2:
        result = True
    elif result[0] == 1 and result[1] == 1:
        result = True
    else:
        result = False
    print(f'#{tc} {result}')



