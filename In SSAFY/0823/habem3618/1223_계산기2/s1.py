import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    string = input()
    stack = []
    ans = ''

    # 수식을 읽는 부분
    for i in string:
        if i == '*':
            stack.append(i)

        elif i == '+':
            while stack:
                ans += stack.pop()
            stack.append(i)
        else:
            ans += i

    while stack:
        ans += stack.pop()

    result = []
    for i in ans:
        if i == '+':
            num2 = result.pop()
            num1 = result.pop()
            result.append(num1 + num2)

        elif i == '*':
            num2 = result.pop()
            num1 = result.pop()
            result.append(num1 * num2)

        else:
            result.append(int(i))

    print('#{} {}'.format(tc, result[0]))
