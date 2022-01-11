import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    word_list = [list(map(str, input())) for _ in range(5)]
    length = []
    max_length = 0
    new_list = ''
    for i in range(5):
        length.append(len(word_list[i]))
        for j in length:
            if j > max_length:
                max_length = j
    for i in range(max_length):
        for j in range(5):
            if i < len(word_list[j]):
                new_list += word_list[j][i]
    print('#{} {}'.format(tc, new_list))
