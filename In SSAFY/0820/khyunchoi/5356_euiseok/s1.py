import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    words = [input() for _ in range(5)]

    max_idx = 0
    for word in words:
        if max_idx < len(word):
            max_idx = len(word)

    print('#{}'.format(tc), end=' ')
    for j in range(max_idx):
        for i in range(5):
            if len(words[i]) > j:
                print(words[i][j], end='')
    print()