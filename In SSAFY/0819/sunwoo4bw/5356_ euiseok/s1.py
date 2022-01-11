import sys
sys.stdin = open('input.txt')
# 칠판에 있는 다섯 개의 단어를 세로로 읽으려 한대
# 자리에 글자가 없으면, 읽지 않고 그 다음 글자로 넘어가

T = int(input())
for tc in range(1, T+1): # 1,2

    word = []
    for _ in range(5): # 1tc 당 5개
        word.append(input())

    # 5개의 word리스트 안에서 최장 찾아줘
    max_len = 0
    for r in word:
        if len(r) > max_len:
            max_len = len(r)

    uiseok_babbling = ''
    for i in range(max_len):
        for j in range(5):
            if i < len(word[j]):
                uiseok_babbling += word[j][i]

    print("#{} {}".format(tc, uiseok_babbling))