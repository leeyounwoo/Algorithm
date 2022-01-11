import sys
sys.stdin = open("input.txt")
left_list = ['(', '{']
right_list = [')', '}']
result = 1
T = int(input())
for tc in range(1, T+1):
    stack = []
    code = str(input())
    for i in range(len(code)):
        if code[i] in left_list:
            stack.append(code[i])
        if code[i] in right_list:
            if len(stack) == 0:
                result = 0
                break
            else:
                if code[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif code[i] == '}' and stack[-1] == '{':
                    stack.pop()
    if len(stack) != 0:
        result = 0
    print('#{} {}'.format(tc, result))



