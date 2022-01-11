import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    case_test = [input() for _ in range(5)]

    result = ''
    for j in range(16):
        for i in range(len(case_test)):
            try:
                result += case_test[i][j]
            except:
                pass
    print('#{} {}'.format(tc+1, result))