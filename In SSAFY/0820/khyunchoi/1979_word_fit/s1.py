import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    size, word_length = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(size)]

    result = 0
    for i in range(size):
        for j in range(size):
            if puzzle[i][j] == 1:
                if j == 0 or (j > 0 and puzzle[i][j-1] == 0):
                    cnt = 0
                    tmp_j = j
                    while tmp_j < size and puzzle[i][tmp_j] == 1:
                        cnt += 1
                        tmp_j += 1

                    if cnt == word_length:
                        result += 1

                if i == 0 or (i > 0 and puzzle[i-1][j] == 0):
                    cnt = 0
                    tmp_i = i
                    while tmp_i < size and puzzle[tmp_i][j] == 1:
                        cnt += 1
                        tmp_i += 1

                    if cnt == word_length:
                        result += 1

    print('#{} {}'.format(tc, result))