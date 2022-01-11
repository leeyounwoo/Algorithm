import sys
sys.stdin = open('input.txt')


def boyer_moore(word, sentence):

    w_len = len(word)
    s_len = len(sentence)

    s_idx = 0
    while s_idx + w_len - 1 < s_len:
        temp_idx = w_len - 1
        i = w_len - 1
        while i >= 0:
            if word[i] == sentence[s_idx + temp_idx]:
                temp_idx -= 1
            elif temp_idx != w_len - 1:
                temp_idx = w_len - 1
                continue
            i -= 1
        if temp_idx == -1:
            return 1
        s_idx += temp_idx + 1

    return 0


T = int(input())

answer = []
for tc in range(1, T+1):

    word = input()
    sentence = input()

    result = boyer_moore(word, sentence)

    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
