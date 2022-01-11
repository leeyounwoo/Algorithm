import sys
sys.stdin = open("input.txt")
for tc in range(1, 11):
    N, num_list = input().split()
    stack = []
    for i in num_list:
        if len(stack) > 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print('#{}'.format(tc), end=' ')
    print(''.join(map(str, stack)))