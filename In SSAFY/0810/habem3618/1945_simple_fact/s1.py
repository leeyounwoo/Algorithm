import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    number = int(input())
    result = [0 for _ in range(5)]

    while number > 1:
        if not number % 2:
            number = number // 2
            result[0] += 1

        elif not number % 3:
            number = number // 3
            result[1] += 1

        elif not number % 5:
            number = number // 5
            result[2] += 1

        elif not number % 7:
            number = number // 7
            result[3] += 1

        elif not number % 11:
            number = number // 11
            result[4] += 1
    result = list(map(str, result))
    result = " ".join(result)

    print('#{} {}'.format(tc + 1, result))
