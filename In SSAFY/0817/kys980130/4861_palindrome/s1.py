import sys
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    result = []
    data = [input() for _ in range(N)]

    for i in range(len(data)):
        for i in range(len(data[0])):
            if data[i:i+M] == data[i:i+M][::-1]:
                result.append(data[i:i+M])

    for x in range(len(data[0])):
        # x : 0, 1, 2

        # 여기가 세로축 탐색 (위에서 아래로)
        for y in range(len(data)-M+1):

            # y축에서 M개만큼 글자를 봐야함
            # 예를 들어 M=2인 경우,
            num_list = ''
            for i in range(M):
                num_list += data[y+i][x]

            # 이 시점에서 result에는
            # 'ab'가 담겨있음
            # 그리고 여기서 result에 담긴 값이 팰린드롬인지 확
            if num_list[i:i+N] == num_list[i:i+N][::-1]:
                result.append(num_list[i:i+N])
    print(result)