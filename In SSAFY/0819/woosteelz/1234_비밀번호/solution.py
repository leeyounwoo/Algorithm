import sys
sys.stdin = open('input.txt')

for tc in range(10):
    num, password = input().split()
    stack = []
    for pwd in password:
        if not stack:
            stack.append(pwd)
        else:
            if stack[-1] == pwd:
                stack.pop()
            else:
                stack.append(pwd)
    print('#{} {}'.format(tc+1, ''.join(stack)))