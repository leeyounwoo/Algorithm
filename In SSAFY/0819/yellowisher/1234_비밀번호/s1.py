import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N, s = input().split()
    stack = []
    for i in range(0, int(N)):
        if not stack or s[i] != stack[-1]:
            stack.append(s[i])
        else:
            stack.pop()

    print("#{} {}".format(tc + 1, ''.join(stack)))


