import sys
sys.stdin = open('input.txt')


T = int(input())

answer = []
for tc in range(1, T+1):

    word1 = input()
    word2 = input()
    word_dict = {}
    for char in word2:
        word_dict[char] = word_dict.get(char, 0) + 1

    result = 0
    for char in word1:
        temp = word_dict.get(char, 0)
        if result < temp:
            result = temp

    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))
