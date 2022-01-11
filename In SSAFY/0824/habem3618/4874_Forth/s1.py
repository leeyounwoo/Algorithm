import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    string = input().split()
    result = []

    try:
        for i in string:

            if i == '.':
                ans = result.pop()
                if len(result) != 0:
                    ans = 'error'
                break

            elif i == '+':
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 + num2)

            elif i == '-':
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 - num2)

            elif i == '*':
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 * num2)

            elif i == '/':
                num2 = result.pop()
                num1 = result.pop()
                result.append(num1 // num2)

            else:
                result.append(int(i))
    except:
        ans = 'error'

    print('#{} {}'.format(tc, ans))
