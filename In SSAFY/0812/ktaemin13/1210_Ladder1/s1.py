import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = input()
    ladder = [list(map(int, (input().split()))) for _ in range(100)]

    result = 0
    for i in range(100):
        j = 0
        if ladder[j][i] == 1:
            while j < 99:
                j += 1
                if i != 99 and ladder[j][i+1] == 1:
                    while i != 99 and ladder[j][i+1] == 1:
                        i += 1
                elif i != 0 and ladder[j][i-1] == 1:
                    while i != 0 and ladder[j][i-1] == 1:
                        i -= 1
        if ladder[j][i] == 2:
            break
        else:
            result += 1
    print('#{0} {1}'.format(tc+1, result))