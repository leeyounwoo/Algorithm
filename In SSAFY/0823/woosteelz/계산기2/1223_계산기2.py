import sys
sys.stdin = open('input.txt')

def post_fix(string):
    stack = []
    ans = ''
    for s in string:
        if s == '*':
            stack.append(s)
        elif s == '+':
            while stack:
                ans += stack.pop()
            stack.append(s)
        else:
            ans += s

    while stack:
        ans += stack.pop()
    return ans

def cal_post_fix(string):
    stack = []
    token = ['+', '*']

    for s in string:
        if not s in token:
            stack.append(int(s))
        else:
            if s == '+':
                stack.append(stack.pop() + stack.pop())
            elif s == '*':
                stack.append(stack.pop() * stack.pop())
    return stack[0]

for tc in range(10):
    n = int(input())
    string = input()
    print('#{} {}'.format(tc+1, cal_post_fix(post_fix(string))))
