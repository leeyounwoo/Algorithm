import sys
sys.stdin = open('input.txt')

def scan_col(words, M):
    result = ''
    for x in range(len(words[0])):
        for y in range(len(words)-M+1):
            sliced = ''
            for dy in range(M):
                sliced += words[y+dy][x]
            if is_pal(sliced):
                return sliced
    return result

def scan_row(words, M):
    result = ''
    for y in range(len(words)):
        for x in range(len(words[y])-M+1):
            sliced = words[y][x:M+x]
            if is_pal(sliced):
                return sliced
    return result

def is_pal(word):
    if word == word[::-1]:
        return True
    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)]

    # x축 확인
    result_x = scan_row(words, M)
    # 가로 비교
    result_y = scan_col(words, M)

    result = ''
    if result_x:
        result = result_x
    else:
        result = result_y
    print("#{} {}".format(tc, result))