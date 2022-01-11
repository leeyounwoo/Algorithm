import sys
sys.stdin = open("input.txt")
N = int(input())
for tc in range(1, N+1):
    str1, str2 = map(str, input().split())
    if str2 in str1:
        cnt = str1.count(str2)
    total = cnt + len(str1)-len(str2)*cnt
    print('#{} {}'.format(tc, total))