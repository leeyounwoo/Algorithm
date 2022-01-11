import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    data = [input() for _ in range(N)]

    for x in range(len(data[0])):
        for y in range(len(data)-N+1):
            word_list = ''
            for i in range(M):
                word_list += data[x][y+i]
            if word_list == word_list[::-1]:
                result.append(word_list)

    for x in range(len(data[0])):
        for y in range(len(data)-N+1):
            word_list = ''
            for i in range(M):
                word_list += data[y+i][x]
            if word_list == word_list[::-1]:
                result.append(word_list)
    print('#{} {}'.format(tc, result[0]))