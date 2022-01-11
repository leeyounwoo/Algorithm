import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    st1, st2 = map(str, input().split())
    result = st1.replace(st2, '0')
    print('#{} {}'.format(tc+1, len(result)))