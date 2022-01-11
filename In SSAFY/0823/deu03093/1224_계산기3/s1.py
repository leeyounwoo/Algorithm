import sys
sys.stdin = open('input.txt')

def make_postfix(string):
    operation = []
    stack = []
    for i in range(len(string)):
        if string[i] in numbers:
            stack.append(string[i])
        else:
            if not operation or level_in[operation[len(operation) - 1]] < level_out[string[i]]:
                operation.append(string[i])
            else:
                while operation and level_in[operation[len(operation) - 1]] >= level_in[string[i]]:
                    op = operation.pop()
                    if op == '(':
                        break
                    stack.append(op)
                if string[i] != ')':
                    operation.append(string[i])

    for i in range(len(operation)):
        stack.append(operation.pop())
    return stack


def cal_postfix(arr):
    stack = []
    for i in range(len(arr)):
        if arr[i] in numbers:
            stack.append(arr[i])
        else:
            if arr[i] == '+' or arr[i] == '*':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if arr[i] == '+':
                    temp = num1 + num2
                else:
                    temp = num2 * num1
                stack.append(temp)
    return stack[0]


numbers = [str(i) for i in range(1, 10)]
level_out = {'+': 1, '*': 2, '(': 3, ')': 0}
level_in = {'+': 1, '*': 2, '(': 0, ')': 0}
for T in range(1, 11):
    N = int(input())
    string = input()
    postfix_notation = make_postfix(string)
    ans = cal_postfix(postfix_notation)
    print('#{} {}'.format(T, ans))