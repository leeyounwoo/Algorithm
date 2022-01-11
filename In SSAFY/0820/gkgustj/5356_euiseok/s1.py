import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    string = []

    for _ in range(5):
        string.append(input())

    result = ''
    for i in range(16):
        for s in string:
            if len(s) > i:
                result += s[i]

    print('#{} {}'.format(t, result))