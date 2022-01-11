import sys
sys.stdin = open('input.txt')

T= int(input())
for test_case in range(1,T+1):
    max_word =[]
    words = []
    almost_ans = []
    #어떤 글자들이 있는지
    for suk in range(5):
        words.append(input())
    print(words)
    #몇번 읽기 시작할건지
    for i in words:
        max_word.append(len(i))
    long_range = max(max_word)

    # 0 씩 long_range 만큼 5줄 소환하고, 거기에 값넣어
    # 그 다음 그 값들을 뺄건데 만약 0이면 continue 하도록 하자


    # part 1
    # for i in range(5):
    #     result = [0] * long_range
    #     print(result)
    # for j in range(long_range):
    #     for k in range(5):
    #         result[k][j] = words[k][j]

    # part 2

    for j in range(long_range):
        for i in range(5):
            if j < len(words[i]):
                almost_ans.append(words[i][j])


    # part 3

    # try:
    #     for j in range(long_range):
    #         for i in range(5):
    #             almost_ans.append(words[i][j])
    # except IndexError:
    #     pass
    for i in almost_ans:
        print(i,end ="")