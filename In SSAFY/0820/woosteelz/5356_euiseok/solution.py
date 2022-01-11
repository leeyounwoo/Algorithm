import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(TC):
    words = []
    for _ in range(5):
        temp = input()
        temp += '*' * (15 - len(temp))
        words.append(temp)
    ans = ''
    for i in range(15):
        for j in range(5):
            if not words[j][i] == '*':
                ans += words[j][i]
    print('#{} {}'.format(tc + 1, ans))