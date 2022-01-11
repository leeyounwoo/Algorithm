import sys
sys.stdin = open('input.txt')
# 칠판에 있는 다섯 개의 단어를 세로로 읽으려 한대
# 자리에 글자가 없으면, 읽지 않고 그 다음 글자로 넘어가

T = int(input())
for tc in range(1, T+1):
    word = [0] * 5

    max_len = 0

    for i in range(5) :
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])
    print('#{}'.format(tc), end=' ')

    for i in range(max_len):
        for j in range(5):
            # 1. 허락받고 쓰자
            # if len(word[j]) > i :
            #     print(word[j][i], end='')
            # 2. 허락은 무슨 용서를 구하자...
            try :
                print(word[j][i], end='')
            except :
                pass

    print()
