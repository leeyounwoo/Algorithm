import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    new_string = ''
    stack = []
    # 후위 표기법으로 변환
    for i in string:
        if i.isdigit():
            new_string += i
        else:
            if len(stack) == 0:
                stack.append(i)
            else:
                if i == ')':
                    while stack[-1] != '(':
                        new_string += stack.pop()
                    stack.pop()
                elif i == '+':
                    while len(stack) != 0 and stack[-1] != '(':
                        new_string += stack.pop()
                elif i == '*':
                    while len(stack) != 0 and stack[-1] not in '+(':
                        new_string += stack.pop()

                if i != ')':
                    stack.append(i)
    while stack:
        if stack[-1] == '(':
            stack.pop()
        else:
            new_string += stack.pop()
    # 계산부분
    for i in new_string:
        if i.isdigit():
            stack.append(int(i))
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                stack.append(a + b)
            else:
                stack.append(a * b)

    result = stack.pop()
    print('#{} {}'.format(tc, result))