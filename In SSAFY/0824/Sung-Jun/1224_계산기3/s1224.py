import sys
sys.stdin = open('input.txt')


def forth(char):
    stack = []
    for check in char:
        if check.isdigit():
            stack.append(int(check))
        else:
            try:
                a = stack.pop()
                b = stack.pop()
                if check == '+':
                    stack.append(b + a)
                elif check == '*':
                    stack.append(b * a)
            except:
                return 'error'
    return stack[0]

T = 10
for tc in range(T):
    number = int(input())
    char = input()
    order_num = '(+*)'

    stack = []
    result = ''
    for check in range(number):
        if char[check] not in ['+', '*', '(', ')']:
            result += char[check]
        else:
            if stack == []:
                stack.append(char[check])
            elif char[check] == '(':
                stack.append(char[check])
            elif char[check] == '+':
                if order_num.find(stack[-1]) < order_num.find(char[check]):
                    stack.append(char[check])
                else:
                    while True:
                        if order_num.find(stack[-1]) < order_num.find(char[check]):
                            stack.append(char[check])
                            break
                        result += stack.pop()
            elif char[check] == '*':
                if order_num.find(stack[-1]) < order_num.find(char[check]):
                    stack.append(char[check])
                else:
                    while True:
                        if order_num.find(stack[-1]) < order_num.find(char[check]):
                            stack.append(char[check])
                            break
                        result += stack.pop()
            else:
                while True:
                    if stack[-1] == '(':
                        stack.pop()
                        break
                    else:
                        result += stack.pop()


    print('#{} {}'.format(tc + 1, forth(result)))



