import sys

sys.stdin = open('input.txt')
for T in range(1, 1+int(input())):
    stack = []
    string = input()
    for i in range(len(string)):
        if not len(stack) or string[i] != stack[-1]:
            stack.append(string[i])
        else:
            stack.pop()

    print('#{} {}'.format(T, len(stack)))