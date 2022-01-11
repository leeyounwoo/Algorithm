import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    full_word, word = input().split()
    N = len(full_word)
    M = len(word)

    if word in full_word :
        count = full_word.count(word)             # count 1, 2

    for c in range(count) : # 0
        full_word.replace(word,'',count)
        result = full_word.replace(word,'',count)  # result na, aku

        second_count = 0
        for i in result :
            second_count += 1

    print('#{} {}'.format(tc, count + second_count))
