import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    string = input()
    new_string = ''
    stack = []

    for char in string:
        if char in '0123456789':
            new_string += char
        else:
            if len(stack) == 0:
                stack.append(char)
            else:
                if char == '+':
                    while len(stack) != 0:
                        new_string += stack.pop()
                else:
                    while len(stack) != 0 and stack[-1] != '+':
                        new_string += stack.pop()
                stack.append(char)
    while stack:
        new_string += stack.pop()

    for char in new_string:
        if char in '0123456789':
            stack.append(char)
        else:
            if char == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a)+int(b)))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(str(int(a) * int(b)))

    result = stack.pop()
    print('#{} {}'.format(tc, result))