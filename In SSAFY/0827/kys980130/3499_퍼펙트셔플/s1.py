import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    words = list(input().split())
    top = []
    down = []
    new_words = []
    if N % 2 == 0:
        for i in range(N//2):
            top.append(words[i])
        for j in range(N//2, N):
            down.append(words[j])
    else:
        for i in range(N//2+1):
            top.append(words[i])
        for j in range(N//2+1, N):
            down.append(words[j])
    try:
        for m in range(len(top)):
            new_words.append(top[m])
            new_words.append(down[m])
    except:
        pass
    print('#{}'.format(tc), end=" ")
    print(' '.join(new_words))
