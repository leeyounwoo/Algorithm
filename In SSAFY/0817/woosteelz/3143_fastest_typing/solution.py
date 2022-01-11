import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(TC):
    a, b = map(str, input().split())
    ans = 0
    idx = 0
    while idx < len(a) - len(b) + 1:
        if a[idx:idx+len(b)] == b:
            ans += 1
            idx += len(b)
        else:
            ans += 1
            idx += 1
    if idx < len(a):
        ans += len(a[idx:])

    print('#{} {}'.format(tc+1, ans))
