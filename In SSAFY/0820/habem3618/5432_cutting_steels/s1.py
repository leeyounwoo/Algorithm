import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    iron = input()
    stack = []
    ans = 0

    for i in range(len(iron)):
        if iron[i] == '(':
            stack.append('(')
        else:
            stack.pop()
            if iron[i-1] == '(':
                # 레이저
                ans += len(stack)
            else:
                ans += 1
    print("#{} {}".format(tc, ans))
