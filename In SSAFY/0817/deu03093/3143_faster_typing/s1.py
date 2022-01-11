import sys

sys.stdin = open('input.txt')


for T in range(1, int(input()) + 1):
    string, macro = map(str, input().split())
    ans = 0

    i = 0
    while i < len(string):
        if string[i] == macro[0]:
            for j in range(len(macro)):
                if i + j >= len(string) or string[i + j] != macro[j]:
                    break
            else:
                i += len(macro) - 1
        i += 1
        ans += 1

    print('#{} {}'.format(T, ans))
