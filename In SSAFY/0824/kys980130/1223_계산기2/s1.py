import sys
sys.stdin = open("input.txt")
T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    stack = []
    cal = ''

    # 수식을 읽는 부분
    for char in string:
        if char == '*':
            stack.append(char)
        elif char == '+':
            while stack:
                cal += stack.pop()
            stack.append(char)
        else:
            cal += char

    while stack:
        cal += stack.pop()

    result = []
    for j in cal:
        if j == '+':
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(num1+num2)
        elif j == '*':
            num1 = int(result.pop())
            num2 = int(result.pop())
            result.append(num1*num2)
        else:
            result.append(j)
    print('#{} {}'.format(tc, result.pop()))


