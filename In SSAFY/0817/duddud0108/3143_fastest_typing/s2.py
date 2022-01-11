import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(T):
    text, pattern = input().split()
    cnt = text.count(pattern)
    print('#{0} {1}'.format(tc + 1, len(text) - (len(pattern)-1)*cnt))