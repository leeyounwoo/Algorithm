import sys
sys.stdin = open('input.txt')


def check_pal(word):
    if word == word[::-1]:
        return True
    return False


def find_pal(N, M, letters):

    for i in range(N):
        for j in range(N):
            if i < N-M+1:
                tempword = ''
                for k in range(M):
                    tempword += letters[i+k][j]
                if check_pal(tempword):
                    return tempword
            if j < N-M+1:
                tempword = letters[i][j:j+M]
                if check_pal(tempword):
                    return tempword


T = int(input())

answer = []
for tc in range(1, T+1):

    N, M = map(int, input().split())

    letters = [input() for _ in range(N)]

    result = find_pal(N, M, letters)
    answer.append(result)

for tc in range(1, T+1):
    print('#{0} {1}'.format(tc, answer[tc-1]))