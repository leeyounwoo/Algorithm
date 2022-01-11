import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    stack = []
    s = input()
    for i in range(len(s)):
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()

    print('#{} {}'.format(tc + 1, len(stack)))

