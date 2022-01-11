import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # set을 써서 str1에 있는 중복되는 값들을 지워줘
    # str1 in str2 해서 하나하나 비교 ㄱㄱ
    str1 = input()
    str2 = input()

    n_d = set(str1)    # {'Y', 'P', 'X', 'V'}
    # word_len = len(n_d)  # 4 3 10
    #
    # for i in len(n_d): # 4-0 1 2 3
    #     if n_d[i] in str2 :

    word_dic = {}
    for w in str2:
        if w in n_d:    # {'Y', 'P', 'X', 'V'}
            if w in word_dic.keys():
                value = word_dic.get(w)       # key로 value값 얻기
                word_dic[w] = value + 1
            else:
                word_dic[w] = 1
    # 가장 많이 중복된 거-> max value
    max_v = max(word_dic.values())
    print('#{} {}'.format(tc, max_v))