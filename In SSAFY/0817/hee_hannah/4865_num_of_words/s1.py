import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    x = input()
    y = input()
    a = {}
    for i in x:
        a[i] = y.count(i)

    max_v = max(a.values())
    for key, value in a.items():
        if value == max_v:
            print('#{} {}'.format(tc, value))
            break

    # max_v 부터 이방법으로도 가능 이다음 프린트
    # result = max(a.items(), key=lambda pair: pair[1])[1]