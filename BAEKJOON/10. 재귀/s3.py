from pprint import pprint

def makePattern(prev):
    prev_n = len(prev)
    now_n = prev_n * 3
    new_pattern = [[' ']*now_n for _ in range(now_n)]
    flag_i = 0
    for i in range(0, now_n, prev_n):
        flag_j = 0
        for j in range(0, now_n, prev_n):
            if flag_i == 1 and flag_j == 1:
                flag_j += 1
                continue
            for k in range(prev_n):
                for h in range(prev_n):
                    new_pattern[i+k][j+h] = prev[k][h]
            flag_j += 1

        flag_i += 1
    # pprint(new_pattern)
    return new_pattern

n = int(input())
if n == 3:
    print('***')
    print('* *')
    print('***')
else:
    pattern = [['*', '*', '*'], ['*', ' ', '*'], ['*', '*', '*']]
    while n != 3:
        pattern = makePattern(pattern)
        n /= 3
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            print(pattern[i][j], end='')
        print()
