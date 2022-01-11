import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    steels = input()
    ans = 0
    stick = 0
    idx = 0
    while idx < len(steels):
        if steels[idx] == '(' and steels[idx+1] == ')':
            ans += stick
            idx += 2
        elif steels[idx] == '(':
            stick += 1
            idx += 1
        else:
            ans += 1
            stick -= 1
            idx += 1
    ans += stick
    print('#{} {}'.format(tc+1, ans))
