import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    new_string = ''
    stack = []
    # 후위 표기법으로 변환
    for char in string:
        if char in '0123456789':
            new_string += char
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == ')':
                    while stack[-1] != '(':
                        new_string += stack.pop()
                    stack.pop()
                elif char == '+':
                    while len(stack) != 0 and stack[-1] != '(':
                        new_string += stack.pop()
                elif char == '*':
                    while len(stack) != 0 and stack[-1] not in '+(':
                        new_string += stack.pop()

                if char != ')':
                    stack.append(char)
    while stack:
        new_string += stack.pop()

    # 계산부분
    for char in new_string:
        if char in '0123456789':
            stack.append(int(char))
        else:
            a = stack.pop()
            b = stack.pop()
            if char == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)

    result = stack.pop()
    print('#{} {}'.format(tc, result))