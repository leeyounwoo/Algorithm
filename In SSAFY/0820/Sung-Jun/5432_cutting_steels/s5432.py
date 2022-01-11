import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    test = input()

    stack = []
    ans = 0
    for num in range(len(test)):
        if test[num] == '(':
            stack.append(test[num])
        elif test[num] == ')':
            if test[num-1] + test[num] == '()':
                stack.pop()
                ans += len(stack)
            else:
                ans += 1
                stack.pop()

    print('#{} {}'.format(tc+1, ans))