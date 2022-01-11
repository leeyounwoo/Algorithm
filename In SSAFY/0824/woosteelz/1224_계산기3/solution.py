import sys
sys.stdin = open('input.txt')

def in_to_post(string):
    postfix = ''
    stack = []
    for s in string:
        if s.isdigit():
            postfix += s
        else:
            # 닫는 괄호면 여는 괄호를 만날때까지 stack에서 pop
            if s == ')':
                while stack:
                    if stack[-1] == '(':
                        break
                    postfix += stack.pop()
                stack.pop()
            # * 이면 *이 나올때까지 pop
            elif s == '*':
                while stack:
                    if not stack[-1] == '*':
                        break
                    postfix += stack.pop()
                stack.append(s)
            # + 이면 여는 괄호가 나올때까지 pop
            elif s == '+':
                while stack:
                    if stack[-1] == '(':
                        break
                    postfix += stack.pop()
                stack.append(s)
            else:
                stack.append(s)

    while stack:
        postfix += stack.pop()
    return postfix

def cal_post(string):
    stack = []
    token = ['+', '*']
    for s in string:
        if s in token:
            if s == '+':
                stack.append(stack.pop() + stack.pop())
            elif s == '*':
                stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(s))
    return stack

for tc in range(10):
    num = int(input())
    string = input()
    print('#{} {}'.format(tc+1, *cal_post(in_to_post(string))))