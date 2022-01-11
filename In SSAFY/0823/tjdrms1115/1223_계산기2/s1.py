import sys
sys.stdin = open('input.txt')

# T = int(input())
T = 10

answer = []
for tc in range(1, T+1):
    N = int(input())
    seq = input()

    stack = []
    operator = {'+': 1, '*': 2}
    postfix_expression = ''
    for i in range(N):
        if seq[i] in '0123456789':
            postfix_expression += seq[i]
        elif seq[i] in operator:
            while len(stack) > 0 and operator[stack[-1]] >= operator[seq[i]]:
                postfix_expression += stack.pop()
            stack.append(seq[i])
    for i in range(len(stack)):
        postfix_expression += stack.pop()

    if not stack:
        for i in range(len(postfix_expression)):
            if postfix_expression[i] in '0123456789':
                stack.append(int(postfix_expression[i]))
            elif postfix_expression[i] in operator:
                if postfix_expression[i] == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif postfix_expression[i] == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a * b)

    result = stack.pop()
    answer.append(result)

for tc in range(1, T+1):
    print('#{} {}'.format(tc, answer[tc-1]))
