import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    n, pw = input().split()

    stack = []
    for i in range(int(n)):
        if stack and pw[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(pw[i])

    print('#{} {}'.format(t, ''.join(stack)))