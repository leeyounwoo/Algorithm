import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N, password = input().split()
    stack = []
    password = list(password.strip())

    for i in password:
        # 스택에 아무것도 없거나 비교할 문자가 스택 마지막 문자랑 다르면 넣기
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    print('#{} {}'.format(tc, ''.join(stack)))