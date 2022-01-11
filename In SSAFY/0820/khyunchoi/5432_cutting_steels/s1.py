import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1): # 시간초과
    brackets = input()

    result = 0
    for i in range(len(brackets)-1):
        if brackets[i:i+2] == '((':
            result += 1
            flag = 0
            for j in range(i, len(brackets)):
                if brackets[j] == '(':
                    flag += 1
                    if brackets[j+1] == ')':
                        result += 1
                else:
                    flag -= 1

                if flag == 0:
                    break

    print('#{} {}'.format(tc, result))