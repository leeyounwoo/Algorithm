import sys
sys.stdin = open("input.txt")



for tc in range(1, 11):
    N, M = 100, 100
    _ = int(input())
    result = []
    data = [input() for _ in range(N)]

    for x in range(len(data[0])):
        for y in range(len(data[0])-M+1):
            word_list = ''
            for i in range(M):
                word_list += data[x][y+i]


    # for x in range(len(data[0])):
    #     for y in range(len(data)-M+1):
    #         word_list = ''
    #         for i in range(M):
    #             word_list += data[y+i][x]
    #         if word_list == word_list[::-1]:
    #             result.append(word_list)
    #         print(result)

